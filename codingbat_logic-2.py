# Logic-2

## make_bricks
def make_bricks(small, big, goal):
  nbig = goal // 5
  if big <= nbig:
    nbig = big
  goal = goal - (nbig * 5)
  if goal <= small:
    return True
  else:
    return False

## no_teen_sum
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  if 13 <= n <= 14 or 17 <= n <= 19:
    return 0
  else:
    return n

## make_chocolate
def make_chocolate(small, big, goal):
  wbig = big * 5 
  if goal >= wbig:
    remaining = goal - wbig
  if goal < wbig:
    remaining = goal % 5
  if small >= remaining:
    return remaining
  return -1

## lone_sum 
def lone_sum(a, b, c):
  sum = 0
  if a not in [b, c]:
    sum += a
  if b not in [a, c]:
    sum += b
  if c not in [a, b]:
    sum += c
  
  return sum

## round_sum
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  if num % 10 < 5:
    return num - num % 10

## lucky_sum
def lucky_sum(a, b, c):
  if 13 not in [a, b, c]:
    return a + b + c
  if 13 == a:
    return 0
  if 13 == b:
    return a
  if 13 == c:
    return a + b

## close_far
def close_far(a, b, c):
  if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
    return True
  if abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2:
    return True
  return False