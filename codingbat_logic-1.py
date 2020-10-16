# Logic-1

## cigar_party
def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60 and is_weekend is False:
    return True
  elif cigars >= 40 and is_weekend is True:
    return True
  else:
    return False

## caught_speeding
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

## love6
def love6(a, b):
  if a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6:
    return True
  else:
    return False

## date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

## sorta_sum
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  else:
    return a + b

## in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return 1 <= n <= 10

## squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  else:
    return 60 <= temp <= 90

## alarm_clock
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

## near_ten
def near_ten(num):
  x = num % 10
  if 10 - x <= 2 or x <= 2:
    return True
  else:
    return False
