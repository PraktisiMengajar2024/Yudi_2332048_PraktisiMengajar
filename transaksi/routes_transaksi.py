from flask import Blueprint, request, jsonify
from transaksi.controller.transaksicontroller import TransaksiController

transaksi_routes = Blueprint('transaksi_routes',__name__)
transaksi_controller = TransaksiController()

@transaksi_routes.route('/transaksi', methods=['GET'])
def lihat_transaksi():
    if request.method == 'GET':
        return jsonify(transaksi_controller.lihat_transaksi())
    
#rute mencari data
@transaksi_routes.route('/transaksi/<int:id>', methods=['GET'])
def cari_transaksi(id):
    return transaksi_controller.cari_transaksi(id)

#rute tambah data
@transaksi_routes.route('/transaksi', methods=['POST'])
def tambah_transaksi():
    data = request.json
    return transaksi_controller.tambah_transaksi(data)

#rute update data
@transaksi_routes.route('/transaksi/<int:id>', methods=['PUT'])
def update_transaksi(id):
    data = request.json
    return transaksi_controller.update_transaksi(id, data)