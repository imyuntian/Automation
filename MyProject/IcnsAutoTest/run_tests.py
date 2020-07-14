import unittest
import HTMLTestRunner
import os
import sys
# sys.path.append('./api')

print(os.path.dirname(__file__))
base_dir = os.path.dirname(__file__)
login_case_dir = base_dir + "\\api\\login"
print(os.path.abspath(__file__))
discover = unittest.defaultTestLoader.discover(login_case_dir, pattern='*_test.py')

if __name__  == "__main__":
    # pass
    # runner = HTMLTestRunner()
    runner = unittest.TextTestRunner()
    runner.run(discover)
