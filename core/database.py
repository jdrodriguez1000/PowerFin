import os
from supabase import create_client, Client
from dotenv import load_dotenv
from core.logger import Logger

# Load environment variables from .env
load_dotenv()

class Database:
    _instance = None
    client: Client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        Logger.info("Initializing Supabase connection...")
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        
        if self.url and self.key:
            try:
                self.client = create_client(self.url, self.key)
                Logger.info("Supabase client created successfully.")
            except Exception as e:
                Logger.error(f"Failed to create Supabase client: {str(e)}")
        else:
            Logger.warning("Supabase URL or Key missing. Database connection not established.")

    @classmethod
    def get_client(cls) -> Client:
        return cls().client

    @classmethod
    def test_connection(cls):
        """Simple health check to verify the connection is active."""
        client = cls.get_client()
        if client:
            try:
                # Instead of checking a table, we can check the auth object or a simple select
                # Note: 'auth' doesn't usually make a network call until needed.
                # Let's try to fetch an empty list from a non-existent table and handle the error.
                # If we get a 404 from Postgrest, it means we REACHED Supabase.
                client.from_("_healthcheck").select("*").limit(1).execute()
                return True
            except Exception as e:
                # If we get a response that looks like it came from Supabase (404, 401, etc.)
                # and not a network timeout or DNS error, we are in good shape.
                err_str = str(e).lower()
                # Case 1: Table not found (means we reached the DB)
                # PGRST205: Could not find the table in the schema cache
                if "relation" in err_str or "not found" in err_str or "pgrst205" in err_str:
                    return True
                # Case 2: Invalid API Key (shouldn't happen with correct keys)
                if "invalid api key" in err_str:
                    Logger.error("Supabase API Key is invalid.")
                    return False
                
                Logger.error(f"Supabase connection test failed: {str(e)}")
        return False
