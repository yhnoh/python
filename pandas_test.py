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

    def test_create_dataframe(self):
        arr = np.array([
            ['name1', 10, 160, 'M'],
            ['name2', 12, 170, 'F'],
            ['name3', 15, 180, 'M']
        ])

        df = pd.DataFrame(arr, columns=['name', 'age', 'height', 'sex'])
        print('dataFrame =\n', df)

        dict = {
            'name': ['name1', 'name2', 'name3'],
            'age': [10, 12, 15],
            'height': [160, 170, 180],
            'sex': ['M', 'F', 'M']
        }

        df = pd.DataFrame(dict)
        print('dataFrame =\n', df)

    def test_index_dataframe(self):
        """
        """
        dict = {
            'name': ['name1', 'name2', 'name3'],
            'age': [10, 12, 15],
            'height': [160, 170, 180],
            'sex': ['M', 'F', 'M']
        }

        df = pd.DataFrame(dict)
        print("dataFrame =\n", df)
        print("dataFrame Index=\n",df.index)

        """
        인덱스 지정, 컬럼을 기반으로 인덱스 지정 가능
        """
        # df = df.set_index('name')
        ## 인덱스 지정, 컬럼을 기반으로 인덱스 지정 가능
        set_index = df.set_index('name')
        print("dataFrame Index=\n", set_index)
        print('dataframe loc =\n', set_index.loc['name1'])
        ## 기본 인덱스 복원
        print('dataframe =\n', df)
        print("dataFrame Index=\n", df.reset_index())


if __name__ == '__main__':
    unittest.main()
