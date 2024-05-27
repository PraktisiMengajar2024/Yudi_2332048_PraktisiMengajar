from config.database_config import DatabaseConnector
from pelanggan.model.pelangganmodels import Pelanggan
from datetime import datetime, timedelta
import mysql.connector

class PelangganController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_pelanggan(self):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from pelanggan")
            results = cursor.fetchall()
            cursor.close()

            pelanggan_list = []
            for row in results:

                created_at = row['created_at']
                updated_at = row['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at 
                pelanggan = Pelanggan(row['id'], row['nama'], row['alamat'], row['telepon'], created_at, updated_at)
                pelanggan_list.append(pelanggan)

            return pelanggan_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
        
    # melihat dengan json
    def lihat_pelanggan(self):
        all_pelanggan = self.get_all_pelanggan()
        if all_pelanggan is not None:
            pelanggan_data = [pelanggan.to_dict() for pelanggan in all_pelanggan]
            return {'produk': pelanggan_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data pelanggan'}, 500
        
    # pencarian data dari tabel pelanggan
    def cari_pelanggan(self,id):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from pelanggan where id = %s", (id,))
            pelanggan = cursor.fetchone()
            cursor.close()

            if pelanggan:
                created_at = pelanggan['created_at']
                updated_at = pelanggan['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at
                
                pelanggan_obj = Pelanggan(pelanggan['id'], pelanggan['nama'], pelanggan['alamat'], pelanggan['telepon'], created_at, updated_at)
                return {'pelanggan': pelanggan_obj.to_dict()}, 200
            else:
                return {'message': 'Data pelanggan tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data pelanggan'}, 500
        
    # tambah data produk
    def tambah_pelanggan(self,data):
        try:
            nama = data.get('nama')
            alamat = data.get('alamat')
            telepon = data.get('telepon')
            created_at = datetime.now()
            updated_at = datetime.now()

            cursor = self.db.cursor()
            query = 'insert into pelanggan (nama, alamat, telepon, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(query, (nama, alamat, telepon, created_at, updated_at))
            self.db.commit()
            cursor.close()

            return {'message': 'Data pelanggan berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data pelanggan'}, 500
        
    # update data pelanggan
    def update_pelanggan(self, id, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from pelanggan where id = %s"
            cursor.execute(query, (id,))
            pelanggan = cursor.fetchone()
            cursor.close()

            if not pelanggan:
                return {'message': 'Data pelanggan tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update pelanggan SET nama = %s, alamat = %s, telepon = %s, updated_at = NOW() where id = %s"
            cursor.execute(query, (data['nama'], data['alamat'], data['telepon'], id))
            self.db.commit()
            cursor.close()

            return {'message': 'Data pelanggan berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data pelanggan'}, 500
        
    # delete data produk
    def hapus_pelanggan(self, id):
        try:
            cursor = self.db.cursor()
            query = "delete from pelanggan where id = %s"
            cursor.execute(query, (id,))
            self.db.commit()
            affected_rows = cursor.rowcount
            cursor.close()

            if affected_rows > 0:
                return {'message': 'Data pelanggan berhasil dihapus'}, 200
            else:
                return {'message': 'Data pelanggan tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menghapus data pelanggan'}, 500