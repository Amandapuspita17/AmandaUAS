from app import db

class Karyawan(db.Model):
    __tablename__ = 'karyawan'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    posisi = db.Column(db.String(50), nullable=False)
    gaji = db.Column(db.Integer, nullable=False)
