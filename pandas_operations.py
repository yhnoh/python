import unittest
import pandas as pd
import numpy as np
from IPython.display import display

class MyTestCase(unittest.TestCase):

    """
    None: 파이썬 객체의 Null 값을 나타냄
    NaN (Not a Number): 부동소수점의 Null 값을 나타냄
    """
    def test_something(self):
        df = pd.DataFrame({
            'First Score': [100, 90, np.nan, 95],
             'Second Score': [30, 45, 56, np.nan],
             'Third Score': [np.nan, 40, 80, 98]
        })

        print()
        print("isnull() 메서드를 이용한 null 여부 확인")
        print(df.isnull())

        print()
        print("isnull() 메서드를 이용한 필터링")
        ## Second Score가 null인 행만 필터링
        isnull_series = pd.isnull(df["Second Score"])
        display(isnull_series)
        display(df[isnull_series])

        print()
        print("isna() 메서드를 이용한 null 여부 확인")
        display(df.isna())

        print()
        print("notnull() 메서드를 이용한 null 여부 확인")
        display(df.notnull())

        print()
        print("notnull() 메서드를 이용한 필터링")
        ## Second Score가 null이 아닌 행만 필터링
        is_notnull_series = pd.notnull(df["Second Score"])
        display(is_notnull_series)
        display(df[is_notnull_series])

        print()
        print("fillna() 메서드를 통한 null 값 대체")
        display(df.fillna(0))

        print()
        print("ffill() 및 bfill() 메서드를 통한 null 값 대체")
        ## ffill() 메서드를 이용하여 앞의 값으로 채우기
        display(df.ffill())
        ## bfill() 메서드를 이용하여 뒤의 값으로 채우기
        display(df.bfill())

        print()
        print("replace() 메서드를 이용한 특정 값 대체")
        display(df.replace(to_replace=np.nan, value=10))

        df = pd.DataFrame({
            'First Score': [100, 90, np.nan, 95],
            'Second Score': [30, np.nan, 45, 56],
            'Third Score': [52, 40, 80, 98],
            'Fourth Score': [np.nan, np.nan, np.nan, 65]
        })
        print()
        print("dropna() 메서드를 통한 null 값이 포함된 열 제거")
        display(df.dropna())


        df = pd.DataFrame({
            'First Score': [100, np.nan, np.nan, 95],
            'Second Score': [30, np.nan, 45, 56],
            'Third Score': [52, np.nan, 80, 98],
            'Fourth Score': [np.nan, np.nan, np.nan, 65]
        })
        print()
        print("dropna() 메서드를 통한 null 값이 포함된 행 제거 > how 옵션을 사용하여 특정 상황에서만 제거")
        display(df.dropna(how='all'))
        display(df.dropna(how='any'))

        df = pd.DataFrame({
            'First Score': [100, np.nan, np.nan, 95],
            'Second Score': [30, np.nan, 45, 56],
            'Third Score': [52, np.nan, 80, 98],
            'Fourth Score': [60, 67, 68, 65]
        })
        print()
        print("dropna() 메서드를 통한 null 값이 포함된 행 제거 > axis 옵션을 사용하여 null이 포함된 열 제거")
        display(df.dropna(axis='columns'))

