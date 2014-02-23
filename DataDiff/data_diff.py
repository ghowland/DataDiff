"""
DataDiff

Shows differences in data.  Values or containers of values, does not matter.

Does not duck type iterators, only works with lists/tuples/dicts and regular values.
"""


__author__ = 'Geoff Howland <geoff@gmail.com>'


# JSON DIFF DATA.  Show what exists and what doesnt in each...  Then printy print all of it.
#
# Show side-by-side pretty printed data for these fields, as a popup layer, so they can be compared easily.
# Can also mark which lines are different in bold/colors, etc...  Should be good enough
#
# Run JS Lint from the Browser, since it can just run JS.  Apparently Douglas Crawford's version is what everyone is using...
#
# Pass down the data raw so it can be tested.  Otherwise any formatting could break things...
#

import json
import pprint


# JSON test data to compare
JSON_TEST_1 = '''
{"width":8,"height":18,"target123":[50000,175000,250000],"goalType":"mine","resourceType":"time","resourceAmount":150,"fallProbabilities":[0.16666666,0.16666666,0.16666666,0.16666666,0.16666666,0.16666666],"specialProbabilities":[0.0,0.0,0.0,0.0,0.0,0.0],"colorCount":[0,0,0,0,0,0],"nodes":[{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{"gem":{"gemTypeIndex":11}},{},{},{},{},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{},{},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}}],"groups":[],"portals":[],"goalAmount":10,"maxMatches":5,"minMatches":5,"doomTimeAmount":30,"doomMovesAmount":10,"plusTimeAmount":5,"plusMovesAmount":5,"maxNDeadweights":100,"maxNDoomTime":100,"maxNDoomMoves":100,"maxNMorphs":100,"maxNPlus":100,"chocolateType":0,"chocolateAmount":0}
'''
JSON_TEST_2 = '''
{"width":8,"height":18,"target123":[50000,175000,250000],"goalType":"mine","resourceType":"time","resourceAmount":120,"fallProbabilities":[0.16666666,0.16666666,0.16666666,0.16666666,0.16666666,0.16666666],"specialProbabilities":[0.0,0.0,0.0,0.0,0.0,0.0],"colorCount":[0,0,0,0,0,0],"nodes":[{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":9}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{"gem":{"gemTypeIndex":12}},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{"gem":{"gemTypeIndex":11}},{},{},{},{},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{},{},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{},{},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"locked":3,"specialTileType":3},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}},{"gem":{"gemTypeIndex":11}}],"groups":[],"portals":[],"goalAmount":10,"maxMatches":5,"minMatches":5,"doomTimeAmount":30,"doomMovesAmount":10,"plusTimeAmount":5,"plusMovesAmount":5,"maxNDeadweights":100,"maxNDoomTime":100,"maxNDoomMoves":100,"maxNMorphs":100,"maxNPlus":100,"chocolateType":0,"chocolateAmount":0}
'''

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


def _CompareDictValue(key, source, target, source_diff, target_diff, compare_list_as_value, no_difference_value, depth):
  """Making this a function, since source/target are same code with reversed args"""
  # If the target doesnt have this key, the whole value goes into the source_diff
  if key not in target:
    source_diff[key] = source[key]

  # Else, the target has the value, so compare
  else:
    # If this value and the target corresponding value are both Diffable Data types
    if type(source[key]) in (list, tuple, dict) and type(target[key]) in (list, tuple, dict):
      #print('Values:  %s %s %s %s' % (source[key], target[key], compare_list_as_value, depth))
      (child_diff_source, child_diff_target) = DataDiff(source[key], target[key], 
            compare_list_as_value=compare_list_as_value, 
            no_difference_value=no_difference_value, depth=depth+1)
      # Save the difference, as long as it was different (empty containers will be returned if the same)
      if child_diff_source != child_diff_target:
        source_diff[key] = child_diff_source
        target_diff[key] = child_diff_target

    # If the values are the same, do nothing
    #NOTE(geoff): Normally Id put this last as the "else" clause, but here it's in the middle
    #   because there are more than one ways the data is different, and else will catch them all
    elif source[key] == target[key]:
      pass

    # Else, they both different (value or not-diffable-type, doenst matter)
    else:
      source_diff[key] = source[key]
      target_diff[key] = target[key]


