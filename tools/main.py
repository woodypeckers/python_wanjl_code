#!/user/bin/env python
#coding=utf-8
#__auth__=="__wanjl__"


import unittest
from testcases.bugfree_login import  TestLogin


def main():
    suits=unittest.TestSuite()
    loader=unittest.TestLoader()
    suits.addTests(loader.loadTestsFromTestCase(TestLogin))
    unittest.TextTestRunner(verbosity=2).run(suits)



if __name__ == "__main__":
    main()



