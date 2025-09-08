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

        ## Selecting Multiple Rows
        display(nba_pd.loc[["Avery Bradley", "Jae Crowder"]])

        ## Selecting Multiple Rows and Indexes
        display(nba_pd.loc[["Avery Bradley", "Jae Crowder"], ["Team", "Number", "Position"]])
        display(nba_pd.loc["Jae Crowder":, ["Team", "Number", "Position"]])

        ## Selecting Rows By Position with iloc

        display(nba_pd.iloc[0])
        display(nba_pd.iloc[[3, 5, 7]])
        display(nba_pd.iloc[0:3])

        ## Selecting Rows and Columns By Position with iloc
        display(nba_pd.iloc[[3, 4], [1, 2]])
        display(nba_pd.iloc[:, [1, 2]])

        ## Other Useful Indexing Methods
        display(nba_pd.head(5))
        display(nba_pd.tail(5))
        display(nba_pd.at["Avery Bradley", "Age"])
        display(nba_pd.query("Age > 25 and College == 'Duke'"))


if __name__ == '__main__':
    unittest.main()
