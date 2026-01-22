import unittest
import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

def run_suite():
    print("========================================")
    print("RUNNING ALL FINANCAPP TESTS")
    print("========================================")
    
    loader = unittest.TestLoader()
    # We explicitly load the test files we know about to ensure order if needed, 
    # but discover is better for "all".
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    with open("test_report.txt", "w") as f:
        f.write("Running tests...\n")
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n[SUCCESS] All tests passed!")
        sys.exit(0)
    else:
        print("\n[FAILURE] Some tests failed.")
        sys.exit(1)

if __name__ == '__main__':
    run_suite()
