from datetime import datetime

class Produk:
    def __init__(self, id, nama, kategori, harga, stok, created_at=None, updated_at=None):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.updated_at = updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at else None

    @staticmethod
    def from_dict(data):

        return Produk(
            id=data['id'],
            nama=data['nama'],
            kategori=data['kategori'],
            harga=data['harga'],
            stok=data['stok'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            updated_at=datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S") if data.get('updated_at') else None
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'kategori': self.kategori,
            'harga': self.harga,
            'stok': self.stok,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }