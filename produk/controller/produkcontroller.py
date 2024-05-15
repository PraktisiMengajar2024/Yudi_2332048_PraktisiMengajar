from config.database_config import DatabaseConnector
from produk.model.produkmodels import Produk
from datetime import datetime, timedelta
import mysql.connector

class ProdukController:
    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect_to_database()

    def get_all_produk(self):
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("select * from produk")
            results = cursor.fetchall()
            cursor.close()

            produk_list = []
            for row in results:

                created_at = row['created_at']
                updated_at = row['updated_at']
                if isinstance(created_at, timedelta):
                    created_at = datetime.now() - created_at
                if isinstance(updated_at, timedelta):
                    updated_at = datetime.now() - updated_at 
                produk = Produk(row['id'], row['nama'], row['kategori'], row['harga'], row['stok'], created_at, updated_at)
                produk_list.append(produk)

            return produk_list
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
        
    # melihat dengan json
    def lihat_produk(self):
        all_produk = self.get_all_produk()
        if all_produk is not None:
            produk_data = [produk.to_dict() for produk in all_produk]
            return {'produk': produk_data}, 200
        else:
            return {'message': 'Terjadi kesalahan saat mengambil data produk'}, 500