## DataDiff

DataDiff compares Python data structures, and returns a structurally consistent diffed data structure.

## Example Data

Source Diff:


{'a': 10,
 'e': [1, 2, 3],
 'g': {'cc': 20, 'dd': 99},
 'h': {'f': {'bbb': 1200}},
 'i': {'aa': 0,
       'bb': 5,
       'cc': 10,
       'f': {'aaa': 300, 'bbb': 1200, 'ccc': [], 'ddd': {3: 15}}}}


Target Diff:


{'a': 12,
 'c': 15,
 'e': [1, 2, 3, 4, 5],
 'g': {'cc': 10},
 'h': {'f': {'bbb': 900, 'ccc': {'a': 9}}}}

## Example DataDiff

  (source_diff, target_diff) = DataDiff(PY_TEST_1, PY_TEST_2, compare_list_as_value=True)


## Result

```
Source Diff:


{'a': 10,
 'e': [1, 2, 3],
 'g': {'cc': 20, 'dd': 99},
 'h': {'f': {'bbb': 1200}},
 'i': {'aa': 0,
       'bb': 5,
       'cc': 10,
       'f': {'aaa': 300, 'bbb': 1200, 'ccc': [], 'ddd': {3: 15}}}}


Target Diff:


{'a': 12,
 'c': 15,
 'e': [1, 2, 3, 4, 5],
 'g': {'cc': 10},
 'h': {'f': {'bbb': 900, 'ccc': {'a': 9}}}}
```

