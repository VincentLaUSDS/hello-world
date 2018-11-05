Flatten Column names returned by groupby: https://stackoverflow.com/questions/14507794/python-pandas-how-to-flatten-a-hierarchical-index-in-columns

See Pandas to SQL Comparison: https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html

Ideas to Add:
1. Array Agg (for postgres)
```
seq_data = admissions_merged_grouped.groupby('SUBJECT_ID')['icd9_feature_id'].apply(list)
```

# Example of Slicing Hierarchical Row Indices
events_grouped.loc[(slice(None), slice(None), ['DIAG']), :]


