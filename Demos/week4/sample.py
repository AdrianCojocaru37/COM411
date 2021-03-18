



def get_fruits():
  fruits = []
  print("How many fruit would you like to enter?")
  n = int(input())
  for i in range(n):
    print("Type in the next fruit:")
    fruits.append(input())
  
  #Print all items
  print("Your fruits are {}".format(fruits))
#Print only few items by slicing
print(f"Sliced list:{ fruits [0:5]}")

#Print only few items by using negative Index
print(f"Negative index : { fruits [] -1:1]}")
get_fruits()