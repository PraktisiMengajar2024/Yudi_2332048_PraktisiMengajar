from datetime import datetime

class DetailTransaksi:
    def __init__(self, id, id_transaksi, id_produk, jumlah, harga, total, sub_total, metode_pembayaran, created_at=None, updated_at=None):
        self.id = id
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.jumlah = jumlah
        self.harga = harga
        self.total = total
        self.sub_total = sub_total
        self.metode_pembayaran = metode_pembayaran
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.updated_at = updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at else None

    @staticmethod
    def from_dict(data):

        return DetailTransaksi(
            id=data['id'],
            id_transaksi=data['id_transaksi'],
            id_produk=data['id_produk'],
            jumlah=data['jumlah'],
            harga=data['harga'],
            total=data['total'],
            sub_total=data['sub_total'],
            metode_pembayaran=data['metode_pembayaran'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            updated_at=datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S") if data.get('updated_at') else None
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_transaksi': self.id_transaksi,
            'id_produk': self.id_produk,
            'jumlah': self.jumlah,
            'harga': self.harga,
            'total': self.total,
            'sub_total': self.sub_total,
            'metode_pembayaran': self.metode_pembayaran,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }