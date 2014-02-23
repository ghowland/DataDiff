## DataDiff

DataDiff compares Python data structures, and returns a structurally consistent diffed data structure.

This is mostly for my own use at the moment, if you have problems or questions let me know.  I'll be cleaning things up to make it nicer for other people to use with better documentation when I get time.

## Example Data

```
PY_TEST_1 = {
  'a':10,
  'b':10,
  'd':[1,2,3],
  'e':[1,2,3],
  'f':{'aa':0, 'bb':5, 'cc':10},
  'g':{'aa':0, 'bb':5, 'cc':20, 'dd':99},
  'h':{'aa':0, 'bb':5, 'cc':10, 'f':{'aaa':300, 'bbb':1200}},
  'i':{'aa':0, 'bb':5, 'cc':10, 'f':{'aaa':300, 'bbb':1200, 'ccc':[], 'ddd':{3: 15}}},
}

PY_TEST_2 = {
  'a':12,
  'b':10,
  'c':15,
  'd':[1,2,3],
  'e':[1,2,3, 4, 5],
  'f':{'aa':0, 'bb':5, 'cc':10},
  'g':{'aa':0, 'bb':5, 'cc':10},
  'h':{'aa':0, 'bb':5, 'cc':10, 'f':{'aaa':300, 'bbb':900, 'ccc':{'a':9}}},
}
```

## Example Invocation

```
  (source_diff, target_diff) = DataDiff(PY_TEST_1, PY_TEST_2, compare_list_as_value=True)
```

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

