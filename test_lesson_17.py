import unittest
import task_number_17


class TaskTest(unittest.TestCase):
    def test_6_1(self):
        self.assertEqual(task_number_17.task_6_1('Bitcoin', 'BTC'), {'Bitcoin': 'BTC'})

    def test_7_2_C(self):
        self.assertEqual(task_number_17.task_7_2(10, 'C'), (10.0, 283.15, 50.0))

    def test_7_2_F(self):
        self.assertEqual(task_number_17.task_7_2(10, 'F'), (-12.222222222222221, 260.92777777777775, 10.0))

    def test_7_2_K(self):
        self.assertEqual(task_number_17.task_7_2(10, 'K'), (-263.15, 10.0, -441.67))

    def test_11_2(self):
        self.assertEqual(task_number_17.task_11_2(12321), True)

    def test_15_2(self):
        self.assertEqual(task_number_17.task_15_2('063-999-99-99'), '(+38) 063 999-99-99')


if __name__ == "__main__":
    unittest.main()
