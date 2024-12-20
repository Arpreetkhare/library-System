from flask import Blueprint, request, jsonify

from app.helpers.member_helpers import member_to_dict
from app.services.member_service import MemberService


members_bp = Blueprint('members', __name__)

# Create a new member
@members_bp.route('/', methods=['POST'])
def create_member():
    data = request.get_json()
    member_service = MemberService()
    member = member_service.create_member(data)
    return jsonify({"message": "Member created successfully!", "member": member_to_dict(member)}), 201


# Get a specific member by ID
@members_bp.route('/<int:id>', methods=['GET'])
def get_member(id):
    member_service = MemberService()
    member = member_service.get_member_by_id(id)
    return jsonify({"message" : member_to_dict(member)})

# Update a member
@members_bp.route('/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    member_service = MemberService()
    member = member_service.update_member(id, data)
    return jsonify({"message": "Member updated successfully!", "member": member_to_dict(member)})

# Delete a member
@members_bp.route('/<int:id>', methods=['DELETE'])
def delete_member(id):
    member_service = MemberService()
    member_service.delete_member(id)
    return jsonify({"message": "Member deleted successfully!"})
