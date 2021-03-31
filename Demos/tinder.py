def interests():
  print("Enter your interests, one after another and enter \"stop\" when finished")
  set1 =set()
  

  while True:
    activity = input()
    if activity == "stop"
      break
    set1.add(activity)
  return set1
def tinderTheSecond():
  print("First person: ")
  p1set = interests()
  print("Second person: ")
  p2set = interests()
  common = p1set.intersection(p2set)
  if len(common) > 4:
    print(f"Yay you are a match! you have {len(common)} interests")
  else:
    print("I don't think its going to work out you only have {len(common())} interests in common")
tinderTheSecond()