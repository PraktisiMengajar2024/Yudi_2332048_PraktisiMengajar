from datetime import datetime

class Transaksi:
    def __init__(self, id, id_pelanggan, tanggal, created_at=None, updated_at=None):
        self.id = id
        self.id_pelanggan = id_pelanggan
        self.tanggal = tanggal
        self.created_at = created_at.strftime("%Y-%m-%d %H:%M:%S") if created_at else None
        self.updated_at = updated_at.strftime("%Y-%m-%d %H:%M:%S") if updated_at else None

    @staticmethod
    def from_dict(data):

        return Transaksi(
            id=data['id'],
            id_pelanggan=data['id_pelanggan'],
            tanggal=data['tanggal'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S") if data.get('created_at') else None,
            updated_at=datetime.strptime(data['updated_at'], "%Y-%m-%d %H:%M:%S") if data.get('updated_at') else None
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_pelanggan': self.id_pelanggan,
            'tanggal': self.tanggal,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }