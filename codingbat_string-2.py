# String-2

## double_char
def double_char(str):
  result = ''
  for i in range(0, len(str)):
    result += str[i] * 2
  return result

## count_code
def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
      count += 1
  return count

## count_hi
def count_hi(str):
  count = 0
  for i in range(0, len(str)-1):
    if str[i] == 'h' and str[i + 1] == 'i':
      count += 1
  return count

## end_other
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

## cat_dog
def cat_dog(str):
  catcount = str.count('cat')
  dogcount = str.count('dog')
  if catcount == dogcount:
    return True
  else:
    return False

## xyz_there
def xyz_there(str):
  xyzwithoutdot, xyzdot = str.count('xyz'), str.count('.xyz')
  if xyzwithoutdot != xyzdot:
    return True
  else:
    return False
