import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from core.i18n import I18n

def test_i18n():
    print("--- Testing I18n Core with Debt Resolution ---")
    
    # 1. Test Spanish (Default)
    I18n.load_language("es")
    print(f"ES - App Title: {I18n.t('app.title')}")
    assert I18n.t('app.title') == "PowerFin"
    
    # 2. Test English
    I18n.set_language("en")
    print(f"EN - Welcome: {I18n.t('app.welcome')}")
    assert I18n.t('app.welcome') == "Welcome to PowerFin"
    
    # 3. Test Fallback (Key in ES but not in EN)
    print(f"EN Fallback Test: {I18n.t('test.fallback')}")
    assert I18n.t('test.fallback') == "Esto es un fallback"
    
    # 4. Test Portuguese
    I18n.set_language("pt")
    print(f"PT - Button Back: {I18n.t('common.buttons.back')}")
    assert I18n.t('common.buttons.back') == "Voltar"
    
    # 5. Test Missing Key in BOTH (Final Fallback)
    print(f"Missing Key Test: {I18n.t('non.existent.key')}")
    assert I18n.t('non.existent.key') == "[non.existent.key]"
    
    print("\n--- All I18n Tests (with Fallback & Absolute Paths) Passed! ---")

if __name__ == "__main__":
    try:
        test_i18n()
    except AssertionError as e:
        print(f"TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR DURING TESTING: {e}")
        sys.exit(1)
