from flask import Flask
from config.database_config import DatabaseConnector
from produk.routes_produk import produk_routes
from pelanggan.routes_pelanggan import pelanggan_routes
from transaksi.routes_transaksi import transaksi_routes

app = Flask(__name__)

db_connector = DatabaseConnector()
db_connector.test_connection()

app.register_blueprint(produk_routes)
app.register_blueprint(pelanggan_routes)
app.register_blueprint(transaksi_routes)

if __name__ == '__main__':
    app.run(debug=True)