print("Where should i look?")
location = input()
if( location == "in the bedroom"):
  print("Where in the bedroom should i look for ?")
  bedroom_place = input()
  if( bedroom_place == "under the bed"):
    print("Found some shoes but no baterry")
  else:
    print('Found some mess but no baterry')
elif( location == "in the bathroom"):
  print("where in the bathroom should i look for?")
  bathroom_location = input()
  if( location == "in the bathtub"):
    print("Fund a rubber toy but no baterry")
  else:
    print("Found a wet surface but no baterry")
elif( location == "in the lab"):
  print("Where in the lab should i look for?")
  lab_location = input()
  if(lab_location == "on the table"):
    print("I find the keys")
  else:
    print("Found some tools but no baterry")
else:
  print("I dont know where they are")