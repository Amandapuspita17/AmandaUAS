from flask import Blueprint, jsonify, request
from app import db
from app.models import Karyawan

# Membuat blueprint untuk rute-rute API
bp = Blueprint('main', __name__)

# Endpoint untuk mendapatkan semua karyawan (GET)
@bp.route('/karyawan', methods=['GET'])
def get_karyawan():
    karyawans = Karyawan.query.all()
    return jsonify([karyawan.to_dict() for karyawan in karyawans])

# Endpoint untuk mendapatkan karyawan berdasarkan ID (GET)
@bp.route('/karyawan/<int:id>', methods=['GET'])
def get_karyawan_by_id(id):
    karyawan = Karyawan.query.get(id)
    if karyawan:
        return jsonify(karyawan.to_dict())
    return jsonify({'message': 'Karyawan not found'}), 404

# Endpoint untuk menambah karyawan baru (POST)
@bp.route('/karyawan', methods=['POST'])
def create_karyawan():
    data = request.get_json()
    new_karyawan = Karyawan(
        nama=data['nama'],
        posisi=data['posisi'],
        gaji=data['gaji']
    )
    db.session.add(new_karyawan)
    db.session.commit()
    return jsonify(new_karyawan.to_dict()), 201

# Endpoint untuk memperbarui data karyawan (PUT)
@bp.route('/karyawan/<int:id>', methods=['PUT'])
def update_karyawan(id):
    data = request.get_json()
    karyawan = Karyawan.query.get(id)
    if karyawan:
        karyawan.nama = data['nama']
        karyawan.posisi = data['posisi']
        karyawan.gaji = data['gaji']
        db.session.commit()
        return jsonify(karyawan.to_dict())
    return jsonify({'message': 'Karyawan not found'}), 404

# Endpoint untuk menghapus karyawan (DELETE)
@bp.route('/karyawan/<int:id>', methods=['DELETE'])
def delete_karyawan(id):
    karyawan = Karyawan.query.get(id)
    if karyawan:
        db.session.delete(karyawan)
        db.session.commit()
        return jsonify({'message': 'Karyawan deleted'})
    return jsonify({'message': 'Karyawan not found'}), 404
