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
