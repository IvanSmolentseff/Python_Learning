''' Test module'''

import unittest
from scripts_module import *


class TestFunctions(unittest.TestCase):
    '''
    tests
    '''

    def testtwomaxsum(self):
        '''
        test equal
        :return: result
        '''
        self.assertEqual(two_max_sum(15, 7, 10), 25)

    def testtwomaxsum2(self):
        '''
        test not equal
        :return: result
        '''
        self.assertNotEqual(two_max_sum(15, 7, 10), 20)

    def testintfunc(self):
        '''
        test equal
        :return: result
        '''
        self.assertEqual(int_func('expecto patronum'), 'Expecto Patronum')

    def testmyfunc(self):
        '''
        test equal
        :return: result
        '''
        self.assertEqual(my_func([2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]),
                         [23, 1, 3, 10, 4, 11])

    def testexcemption(self):
        '''
        test exception
        :return: result
        '''
        self.failureException(dbz_test_1(5, 0), 'Cannot divide by zero')

    def testraises_1(self):
        '''
        test raises
        :return: result
        '''
        self.assertRaises(DivisionByZero, dbz_test_1, 5, 0)
        # не проходит тест, потому что исключение было перехвачено

    def testraises_2(self):
        '''
        test raises
        :return: result
        '''
        self.assertRaises(DivisionByZero, dbz_test_2, 5, 0)
        # тест проходит, исключение не перехвачено и объявлено

    def testmyfunccount1(self):
        '''
        test in
        :return: result
        '''
        self.assertIn(4, my_func_count(2, 7))

    def testmyfunccount2(self):
        '''
        test not in
        :return: result
        '''
        self.assertNotIn(8, my_func_count(2, 7))

    def testclassobjects1(self):
        '''
        test is not
        :return: result
        '''
        self.assertIsNot(Cell(2), Cell(2))

    def testclassobjects2(self):
        '''
        test greater equal
        :return: result
        '''
        self.assertGreaterEqual(Cell(2).quantity, Cell(2).quantity)

    def testclassobjects3(self):
        '''
        test is instance
        :return: result
        '''
        self.assertIsInstance(Cell(9), Cell)


if __name__ == '__main__':
    unittest.main()
