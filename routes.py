from flask import Blueprint, jsonify, request, abort
from app import db
from app.models import Karyawan  # Import Karyawan model

# Create a Blueprint
bp = Blueprint('main', __name__)

# Define routes

# GET all Karyawan
@bp.route('/karyawan', methods=['GET'])
def get_karyawan():
    karyawans = Karyawan.query.all()
    result = []
    for karyawan in karyawans:
        result.append({
            'id': karyawan.id,
            'nama': karyawan.nama,
            'posisi': karyawan.posisi,
            'gaji': karyawan.gaji
        })
    return jsonify(result)

# GET single Karyawan by ID
@bp.route('/karyawan/<int:id>', methods=['GET'])
def get_karyawan_by_id(id):
    karyawan = Karyawan.query.get(id)
    if karyawan is None:
        abort(404, description="Karyawan not found")
    return jsonify({
        'id': karyawan.id,
        'nama': karyawan.nama,
        'posisi': karyawan.posisi,
        'gaji': karyawan.gaji
    })

# POST a new Karyawan
@bp.route('/karyawan', methods=['POST'])
def create_karyawan():
    data = request.get_json()
    if not data or 'nama' not in data or 'posisi' not in data or 'gaji' not in data:
        abort(400, description="Missing required fields")
    
    new_karyawan = Karyawan(
        nama=data['nama'],
        posisi=data['posisi'],
        gaji=data['gaji']
    )
    
    db.session.add(new_karyawan)
    db.session.commit()
    
    return jsonify({
        'id': new_karyawan.id,
        'nama': new_karyawan.nama,
        'posisi': new_karyawan.posisi,
        'gaji': new_karyawan.gaji
    }), 201

# PUT update an existing Karyawan
@bp.route('/karyawan/<int:id>', methods=['PUT'])
def update_karyawan(id):
    karyawan = Karyawan.query.get(id)
    if karyawan is None:
        abort(404, description="Karyawan not found")
    
    data = request.get_json()
    if 'nama' in data:
        karyawan.nama = data['nama']
    if 'posisi' in data:
        karyawan.posisi = data['posisi']
    if 'gaji' in data:
        karyawan.gaji = data['gaji']
    
    db.session.commit()
    
    return jsonify({
        'id': karyawan.id,
        'nama': karyawan.nama,
        'posisi': karyawan.posisi,
        'gaji': karyawan.gaji
    })

# DELETE a Karyawan by ID
@bp.route('/karyawan/<int:id>', methods=['DELETE'])
def delete_karyawan(id):
    karyawan = Karyawan.query.get(id)
    if karyawan is None:
        abort(404, description="Karyawan not found")
    
    db.session.delete(karyawan)
    db.session.commit()
    
    return jsonify({'message': f'Karyawan {id} telah sukses dihapus'}), 200
