from datetime import date
from typing import Optional

class UserProfile:
    def __init__(
        self,
        id: str,
        full_name: Optional[str] = None,
        currency_code: Optional[str] = None,
        preferred_language: Optional[str] = "es",
        updated_at: Optional[str] = None
    ):
        self.id = id
        self.full_name = full_name
        self.currency_code = currency_code
        self.preferred_language = preferred_language
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            full_name=data.get("full_name"),
            currency_code=data.get("currency_code"),
            preferred_language=data.get("preferred_language"),
            updated_at=data.get("updated_at")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "currency_code": self.currency_code,
            "preferred_language": self.preferred_language
        }
