import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from core.database import Database

def test_supabase_connection():
    print("--- Testing Supabase Connection ---")
    
    # Initialize and test
    db_ok = Database.test_connection()
    
    if db_ok:
        print("[OK] Connection to Supabase successful!")
    else:
        print("[FAILED] Connection to Supabase.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        test_supabase_connection()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
