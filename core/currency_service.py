from core.database import Database
from core.logger import Logger

class Currency:
    def __init__(self, code: str, name: str, region: str, symbol: str):
        self.code = code
        self.name = name
        self.region = region
        self.symbol = symbol

    def __str__(self):
        return f"{self.code} - {self.name}"

class CurrencyService:
    def __init__(self):
        self.db = Database.get_client()

    def get_all_currencies(self):
        """Fetches the master list of currencies."""
        try:
            res = self.db.table("currencies").select("*").execute()
            currencies = [Currency(**item) for item in res.data]
            return {"success": True, "currencies": currencies}
        except Exception as e:
            Logger.error(f"Error fetching currencies: {str(e)}")
            return {"success": False, "error": str(e)}
