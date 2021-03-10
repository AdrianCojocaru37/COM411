print("How many live cable should i avoid?")
avoid_cable = int(input())
number_live_cables = 0
while(number_live_cables < avoid_cable):
  print("Avoiding..", end = "")
  number_live_cables = number_live_cables + 1
  print("Done!", number_live_cables, "number live cables"