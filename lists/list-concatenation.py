import random

everybody = [
  'Noaman',
  'Pete', 
  'Stu', 
  'Tommy',
  'Chas',
  'Jimmie',
]

fab = [
  'Ringo',
  'George', 
  'John', 
  'Paul', 
]

everybody = everybody + fab
max_index = len(everybody) - 1
random_index = random.randint(0, max_index)
beatle = everybody[random_index]

print 'Who is your favorite Beatle?' 
print 'Maybe {} ?'.format(beatle)
