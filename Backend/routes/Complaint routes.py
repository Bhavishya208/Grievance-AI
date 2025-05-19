from flask import Blueprint, request, jsonify
from models import db, Complaint

complaint_bp = Blueprint('complaint', __name__)

@complaint_bp.route('/complaints', methods=['POST'])
def create_complaint():
    data = request.get_json()
    new_complaint = Complaint(
        category=data['category'],
        description=data['description'],
        location=data['location'],
        status='Pending'
    )
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify({"message": "Complaint created successfully"}), 201
