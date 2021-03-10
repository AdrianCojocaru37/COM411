print("What type of adventure would you like ?")
type_adventure =input()
if(type_adventure == "scary") or (type_adventure == "short"):
  print("Enter the dark forest!")
elif(type_adventure == "safe") or (type_adventure == "long"):
  print("Take the safe route")
else:
  print("Not sure where to go")