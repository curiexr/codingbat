# Warmup-2

## string_times
def string_times(str, n):
  return str * n

## string_splosion
def string_splosion(str):
  finalstring = ''
  for i in range(0, len(str)):
    finalstring += str[:i+1]
  return finalstring

## array_front9
def array_front9(nums):
  for i in range(0, 4):
    if i < len(nums):
      if nums[i] == 9:
        return True
  return False

## front_times
def front_times(str, n):
  return str[:3] * n

## last2
def last2(str):
  count = 0
  laststring = str[-2:]
  for i in range(0, len(str)-2):
    if laststring == str[i:i+2]:
      count += 1
  return count

## array123
def array123(nums):
  i = 0
  if len(nums) < 3:
    return False
  for i in range(0, len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

## string_bits
def string_bits(str):
  finalstring = ''
  for i in range(0, len(str)):
    if i % 2 != 0:
      i += 1
    else:
      finalstring += str[i]
  return finalstring

## array_count9
def array_count9(nums):
  count = 0
  for i in range(0, len(nums)):
    if nums[i] == 9:
      count += 1
  return count

## string_match
def string_match(a, b):
  count = 0
  shorter = min(len(a), len(b))
  for i in range(0, shorter-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

