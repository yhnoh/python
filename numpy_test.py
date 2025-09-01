import unittest
import numpy as np

class MyTestCase(unittest.TestCase):

    def test_create_numpy_array(self):
        x = np.array([1, 2, 3])
        y = np.array([
            [1, 2],
            [3, 4],
        ])
        z = np.array([
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ])

        print(x)
        print(y)
        print(z)


    def test_numpy_array_initialization_function(self):
        ## 0으로 초기화된 1차원 numpy 배열 생성
        x_zeros = np.zeros((2))
        ## 0으로 초기화된 2차원 numpy 배열 생성
        y_zeros = np.zeros((2, 3))
        ## 0으로 초기화된 3차원 numpy 배열 생성
        z_zeros = np.zeros((2, 3, 4))

        ## 1로 초기화된 2차원 numpy 배열 생성
        y_ones = np.ones((2, 3))

        ## 0 <= x < 10 사이에서 2씩 증가하는 1차원 배열
        x_arange = np.arange(0, 10, 2)

        print(x_zeros)
        print(y_zeros)
        print(z_zeros)

        print(y_ones)

        print(x_arange)

    def test_numpy_array_indexing(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ])

        print("x에서 하나의 요소 찾기 =", x[2])
        print("x에서 음수를 이용한 인덱싱 =", x[-2])
        print("y에서 하나의 요소 찾기 =", y[1, 1])


    def test_numpy_slicing_indexing(self):

        x = np.array([1, 2, 3, 4, 5])
        y = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ])

        ### Slicing
        ## 인덱스 1 ~ 3 까지의 요소 찾음
        print("x에서 여러 요소 찾기 =", x[1:4])
        ## 0 ~ 1 까지의 행 찾기 : [[1 2 3] [4 5 6]]
        print("y에서 여러 요소 찾기 =", y[0:2])
        ## 0 ~ 1 까지의 행을 찾은 이후, 1 열만 찾기 : [2 5]
        print("y에서 여러 요소 찾기 =", y[:, 1])

    def test_numpy_advenced_indexing(self):

        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        indexes = np.array([1, 3, 5])
        print("여러 인덱스를 통한 요소 찾기 =", arr[indexes])

        condition = arr >= 10
        print("요소의 조건을 통한 요소 찾기 =", arr[condition])

    def test_numpy_operations(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])

        print("addition=", arr1 + arr2)
        print("addition=", np.add(arr1, arr2))
        print("subtraction=", arr1 - arr2)
        print("subtraction=", np.subtract(arr1, arr2))
        print("multiplication=", arr1 * arr2)
        print("multiplication=", np.multiply(arr1, arr2))
        print("division=", arr1 / arr2)
        print("division=", np.divide(arr1, arr2))

        arr3 = np.array([[-1, 1, -2, 2], [-3, 3, -4, 4]])
        print("absolute=", np.absolute(arr3))

    def test_numpy_sorting(self):
        """ numpy 배열 정렬, np.sort() 함수 사용 """
        dtypes = [("name", "U5"), ("age", int), ("score", float)]

        values = [
            ("name1", 18, 3.5),
            ("name2", 19, 2.5),
            ("name3", 20, 4.5)
        ]

        arr = np.array(values, dtype=dtypes)

        print("name을 통한 정렬", np.sort(arr, order=["name"]))
        print("name와 score을 통한 정렬", np.sort(arr, order=["name", "score"]))

        # arr = np.array(["name1", "name2"])
        # print(arr.dtype)


if __name__ == '__main__':
    unittest.main()
