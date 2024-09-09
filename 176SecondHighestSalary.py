import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df1 = employee.drop_duplicates(['salary'])
    if len(df1) < 2:
        return pd.DataFrame([None],columns = ['SecondHighestSalary'])

    df1 = df1.sort_values(['salary'], ascending = False)
    # print(df1)
    df1 = df1.sort_values(['salary'], ascending = False).head(2).tail(1)
    return df1[['salary']].rename(columns = {'salary':'SecondHighestSalary'})