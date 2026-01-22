from core.database import Database
from core.logger import Logger
from models.user_profile import UserProfile

class ProfileService:
    def __init__(self):
        self.db = Database.get_client()

    def get_profile(self, user_id: str):
        """Fetches the user profile from Supabase."""
        try:
            res = self.db.table("profiles").select("*").eq("id", user_id).single().execute()
            if res.data:
                return {"success": True, "profile": UserProfile.from_dict(res.data)}
            return {"success": False, "error": "Profile not found"}
        except Exception as e:
            Logger.error(f"Error fetching profile: {str(e)}")
            return {"success": False, "error": str(e)}

    def update_profile(self, profile: UserProfile):
        """Updates the user profile in Supabase."""
        try:
            data = profile.to_dict()
            # Remove ID from update data as it's the key
            user_id = data.pop("id")
            Logger.info(f"Updating Supabase Profile {user_id} with data: {data}")
            res = self.db.table("profiles").update(data).eq("id", user_id).execute()
            return {"success": True, "data": res.data}
        except Exception as e:
            Logger.error(f"Error updating profile: {str(e)}")
            return {"success": False, "error": str(e)}
