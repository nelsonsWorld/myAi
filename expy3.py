'''
import pandas as pd

file = 'pyExv1.xlsx'

sheet1 = pd.read_excel(file,
                       sheet_name = 0,
                       index_col = 0)
sheet2 = pd.read_excel(file,
                       sheet_name = 1,
                       index_col = 0)

newData = pd.concat([sheet1, sheet2])'''

import pandas as pd

file = 'pyExv1.xlsx'

sheet1 = pd.read_excel(file,
                       sheet_name = 0,
                       index_col = 0)
sheet2 = pd.read_excel(file,
                       sheet_name = 1,
                       index_col= 0)

newData = pd.concat([sheet1, sheet2])

print(newData)






