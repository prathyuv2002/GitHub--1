VARIABLES
4 GAME OVER = False
5 PLAYER HEALTH = 5
6 PLAYER FOOD POUNDS = 500
7 MILES TO GO = 2000
8 CURRENT DAY = 1
9 CURRENT MONTH = 3
10 MONTHS 31 DAYS = [3, 5, 7, 8, 10, 12]
11 HEALTH DECREASES THIS MONTH = 0
12
13
14 def should decrease health():
15
global HEALTH_DECREASES_THIS MONTH
16
if HEALTH DECREASES THIS MONTH < 2:
17
random day = random.randint(0, 30)
18
if random day < 2:
19
return True
20
return False
21
22 # updates the day
23 def add_day():
24
global PLAYER_FOOD_POUNDS