def DataDiff(source, target, compare_list_as_value=True, depth=0, no_difference_value=None):
  """Returns tuple (source_diff, target_diff), where the containers match source/target and 
  any data differences are returned as the unique elements to source or target.

  Takes lists or dicts as primary data containers, to facilitate comparing JSON/YAML.
  Tuples are returned as lists.

  In the case that non-containers are passed in and they are the same (no_difference_data, no_difference_data) is returned
  """
  # Ensure recursion doesnt go out of control
  if depth > 150:
    raise Exception('DataDiff recurlsion depth has hit limit (50), aborting.')

  # If we are not working with 2 different containers we can inspect, then do a simple check
  if type(source) not in (list, tuple, dict) or type(target) not in (list, tuple, dict):
    # If the types are different, the data is different (and cant be compared more)
    if type(source) != type(target):
      return (source, target)
    # Else, theyre the same types, if the values are different
    elif source != target:
      return (source, target)
    # Else, theyre the same types and value
    else:
      # This should only happen if this is a fresh DataDiff() call, depth==0
      if depth == 0:
        return (no_difference_value, no_difference_value)
      else:
        raise Exception('This should never happen, having a mismatching value different in anywhere but depth=0')


  if type(source) in (list, tuple):
    source_diff = []
  elif type(source) == dict:
    source_diff = {}
  else:
    raise Exception('Unhandled source_diff data type: %s' % type(source))

  if type(target) in (list, tuple):
    target_diff = []
  elif type(target) == dict:
    target_diff = {}
  else:
    raise Exception('Unhandled target_diff data type: %s' % type(target))

  # Check for incompatible types, and just return them both as theyre totally different
  if type(source_diff) != type(target_diff):
    return (source, target)

  # If we're handling a Dictionary compare
  if type(source_diff) == dict:
    # Process the source keys first
    for key in source.keys():
      _CompareDictValue(key, source, target, source_diff, target_diff, compare_list_as_value, no_difference_value, depth)

    # Process the target keys next, skipping any source keys we already processed
    for key in target.keys():
      # Skip any keys we already processed in source
      if key in source:
        continue

      # Reverse target/source, so that the reverse comparison/set is done
      _CompareDictValue(key, target, source, target_diff, source_diff, compare_list_as_value, no_difference_value, depth)

  # Else, if we're handling a List compare
  elif type(source_diff) == list:
    # If lists must be compared in total because the order of a list is important
    if compare_list_as_value:
      if source != target:
        return (list(source), list(target))

    # Else, compare each element of the list
    else:
      for count in range(0, len(source)):
        if count >= len(target):
          source_diff.append(source[count])
        elif source[count] != target[count]:
          source_diff.append(source[count])
          target_diff.append(target[count])

      # If the target has more elements than the source, add the rest 
      if len(target) > len(source):
        target_diff += target[-(len(source) - len(target)):]

  else:
    raise Exception('Unspecified type handler for data: %s.  Only dict and list/tuple types are accepted.')

  return (source_diff, target_diff)



def Test():
  JSON_TEST_LOADED_1 = json.loads(JSON_TEST_1)
  JSON_TEST_LOADED_2 = json.loads(JSON_TEST_2)

  (source_diff, target_diff) = DataDiff(PY_TEST_1, PY_TEST_2, compare_list_as_value=True)
  # (source_diff, target_diff) = DataDiff(JSON_TEST_LOADED_1, JSON_TEST_LOADED_2, compare_list_as_value=True)
  # (source_diff, target_diff) = DataDiff('badfasd', {'a':5}, compare_list_as_value=True)
  # (source_diff, target_diff) = DataDiff([9], {'a':5}, compare_list_as_value=True)

  print('Source Diff:\n\n')
  pprint.pprint(source_diff)

  print('\n\nTarget Diff:\n\n')
  pprint.pprint(target_diff)


if __name__ == '__main__':
  Test()

