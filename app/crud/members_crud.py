from datetime import datetime
from app.models.member_model import Member
from app.database import db

class MemberCRUD:
    def __init__(self):
        pass

    def create(self, data):
        new_member = Member(
            name=data['name'],
            email=data['email'],
            joined_date=datetime.now()
        )
        db.session.add(new_member)
        db.session.commit()
        return new_member

    
    def get_by_id(self, member_id):
        return Member.query.get_or_404(member_id)

    def update(self, member_id, data):
        member = Member.query.get_or_404(member_id)
        if not member:
            raise Exception(f"Member with ID {member_id} not found.")
        

        member.name = data['name']
        member.email = data['email']
        member.joined_date = datetime.now()
        db.session.commit()
        return member

    def delete(self, member_id):
        member = Member.query.get_or_404(member_id)
        db.session.delete(member)
        db.session.commit()