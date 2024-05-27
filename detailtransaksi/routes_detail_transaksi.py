from flask import Blueprint, request, jsonify
from detailtransaksi.controller.detailtransaksicontroller import DetailTransaksiController

detailtransaksi_routes = Blueprint('detail_transaksi_routes',__name__)
detailtransaksi_controller = DetailTransaksiController()

@detailtransaksi_routes.route('/detail_transaksi', methods=['GET'])
def lihat_detail_transaksi():
    if request.method == 'GET':
        return jsonify(detailtransaksi_controller.lihat_detail_transaksi())
    
#rute mencari data
@detailtransaksi_routes.route('/detail_transaksi/<int:id>', methods=['GET'])
def cari_detail_transaksi(id):
    return detailtransaksi_controller.cari_detail_transaksi(id)

#rute tambah data
@detailtransaksi_routes.route('/detail_transaksi', methods=['POST'])
def tambah_detail_transaksi():
    data = request.json
    return detailtransaksi_controller.tambah_detail_transaksi(data)