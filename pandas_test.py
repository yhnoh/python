import unittest
import numpy as np
import pandas as pd
from IPython.display import display

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
        ## Access low By Index
        print('dataframe loc =\n', set_index.loc['name1'])
        ## 기본 인덱스 복원
        print('dataframe =\n', df)
        print("dataFrame Index=\n", df.reset_index())

    def test_acess_dataframe(self):
        data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
                'Age': [25, 30, 22, 35, 28],
                'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
                'Salary': [50000, 55000, 40000, 70000, 48000]}

        ### Access Values By Column
        df = pd.DataFrame(data)
        df_by_column = df['Name']
        print("df_by_column =\n", df_by_column)

        ### Access Rows By Index
        df_by_iloc = df.iloc[0]
        print("df_by_iloc =\n", df_by_iloc)
        df_by_loc = df.loc[0]
        print("df_by_loc =\n", df_by_loc)

        ### Access Multiple Rows or Columns
        multiple_rows_columns = df.loc[0:2, ['Name', 'Age']]
        print("multiple_rows_columns =\n", multiple_rows_columns)

        ### Access Rows Based on Condition
        rows_based_on_condition = df[df['Age'] > 25]
        print("rows_based_on_condition =\n", rows_based_on_condition)

        ### Access Specific Cells with at and iat or at
        specific_cell = df.at[2, "Salary"]
        print("specific_cell =\n", specific_cell)
        display(df)

        nba_pd = pd.read_csv("./files/nba.csv", index_col="Name")
        display(nba_pd)

        ## Selecting Multiple Columns
        display(nba_pd[["Age", "College", "Salary"]].head(5))

        ## loc 메서드를 활용한 인덱스 라벨로 데이터 찾기
        ## Selecting Multiple Rows
        display(nba_pd.loc[["Avery Bradley", "Jae Crowder"]])

        ## Selecting Multiple Rows and Indexes
        display(nba_pd.loc[["Avery Bradley", "Jae Crowder"], ["Team", "Number", "Position"]])
        display(nba_pd.loc["Jae Crowder":, ["Team", "Number", "Position"]])

        ## iloc 메서드를 활용한 인덱스 위치로 데이터 찾기
        display(nba_pd.iloc[0])
        display(nba_pd.iloc[[3, 5, 7]])
        display(nba_pd.iloc[0:3])
        display(nba_pd.iloc[:, 0:2])
        ## Selecting Rows and Columns By Position with iloc
        display(nba_pd.iloc[[3, 4], [1, 2]])
        display(nba_pd.iloc[:, [1, 2]])

        ## 데이터를 찾기위한 유용한 메서드
        display(nba_pd.head(5))
        display(nba_pd.tail(5))
        display(nba_pd.at["Avery Bradley", "Age"])
        display(nba_pd.query("Age > 25 and College == 'Duke'"))

    def test_select_dataframe_by_condition(self):
        data = {
            'Name': ['A', 'B', 'C', 'D', 'E'],
            'Age': [10, 20, 30, 40, 50],
            'Salary': [1000, 2000, 3000, 4000, 5000],
        }

        df = pd.DataFrame(data)

        ## loc 메서드를 이용한 조건에 맞는 데이터 찾기
        print()
        print("loc 메서드를 이용한 조건에 맞는 데이터 찾기")
        display(
            df.loc[
                    (df["Age"] >= 20) & (df["Salary"] >= 3000) & (df["Name"].str.startswith('D')),
                    ["Name", "Age"]
                ]
        )

        ## Numpy를 이용한 조건에 맞는 데이터 찾기
        print()
        print("Numpy를 이용한 조건에 맞는 데이터 찾기")
        np_where = np.where((df["Age"] >= 20) & (df["Salary"] >= 3000) & (df["Name"].str.startswith('D')))
        print(np_where)
        display(df.loc[np_where])

        print()
        print("query() 메서드를 이용한 조건에 맞는 데이터 찾기")
        display(df.query("Age >= 20 and Salary >= 3000 and Name.str.startswith('D')"))

        print()
        print("eval() 메서드를 이용한 조건에 맞는 데이터 찾기")
        df_eval = df.eval("Age >= 20 and Salary >= 3000 and Name.str.startswith('D')")
        print(df_eval)
        display(df[df_eval])

    def test_concat_dataframe(self):
        """
        Dataframe Concatenate
        두개 이상의 Dataframe을 하나의 Dataframe으로 합치는 기능
        axis를 지정하여 여러 Dataframe을 하나로 합치는 것이 가능
        """

        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

        data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
                 'Age': [17, 14, 12, 52],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])
        df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])

        print()
        print("concat() 메서드를 이용한 DataFrame 합치기")
        display(pd.concat([df1, df2]))


        ## 서로 다른 컬럼 및 동일한 인덱스를 가진 DataFrame 합치기

        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
                 'Mobile No': [97, 91, 58, 76]}

        data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
                 'Age': [22, 32, 12, 52],
                 'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
                 'Salary': [1000, 2000, 3000, 4000]}

        df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])

        df2 = pd.DataFrame(data2, index=[2, 3, 6, 7])

        ## Axis 옵션을 통한 컬럼 나열
        print()
        print("concat() 메서드를 이용한 DataFrame 합치기 > axis 옵션을 사용한 join outer를 통한 컬럼 나열")
        display(pd.concat([df1, df2], axis=1))

        print()
        print("concat() 메서드를 이용한 DataFrame 합치기 > axis 옵션을 사용한 join inner를 통한 컬럼 나열")
        display(pd.concat([df1, df2], axis=1, join="inner"))

        print()
        print("concat() 메서드를 이용한 DataFrame 합치기 > ignore_index 옵션을 사용한 인덱스 재설정")
        display(pd.concat([df1, df2], ignore_index=True))

        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

        data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
                 'Age': [17, 14, 12, 52],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])
        df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])

        print()
        print("concat() 메서드를 이용한 DataFrame 합치기 > keys 옵션을 사용한 MultiIndex 생성")
        display(pd.concat([df1, df2], keys=["x", "y"]))


        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32],
                 'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

        df = pd.DataFrame(data1, index=[0, 1, 2, 3])
        s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')

        print()
        print("concat() 메서드를 이용한 DataFrame과 Series 합치기")
        display(pd.concat([df, s1], axis=1))

    def test_merge_dataframe(self):
        """
        Dataframe Merging
        SQL의 JOIN과 유사한 기능을 제공하며 특정 컬럼을 기준으로 합치는 기능 제공
        """

        data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
                'Age':[27, 24, 22, 32],}
        data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        print()
        print("merge() 메서드를 이용한 DataFrame 합치기 > on 옵션을 통해서 어떤 컬럼을 기준으로 합칠지 지정")
        display(pd.merge(df1, df2, on='key'))

        data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'key1': ['K0', 'K1', 'K0', 'K1'],
                 'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
                'Age':[27, 24, 22, 32],}
        data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'key1': ['K0', 'K0', 'K0', 'K0'],
                 'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        print()
        print("merge() 메서드를 이용한 DataFrame 합치기 > on 옵션을 이용한 MultiKey Merge")
        display(pd.merge(df1, df2, on=['key', 'key1']))


        data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'key1': ['K0', 'K1', 'K0', 'K1'],
                 'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
                'Age':[27, 24, 22, 32],}

        data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
                 'key1': ['K0', 'K0', 'K0', 'K0'],
                 'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
                'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        print()
        print("merge() 메서드를 이용한 DataFrame 합치기 > how 옵션을 이용한 다양한 Join")
        pd.merge(df1, df2, how='left', on=['key', 'key1'])
        pd.merge(df1, df2, how='right', on=['key', 'key1'])
        pd.merge(df1, df2, how='outer', on=['key', 'key1'])
        pd.merge(df1, df2, how='inner', on=['key', 'key1'])

    def test_join_dataframe(self):
        """
        Dataframe Joining
        SQL의 JOIN과 유사한 기능을 제공하며 특정 인덱스를 기준으로 합치는 기능 제공
        """

        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32]}
        data2 = {'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1, index=['K0', 'K1', 'K2', 'K3'])
        df2 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])

        print()
        print("join() 메서드를 이용한 DataFrame 합치기 > 인덱스 기준")
        display(df1.join(df2))

        print()
        print("join() 메서드를 이용한 DataFrame 합치기 > how 옵션을 이용한 다양한 조인 방식")
        display(df1.join(df2, how='inner'))

        data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                 'Age': [27, 24, 22, 32],
                 'Key': ['K0', 'K1', 'K2', 'K3']}

        data2 = {'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
                 'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])

        print()
        print("join() 메서드를 이용한 DataFrame 합치기 > on 옵션을 활용한 인덱스가 아닌열 기준으로 합치기")
        print(df1.join(df2, on="Key"))


        data1 = {'Name': ['Jai', 'Princi', 'Gaurav'],
                 'Age': [27, 24, 22]}
        data2 = {'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
                 'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons']}

        df1 = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))

        multiple_index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                           ('K2', 'Y2'), ('K2', 'Y3')],
                                          names=['key', 'Y'])

        df2 = pd.DataFrame(data2, index=multiple_index)

        print()
        print("join() 메서드를 이용한 DataFrame 합치기 > MultiIndex 합치기")
        print(df1.join(df2))



if __name__ == '__main__':
    unittest.main()
