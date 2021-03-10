print("How many numbers should i sum up?")
num_to_add = int(input())
summed = 0
total = 0
while(summed < num_to_add):
  print("Please enter number", summed, "of", num_to_add, ":")
  number = int(input())
  total = total + number
  summed = summed + 1

print("The answwer is ", total)