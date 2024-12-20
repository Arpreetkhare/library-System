from sqlite3 import IntegrityError
from app.crud.members_crud import MemberCRUD
from app.models.member_model import Member

class MemberService:
    def __init__(self):
        self.member_crud = MemberCRUD()

    def create_member(self, data):
        """
        Creates a new member with the given data.
        
        :param data: Member details.
        :return: Created member.
        :raises: Exception on failure.
        """
        existing_member = Member.query.filter(
            (Member.email == data.get('title')) 
            
        ).first()
        if existing_member:
            raise ValueError("member already there! ")
        try:
            return self.member_crud.create(data)
        except Exception as e:
            raise Exception(f"Error creating member: {str(e)}")

    
    def get_member_by_id(self, member_id):
        """
        Fetches a member by their ID.

        :param member_id: Member's unique ID.
        :return: Member details.
        :raises: Exception if not found.
        """
        try:
            return self.member_crud.get_by_id(member_id)
        except Exception as e:
            raise Exception(f"Member not found with ID {member_id}: {str(e)}")

    def update_member(self, member_id, data):
        """
        Updates a member with the provided data.

        :param member_id: Member's ID.
        :param data: Updated member data.
        :return: Updated member.
        :raises: Exception on failure.
        """
        try:
            return self.member_crud.update(member_id, data)
        except IntegrityError as e:
            if "Duplicate entry" in str(e.orig):
                raise Exception(f"Email '{data.get('email')}' is already in use by another member.")
            raise Exception(f"Database integrity error: {str(e)}")

        except Exception as e:
            raise Exception(f"Error updating member with ID {member_id}: {e}")
    def delete_member(self, member_id):
        """
        Deletes a member by their ID.

        :param member_id: Member's ID.
        :return: Success message.
        :raises: Exception on failure.
        """
        try:
            return self.member_crud.delete(member_id)
        except Exception as e:
            raise Exception(f"Error deleting member with ID {member_id}: {str(e)}")
