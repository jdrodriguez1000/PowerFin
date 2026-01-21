from datetime import date
from typing import Optional

class UserProfile:
    def __init__(
        self,
        id: str,
        full_name: Optional[str] = None,
        avatar_url: Optional[str] = None,
        website: Optional[str] = None,
        gender: Optional[str] = None,
        birth_date: Optional[str] = None,
        civil_status: Optional[str] = None,
        favorite_color: Optional[str] = None,
        favorite_sport: Optional[str] = None,
        updated_at: Optional[str] = None
    ):
        self.id = id
        self.full_name = full_name
        self.avatar_url = avatar_url
        self.website = website
        self.gender = gender
        self.birth_date = birth_date
        self.civil_status = civil_status
        self.favorite_color = favorite_color
        self.favorite_sport = favorite_sport
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            full_name=data.get("full_name"),
            avatar_url=data.get("avatar_url"),
            website=data.get("website"),
            gender=data.get("gender"),
            birth_date=data.get("birth_date"),
            civil_status=data.get("civil_status"),
            favorite_color=data.get("favorite_color"),
            favorite_sport=data.get("favorite_sport"),
            updated_at=data.get("updated_at")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "avatar_url": self.avatar_url,
            "website": self.website,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "civil_status": self.civil_status,
            "favorite_color": self.favorite_color,
            "favorite_sport": self.favorite_sport
        }
