from flask import Blueprint, request, jsonify
from produk.controller.produkcontroller import ProdukController

produk_routes = Blueprint('produk_routes',__name__)
produk_controller = ProdukController()

@produk_routes.route('/produk', methods=['GET'])
def lihat_produk():
    if request.method == 'GET':
        return jsonify(produk_controller.lihat_produk())