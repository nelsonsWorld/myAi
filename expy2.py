##https://www.geeksforgeeks.org/working-with-excel-files-using-pandas/

''' import pandas as pd



file = 'pyExv1.xlsx'
sheet1 = pd.read_excel(file,
                      sheet_name = 1,
                      index_col = 0)

sheet2 = pd.read_excel(file,
                      sheet_name = 0,
                      index_col = 0)

newData = pd.concat([sheet1,sheet2])

print (newData) '''

import pandas as pd

file = 'pyExv1.xlsx'

sheet1 = pd.read_excel(file,
                       sheet_name = 0,
                       index_col = 0)
sheet2 = pd.read_excel(file,
                       sheet_name = 1,
                       index_col = 0)

newData = pd.concat([sheet1, sheet2])

'''
#To view 5 columns from the top and from the bottom of the data frame.
print(newData.head())
print(newData.tail())
'''


#Export the data back to an Excel file using the method to_excel.

newData.to_excel('firstExpo.xlsx')