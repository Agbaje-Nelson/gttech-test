# write a function that takes your name
# and returns the first and the last characters of your name
# e.g. Chukwudi becomes Ci

name = input ("Enter you name :  ")
def function(name):
  firstletter = name[0]
  lastletter = name[len(name) -1]
  abbrevation = firstletter + lastletter;
  print (abbrevation)

newName = function(name)