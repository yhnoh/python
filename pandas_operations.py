import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from decorator import append
from numpy.f2py.crackfortran import kindselector


class MyTestCase(unittest.TestCase):

    """
    None: 파이썬 객체의 Null 값을 나타냄
    NaN (Not a Number): 부동소수점의 Null 값을 나타냄
    """
    def test_handle_null_dataframe(self):
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

    def test_drop_duplication(self):
        """
        1. subset: Specifies the columns to check for duplicates. If not provided all columns are considered.

        2. keep: Finds which duplicate to keep:
        'first' (default): Keeps the first occurrence, removes subsequent duplicates.
        'last': Keeps the last occurrence and removes previous duplicates.
        False: Removes all occurrences of duplicates.
        3. inplace: If True it modifies the original DataFrame directly. If False (default), returns a new DataFrame.
        """

        df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Alice", "David"],
            "Age": [25, 30, 25, 40],
            "City": ["NY", "LA", "NY", "Chicago"]
        })

        print()
        print("drop_duplicates() 메서드를 통한 중복 제거")
        print(df.drop_duplicates())

        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'David'],
            'Age': [25, 30, 25, 40],
            'City': ['NY', 'LA', 'SF', 'Chicago']
        })

        print()
        print("drop_duplicates() 메서드를 통한 중복 제거 > subset 옵션 사용을 통한 특정 컬럼 중복 제거")
        ## 1개 이상의 컬럼 지정 가능
        print(df.drop_duplicates(subset=['Name']))


        print()
        print("drop_duplicates() 메서드를 통한 중복 제거 > keep 옵션 사용을 중복 제거 방식 지정")
        print(df.drop_duplicates(subset=['Name'], keep="last"))
        ## 중복된 값 모두 제거
        print(df.drop_duplicates(subset=['Name'], keep=False))

    def test_change_datatype(self):

        df = pd.DataFrame({
            'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
            'Age': [25, 30, 22, 35, 28],
            'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
            'Salary': [50000, 55000, 40000, 70000, 48000]
        })


        print(df.dtypes)

        print()
        print("astype() 메서드를 통한 데이터 타입 변환")
        df = df.astype({"Age": float, "Salary": float})
        print(df.dtypes)

    def test_manipulate_string(self):

        df = pd.DataFrame({
            'Names': ['Gulshan', 'Shashank', 'Bablu', 'Abhishek', 'Anand', np.nan, 'Pratap'],
            'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Bangalore', 'Hyderabad']
        })

        print()
        print("DataFrame 원본 타입 확인")
        print(df.dtypes)

        df = df.astype('string')
        print()
        print("DataFrame String 타입 변환")
        print(df.dtypes)

        print("string 타입 메서드 활용")
        print("lower() 메서드를 통한 소문자 변환")
        display(df["Names"].str.lower())

        print()
        print("upper() 메서드를 통한 소문자 변환")
        display(df["Names"].str.upper())


        print()
        print("strip() 메서드를 앞뒤 공백 제거")
        display(df["Names"].str.strip())

        print()
        print("split() 메서드를 문자열 자르기")
        df["Split_Name"] = df["Names"].str.split("a")
        display(df)

        print()
        print("len() 메서드를 이용한 문자열 길이 확인")
        display(df["Names"].str.len())

        print()
        print("cat() 메서드를 이용한 문자열 합치기")
        display(df["Names"].str.cat(sep=","))

        print()
        print("get_dummies() 메서드를 이용한 One-Hot Encoding: 인덱스에 따른 존재여부에 대한 값을 0과 1로 표현")
        display(df["City"].str.get_dummies())

        print()
        print("startswith() 메서드를 문자열 존재 여부 확인")
        display(df["Names"].str.startswith("G"))

        print()
        print("endswith() 메서드를 문자열 존재 여부 확인")
        display(df["Names"].str.endswith("h"))

        print()
        print("replace() 메서드를 이용한 문자열 치환")
        display(df["Names"].str.replace("Gulshan", "Gaurav"))

        print()
        print("repeat() 메서드를 이용한 문자열 반복")
        display(df["Names"].str.repeat(2))

        print()
        print("count() 메서드를 이용한 문자열 패턴 개수 확인")
        display(df["Names"].str.count("a"))

        print()
        print("find() 메서드를 이용한 문자열 패턴 위치 확인")
        display(df["Names"].str.find("a"))

        print()
        print("findall() 메서드를 이용한 전체 문자열 패턴 확인")
        display(df["Names"].str.findall("a"))

        print()
        print("islower() 메서드를 이용한 소문자 여부 확인")
        display(df["Names"].str.islower())

        print()
        print("isupper() 메서드를 이용한 대문자 여부 확인")
        display(df["Names"].str.isupper())

        print()
        print("isnumeric() 메서드를 이용한 숫자 치환 가능 여부 확인")
        display(df["Names"].str.isnumeric())

        print()
        print("swapcase() 메서드를 이용한 대문자 <-> 소문자 변환")
        display(df["Names"].str.swapcase())

    def test_normalization(self):
        df = pd.DataFrame([
            [180000, 110, 18.9, 1400],
            [360000, 905, 23.4, 1800],
            [230000, 230, 14.0, 1300],
            [60000, 450, 13.5, 1500]
        ], columns=['Col A', 'Col B', 'Col C', 'Col D'])

        display(df)
        df.plot(kind='bar')
        plt.show()

        max_scaled = df.copy()


    def test_normalization_maximum_absolute_scaling(self):

        """
        This technique rescales each feature between -1 and 1 by dividing all values by the maximum absolute value in that column.
        This technique is especially useful when your data doesn’t contain negative numbers and
        you want to preserve the data’s sparsity.
        """
        df = pd.DataFrame([
            [180000, 110, 18.9, 1400],
            [360000, 905, 23.4, 1800],
            [230000, 230, 14.0, 1300],
            [60000, 450, 13.5, 1500]
        ], columns=['Col A', 'Col B', 'Col C', 'Col D'])


        for column in df.columns:
            df[column] = df[column] / df[column].abs().max()

        display(df)
        df.plot(kind='bar')
        plt.show()

    def test_normalization_min_max_scaling(self):

        """
        최소값과 최대값의 차이를 이용하여 데이터를 0 ~ 1 사이의 값으로 재조정 하는 방법
        The min-max approach also called normalization rescales the feature to a hard and fast range of [0,1] by subtracting the minimum value of the feature then dividing by the range.
        It works well for models like K-Nearest Neighbors (KNN) which compare distance between data points.

        """
        df = pd.DataFrame([
            [180000, 110, 18.9, 1400],
            [360000, 905, 23.4, 1800],
            [230000, 230, 14.0, 1300],
            [60000, 450, 13.5, 1500]
        ], columns=['Col A', 'Col B', 'Col C', 'Col D'])

        for column in df.columns:
            df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())

        display(df)
        df.plot(kind='bar')
        plt.show()

    def test_normalization_z_score_method(self):
        """

        The z-score method often called standardization changes the values in each column so that they have a mean of 0 and a standard deviation of 1. This technique is best when your data follow a normal distribution or when you want to treat values in terms of how far they are from the average.
        """

        df = pd.DataFrame([
            [180000, 110, 18.9, 1400],
            [360000, 905, 23.4, 1800],
            [230000, 230, 14.0, 1300],
            [60000, 450, 13.5, 1500]
        ], columns=['Col A', 'Col B', 'Col C', 'Col D'])


        for column in df.columns:
            df[column] = (df[column] - df[column].mean()) / df[column].std()

        display(df)

    def test_append_using_dataframe(self):
        """
        https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat
        """
        df = pd.DataFrame()
        df['Name'] = ['Abhijit', 'Smriti', 'Akash', 'Roshni']
        df['Age'] = [20, 19, 20, 14]
        df['Student'] = [False, True, True, False]

        display(df)


        # series = pd.Series(['Mansi', 19, True], index=['Name', 'Age', 'Student'])
        series = pd.Series(['Mansi', 19, True], index=['Name', 'Age', 'Student'])
        display(series)


        display(pd.concat([df, series.to_frame().T], ignore_index=True))
