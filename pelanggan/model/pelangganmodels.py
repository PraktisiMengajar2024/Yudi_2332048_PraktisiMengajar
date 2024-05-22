from datetime import datetime

class Pelanggan:
    def __init__(self, id, nama, alamat, telepon, created_at=None, updated_at=None):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.updated_at = updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at else None

    @staticmethod
    def from_dict(data):

        return Pelanggan(
            id=data['id'],
            nama=data['nama'],
            alamat=data['alamat'],
            telepon=data['telepon'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            updated_at=datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S") if data.get('updated_at') else None
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'alamat': self.alamat,
            'telepon': self.telepon,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }