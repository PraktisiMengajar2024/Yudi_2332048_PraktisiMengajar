from config.database_config import DatabaseConnector
from detailtransaksi.model.detailtransaksimodels import DetailTransaksi
from datetime import datetime, timedelta
import mysql.connector

class DetailTransaksiController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_detail_transaksi(self):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from detail_transaksi")
            results = cursor.fetchall()
            cursor.close()

            detailtransaksi_list = []
            for row in results:

                created_at = row['created_at']
                updated_at = row['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at 
                detailtransaksi = DetailTransaksi(row['id'], row['id_transaksi'], row['id_produk'], row['jumlah'], row['harga'], row['total'], row['sub_total'],
                                                  row['metode_pembayaran'], created_at, updated_at)
                detailtransaksi_list.append(detailtransaksi)

            return detailtransaksi_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        
    # melihat dengan json
    def lihat_detail_transaksi(self):
        all_detail_transaksi = self.get_all_detail_transaksi()
        if all_detail_transaksi is not None:
            detail_transaksi_data = [detail_transaksi.to_dict() for detail_transaksi in all_detail_transaksi]
            return {'DetailTransaksi': detail_transaksi_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data detail transaksi'}, 500
        
    # pencarian data dari tabel transaksi
    def cari_detail_transaksi(self,id):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from detail_transaksi where id = %s", (id,))
            detailtransaksi = cursor.fetchone()
            cursor.close()

            if detailtransaksi:
                created_at = detailtransaksi['created_at']
                updated_at = detailtransaksi['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at
                
                detailtransaksi_obj = DetailTransaksi(detailtransaksi['id'], detailtransaksi['id_transaksi'], detailtransaksi['id_produk'], 
                                                      detailtransaksi['jumlah'], detailtransaksi['harga'], detailtransaksi['total'],
                                                      detailtransaksi['sub_total'], detailtransaksi['metode_pembayaran'],
                                                      created_at, updated_at)
                return {'detailtransaksi': detailtransaksi_obj.to_dict()}, 200
            else:
                return {'message': 'Data detail transaksi tidak ditemukan'}, 404
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat mencari data detail transaksi'}, 500
        
    # tambah data transaksi
    def tambah_detail_transaksi(self, data):
        try:
            id_transaksi = data.get('id_transaksi')
            id_produk = data.get('id_produk')
            jumlah = data.get('jumlah')
            metode_pembayaran = data.get('metode_pembayaran')
            created_at = datetime.now()
            updated_at = datetime.now()

            cursor = self.db.cursor()
            query = """
            INSERT INTO detail_transaksi 
            (id_transaksi, id_produk, jumlah, metode_pembayaran, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (id_transaksi, id_produk, jumlah, metode_pembayaran, created_at, updated_at))
            self.db.commit()
            cursor.close()

            return {'message': 'Data detail transaksi berhasil ditambahkan'}, 201
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return {'message': 'Terjadi kesalahan saat menambah data detail transaksi'}, 500