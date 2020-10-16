
Codingbat.com Python Solutions. These are my own solutions, not necessarily the best or the fastest. It may serve a purpose for someone looking for alternative solutions. Good luck :)

# Warmup-1

## sleep_in
```
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False
```
## diff21
```
def diff21(n):
  if n <= 21:
    return abs(n - 21)
  if n >= 21:
    return abs(n - 21) * 2
```
## near_hundred
```
def near_hundred(n):
  while 90 <= n <= 110 or 190 <= n <= 210:
    return True
  else:
    return False
```
## missing_char
```
def missing_char(str, n):
  beginning = str[:n]
  end = str[(n+1):]
  return beginning + end
```
## monkey_trouble
```
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  if a_smile == False and b_smile == False:
    return True
  else:
    return False
```
## parrot_trouble
```
def parrot_trouble(talking, hour):
  if talking == True and hour not in range (7, 21):
    return True
  else:
    return False
```
## pos_neg
```
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return a * b < 0
```
## front_back
```
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1:] + str[1:-1] + str[:1]
```
## sum_double
```
def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return (a + b)
```
## makes10
```
def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False
```
## not_string
```
def not_string(str):
  if str[0:3] != 'not':
    return 'not ' + str
  else:
    return str
```
## front3
```
def front3(str):
  if len(str) >= 3:
    return str[0:3] * 3
  else: 
    return str * 3
```
# Warmup-2

## string_times
```
def string_times(str, n):
  return str * n
```
## string_splosion
```
def string_splosion(str):
  finalstring = ''
  for i in range(0, len(str)):
    finalstring += str[:i+1]
  return finalstring
```
## array_front9
```
def array_front9(nums):
  for i in range(0, 4):
    if i < len(nums):
      if nums[i] == 9:
        return True
  return False
```
## front_times
```
def front_times(str, n):
  return str[:3] * n
```
## last2
```
def last2(str):
  count = 0
  laststring = str[-2:]
  for i in range(0, len(str)-2):
    if laststring == str[i:i+2]:
      count += 1
  return count
```
## array123
```
def array123(nums):
  i = 0
  if len(nums) < 3:
    return False
  for i in range(0, len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
```
## string_bits
```
def string_bits(str):
  finalstring = ''
  for i in range(0, len(str)):
    if i % 2 != 0:
      i += 1
    else:
      finalstring += str[i]
  return finalstring
```
## array_count9
```
def array_count9(nums):
  count = 0
  for i in range(0, len(nums)):
    if nums[i] == 9:
      count += 1
  return count
```
## string_match
```
def string_match(a, b):
  count = 0
  shorter = min(len(a), len(b))
  for i in range(0, shorter-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
```
# String-1

## hello_name
```
def hello_name(name):
  name = 'Hello ' + name + '!'
  return name
```
## make_out_word
```
def make_out_word(out, word):
  return out[:2] + word + out[2:]
```
## first_half
```
def first_half(str):
  return str[:len(str)/2]
```
## non_start
```
def non_start(a, b):
  return a[1:] + b[1:]
```
## make_abba
```
def make_abba(a, b):
  return a + b + b + a
```
## extra_end
```
def extra_end(str):
  return 3 * str[-2:]
```
## without_end
```
def without_end(str):
  return str[1:-1]
```
## left2
```
def left2(str):
  return str[2:] + str[:2]
```
## make_tags
```
def make_tags(tag, word):
  starttag = '<' + tag + '>'
  endtag = '</' + tag + '>'
  finalword = starttag + word + endtag
  return finalword
```
## first_two
```
def first_two(str):
  return str[:2]
```
## combo_string
```
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a
```
# String-2

## double_char
```
def double_char(str):
  result = ''
  for i in range(0, len(str)):
    result += str[i] * 2
  return result
```
## count_code
```
def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
      count += 1
  return count
```
## count_hi
```
def count_hi(str):
  count = 0
  for i in range(0, len(str)-1):
    if str[i] == 'h' and str[i + 1] == 'i':
      count += 1
  return count
```
## end_other
```
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) > len(b):
    if a.endswith(b):
      return True
    else:
      return False
  if len(a) < len(b):
    if b.endswith(a):
      return True
    else:
      return False
  if len(a) == len(b):
    if a == b:
      return True
    else:
      return False
```
## cat_dog
```
def cat_dog(str):
  catcount = str.count('cat')
  dogcount = str.count('dog')
  if catcount == dogcount:
    return True
  else:
    return False
```
## xyz_there
```
def xyz_there(str):
  xyzwithoutdot, xyzdot = str.count('xyz'), str.count('.xyz')
  if xyzwithoutdot != xyzdot:
    return True
  else:
    return False
```
# List-1

## first_last6
```
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False
```
## common_end
```
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False
```
## reverse3
```
def reverse3(nums):
  return nums[::-1]
```
## middle_way
```
def middle_way(a, b):
  return [a[1], b[1]]
```
## same_first_last
```
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
    else:
      return False
  else:
    return False
```
## sum3
```
def sum3(nums):
  return nums[0] + nums[1] + nums[2]
```
## max_end3
```
def max_end3(nums):
  larger = max(nums[2], nums[0])
  nums[0] = larger
  nums[1] = larger
  nums[2] = larger
  return nums
```
## make_ends
```
def make_ends(nums):
  a = nums[0]
  b = nums[-1]
  return [a, b]
```
## make_pi
```
def make_pi():
  return [3, 1, 4]
```
## rotate_left3
```
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]
```
## sum2
```
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif 2 > len(nums) > 0:
    return nums[0]
  else:
    return 0
```
## has23
```
def has23(nums):
  if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False
```
# List-2

## count_evens
```
def count_evens(nums):
  count = 0
  for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count
```
## sum13
```
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
```
## big_diff
```
def big_diff(nums):
  return max(nums) - min(nums)
```
## sum67
```
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
```
## centered_average
```
def centered_average(nums):
  totalavg = 0    
  sum = 0
  for i in range(0, len(nums), 1):
    sum += nums[i]
  sum = sum - min(nums) - max(nums)
  totalavg = sum / (len(nums)-2)
  return totalavg
```
## has22
```
def has22(nums):
  for i in range (0, len(nums)-1):
    if nums[i:i+2] == [2, 2]:
      return True
  return False
```
# Logic-1

## cigar_party
```
def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60 and is_weekend is False:
    return True
  elif cigars >= 40 and is_weekend is True:
    return True
  else:
    return False
```
## caught_speeding
```
def caught_speeding(speed, is_birthday):
  if is_birthday is False:
    speed = speed
  if is_birthday is True:
    speed = speed - 5
  if speed <= 60:
    return 0
  if speed  >=61 and speed <= 80:
    return 1
  if speed >= 81:
    return 2
```
## love6
```
def love6(a, b):
  if a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6:
    return True
  else:
    return False
```
## date_fashion
```
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1
```
## sorta_sum
```
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  else:
    return a + b
```
## in1to10
```
def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return 1 <= n <= 10
```
## squirrel_play
```
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  else:
    return 60 <= temp <= 90
```
## alarm_clock
```
def alarm_clock(day, vacation):
  if vacation:
    if 1 <= day <= 5:
      return '10:00'
    if day == 0 or day == 6:
      return 'off'
  else:
    if 1 <= day <= 5:
      return '7:00'
    if day == 0 or day == 6:
      return '10:00'
```
## near_ten
```
def near_ten(num):
  x = num % 10
  if 10 - x <= 2 or x <= 2:
    return True
  else:
    return False
```