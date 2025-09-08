import unittest
import numpy as np
import pandas as pd

class MyTestCase(unittest.TestCase):

    def test_create_pandas(self):
        series = pd.Series([1, 2, 3])
        print("series =", series)

        arr = np.array([1, 2, 3])
        series = pd.Series(arr)
        print("series =", series)

        data_frame = pd.DataFrame(['a', 'b', 'c'])
        print('dataFrame =', data_frame)

        arr = np.array(['a', 'b', 'c'])
        data_frame = pd.DataFrame(arr)
        print('dataFrame =', data_frame)


if __name__ == '__main__':
    unittest.main()
