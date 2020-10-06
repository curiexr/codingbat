# List-1

## first_last6
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

## common_end
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

## reverse3
def reverse3(nums):
  return nums[::-1]

## middle_way
def middle_way(a, b):
  return [a[1], b[1]]

## same_first_last
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
    else:
      return False
  else:
    return False

## sum3
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

## max_end3
def max_end3(nums):
  larger = max(nums[2], nums[0])
  nums[0] = larger
  nums[1] = larger
  nums[2] = larger
  return nums

## make_ends
def make_ends(nums):
  a = nums[0]
  b = nums[-1]
  return [a, b]

## make_pi
def make_pi():
  return [3, 1, 4]

## rotate_left3
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

## sum2
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif 2 > len(nums) > 0:
    return nums[0]
  else:
    return 0

## has23
def has23(nums):
  if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False

