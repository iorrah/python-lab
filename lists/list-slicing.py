beatles = [
  'Ringo',
  'George', 
  'John', 
  'Paul', 
  'Noaman',
  'Pete', 
  'Stu', 
  'Tommy',
  'Chas',
  'Jimmie',
]

print ('{} and {} played the'
  ' bass'.format(beatles[3], beatles[-4]))

fab = beatles[0:4]
str_fab = ', '.join(fab)

print 'Have you have heard about {}?'.format(str_fab)
