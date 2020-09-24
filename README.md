# codingbat
Codingbat.com Python Solutions

# Warmup-1

#sleep_in
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

#diff21
def diff21(n):
  if n <= 21:
    return abs(n - 21)
  if n >= 21:
    return abs(n - 21) * 2

#near_hundred
def near_hundred(n):
  while 90 <= n <= 110 or 190 <= n <= 210:
    return True
  else:
    return False

#missing_char
def missing_char(str, n):
  beginning = str[:n]
  end = str[(n+1):]
  return beginning + end

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  if a_smile == False and b_smile == False:
    return True
  else:
    return False

#parrot_trouble
def parrot_trouble(talking, hour):
  if talking == True and hour not in range (7, 21):
    return True
  else:
    return False

#pos_neg
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return a * b < 0

#front_back
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1:] + str[1:-1] + str[:1]

#sum_double
def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return (a + b)

#makes10
def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False

#not_string
def not_string(str):
  if str[0:3] != 'not':
    return 'not ' + str
  else:
    return str

#front3
def front3(str):
  if len(str) >= 3:
    return str[0:3] * 3
  else: 
    return str * 3