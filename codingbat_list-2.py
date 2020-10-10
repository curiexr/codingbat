# List-2

## count_evens
def count_evens(nums):
  count = 0
  for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count

## sum13
def sum13(nums):
  i = 0
  sum = 0
  if len(nums) == 0:
    return 0
  while i < len(nums):
    if nums[i] != 13:
      sum += nums[i]
    else:
      i += 1
    i += 1
  return sum

## big_diff
def big_diff(nums):
  return max(nums) - min(nums)

## sum67
def sum67(nums):
  sum = 0
  count = True
  
  for i in range(0, len(nums)):
    if nums[i] == 6:
      count = False
    elif count is False and nums[i] == 7:
      count = True
    elif count is True:
      sum += nums[i]
  return sum

## centered_average
def centered_average(nums):
  totalavg = 0    
  sum = 0
  for i in range(0, len(nums), 1):
    sum += nums[i]
  sum = sum - min(nums) - max(nums)
  totalavg = sum / (len(nums)-2)
  return totalavg

## has22
def has22(nums):
  for i in range (0, len(nums)-1):
    if nums[i:i+2] == [2, 2]:
      return True
  return False

