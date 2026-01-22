import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from core.currency_service import CurrencyService

def test_currencies_seeding():
    print("--- Testing Currencies Seeding ---")
    service = CurrencyService()
    res = service.get_all_currencies()
    
    if not res["success"]:
        print(f"[FAILED] Error fetching currencies: {res.get('error')}")
        sys.exit(1)
        
    currencies = res["currencies"]
    print(f"Found {len(currencies)} currencies.")
    
    for c in currencies:
        print(f"  - {c}")
        
    # Check for expected seeds (Phase 5 plan mentioned COP, USD, EUR)
    expected_codes = ["COP", "USD", "EUR"]
    found_codes = [c.code for c in currencies]
    
    missing = [code for code in expected_codes if code not in found_codes]
    
    if missing:
        print(f"[FAILED] Missing expected currencies: {missing}")
        sys.exit(1)
    else:
        print("[OK] All expected currencies found.")

if __name__ == "__main__":
    test_currencies_seeding()
