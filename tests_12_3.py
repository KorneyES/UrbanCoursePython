import unittest
from suite_12_3 import test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
