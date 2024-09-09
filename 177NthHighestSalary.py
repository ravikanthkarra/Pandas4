import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # result = []
    # for i in len(range(employee)):
    #     sal = employee['salary'][i]
    #     if sal not in result:
    #         result.append(sal)
    # result.sort(reverse = True)
    # if N>len(result) or N <=0:
    #     return pd.DataFrame(f'getNthHighestSalary({N})': Null)
    # else:
    #     return return pd.DataFrame(f'getNthHighestSalary({N})': result[0])

    # df1 = employee.sort_values(by = 'salary', ascending = False)
    df1 = employee.drop_duplicates('salary')
    if N > len(df1) or N <= 0:
        return pd.DataFrame([None], columns = [f'getNthHighestSalary({N})'])
    df1['rank'] = df1['salary'].rank(method = 'dense', ascending = False)
    df1 = df1[(df1['rank'] == N)]
    return df1[['salary']].rename(columns = {'salary': f'getNthHighestSalary({N})'})