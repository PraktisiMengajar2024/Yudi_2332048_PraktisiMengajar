from config.database_config import DatabaseConnector
from transaksi.model.transaksimodel import Transaksi
from datetime import datetime, timedelta
import mysql.connector

class TransaksiController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_transaksi(self):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from transaksi")
            results = cursor.fetchall()
            cursor.close()

            transaksi_list = []
            for row in results:

                created_at = row['created_at']
                updated_at = row['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at 
                transaksi = Transaksi(row['id_transaksi'], row['id_pelanggan'], row['tanggal'], created_at, updated_at)
                transaksi_list.append(transaksi)

            return transaksi_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
        
    # melihat dengan json
    def lihat_transaksi(self):
        all_transaksi = self.get_all_transaksi()
        if all_transaksi is not None:
            transaksi_data = [transaksi.to_dict() for transaksi in all_transaksi]
            return {'produk': transaksi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data transaksi'}, 500
        
    # pencarian data dari tabel transaksi
    def cari_transaksi(self,id_transaksi):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from transaksi where id_transaksi = %s", (id_transaksi,))
            transaksi = cursor.fetchone()
            cursor.close()

            if transaksi:
                created_at = transaksi['created_at']
                updated_at = transaksi['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at
                
                transaksi_obj = Transaksi(transaksi['id_transaksi'], transaksi['id_pelanggan'], transaksi['tanggal'], created_at, updated_at)
                return {'transaksi': transaksi_obj.to_dict()}, 200
            else:
                return {'message': 'Data transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data transaksi'}, 500
        
    # tambah data transaksi
    def tambah_transaksi(self,data):
        try:
            id_pelanggan = data.get('id_pelanggan')
            tanggal = data.get('tanggal')
            created_at = datetime.now()
            updated_at = datetime.now()

            cursor = self.db.cursor()
            query = 'insert into transaksi (id_pelanggan, tanggal, created_at, updated_at) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (id_pelanggan, tanggal, created_at, updated_at))
            self.db.commit()
            cursor.close()

            return {'message': 'Data transaksi berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data transaksi'}, 500
        
    # update data transaksi
    def update_transaksi(self, id_transaksi, data):
        try:
            if not data:
                return {'message': 'Data yang diterima kosong'}, 400
            
            cursor = self.db.cursor(dictionary=True)
            query = "select * from transaksi where id_transaksi = %s"
            cursor.execute(query, (id_transaksi,))
            transaksi = cursor.fetchone()
            cursor.close()

            if not transaksi:
                return {'message': 'Data transaksi tidak ditemukan'}, 404
            
            cursor = self.db.cursor()
            query = "update transaksi SET id_pelanggan = %s, tanggal = %s, updated_at = NOW() where id_transaksi = %s"
            cursor.execute(query, (data['id_pelanggan'], data['tanggal'], id_transaksi))
            self.db.commit()
            cursor.close()

            return {'message': 'Data transaksi berhasil diperbarui'}, 200
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat memperbarui data transaksi'}, 500