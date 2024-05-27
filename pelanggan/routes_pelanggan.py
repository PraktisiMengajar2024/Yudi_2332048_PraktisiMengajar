from flask import Blueprint, request, jsonify
from pelanggan.controller.pelanggancontroller import PelangganController

pelanggan_routes = Blueprint('pelanggan_routes',__name__)
pelanggan_controller = PelangganController()

@pelanggan_routes.route('/pelanggan', methods=['GET'])
def lihat_pelanggan():
    if request.method == 'GET':
        return jsonify(pelanggan_controller.lihat_pelanggan())
    
#rute mencari data
@pelanggan_routes.route('/pelanggan/<int:id>', methods=['GET'])
def cari_pelanggan(id):
    if request.method == 'GET':
        return pelanggan_controller.cari_pelanggan(id)

#rute tambah data
@pelanggan_routes.route('/pelanggan', methods=['POST'])
def tambah_pelanggan():
    data = request.json
    return pelanggan_controller.tambah_pelanggan(data)

#rute update data
@pelanggan_routes.route('/pelanggan/<int:id>', methods=['PUT'])
def update_pelanggan(id):
    data = request.json
    return pelanggan_controller.update_pelanggan(id, data)

#rute hapus data
@pelanggan_routes.route('/pelanggan/<int:id>', methods=['DELETE'])
def hapus_pelanggan(id):
    #data = request.json
    return pelanggan_controller.hapus_pelanggan(id)