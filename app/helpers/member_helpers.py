from datetime import datetime


def member_to_dict(member):
    
    return {
        "id": member.id,
        "name": member.name,
        "email": member.email,
        "joined_date": member.joined_date
    }
    