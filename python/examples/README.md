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

```
df = pd.DataFrame({
    'a': ['A', 'A', 'B', 'C', 'D', 'E'],
    'npdes_permit_id': ['AK000', 'AK000', 'BD', 'CD', 'DE', 'EF']
})

df.groupby(['a', 'npdes_permit_id'])['npdes_permit_id'].count()

a  npdes_permit_id
A  AK000              2
B  BD                 1
C  CD                 1
D  DE                 1
E  EF                 1
Name: npdes_permit_id, dtype: int64
```
