from models import db, Complaint

def get_pending_complaints():
    return Complaint.query.filter_by(status='Pending').all()
