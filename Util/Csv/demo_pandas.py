import pandas

"""
Reading data with pandas - Data read is being stored in a dataframe

"""

df = pandas.read_csv('hrdata.csv')
print(df)

print(type(df['Hire Date'][0]))

df = pandas.read_csv('hrdata.csv', index_col='Name')
print(df)


df = pandas.read_csv('hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')