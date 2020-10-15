Example of creating a new column based on values from other columns (apply): https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o

Code to use regex based on list:

```
import re
import sys

import numpy as np
import pandas as pd

antibiotic_list = [
    'VANCOMYCIN',
    'CEFTRIAXONE',
]

def label_antibiotic(row, antibiotic_list):
    for med in antibiotic_list:
        if bool(re.search('{}'.format(med), row['ANTIBIOTIC MEDICATION'])):
            return True
    return False

df['antibiotic_flag'] = df.apply(lambda row: label_antibiotic(row, antibiotic_list), axis=1)

df.loc[df['antibiotic_flag']].groupby(['CSN']).agg({'ANTIBIOTIC ORDER TIME': np.min})
```

Equivalent of Group By Count(\*) in PostgreSQL
This was a pretty good resource: https://mode.com/blog/group-by-sql-python/

```
df_test = pd.DataFrame({
    'a': ['A', 'A', 'B', 'B', 'B', 'C', 'D', 'E'],
    'npdes_permit_id': ['AK000', 'AK000', 'BD', 'BD', np.nan, 'CD', 'DE', 'EF']
})

df_test
>	a	npdes_permit_id
0	A	AK000
1	A	AK000
2	B	BD
3	B	BD
4	B	NaN
5	C	CD
6	D	DE
7	E	EF

# Note the dropna argument is new in pandas 1.1 https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
df_test.groupby(['a', 'npdes_permit_id'], dropna=False).size().sort_values(ascending=False)

>a  npdes_permit_id
B  BD                 2
A  AK000              2
E  EF                 1
D  DE                 1
C  CD                 1
B  NaN                1
dtype: int64

df_test.groupby(['a'], dropna=False).size().sort_values(ascending=False)

>a
B    3
A    2
E    1
D    1
C    1
dtype: int64
```
