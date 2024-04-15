c#https://www.geeksforgeeks.org/working-with-excel-files-using-pandas/
#https://stackoverflow.com/questions/63950775/how-can-i-insert-an-excel-formula-using-pandas-when-i-save-it-as-an-excel-file
#https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-fromi
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
print(newData.head())
#To view 5 columns from the top and from the bottom of the data frame.
print(newData.tail())
'''


#Export the data back to an Excel file using the method to_excel.

newData.to_excel('firstExpo.xlsx')