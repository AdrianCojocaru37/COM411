

def student():
  print("Enter your name:")
  name=input()
  print("What is your age?")
  age = int(input())
  print("Do you have a dog?")
  dog=input()
  if dog =="yes":
    dog_bool = True
  else:
    dog_bool = False
  return name,age,dog_bool
""""
person = ("Piotr", 67,False)

print(person)


# Access elements via index just u do with list
print(person[1])

if person[2]:
  print("Yay--you have a dog")
else:
  print("No dog!!!")

print("Which item to print?")

if n<len(person):
  print(person[n-1])
# you cannot modify (mutate)a tuple

#person[0]="peter"
#print(person)

print(person+2000)
"""
print("How many students to generate")
n = int(input())
count=0# keep track of how many repetitions we have done


all_students =[]
while(count<n):
  tuplex=student()
  all_students.append(tuplex)
  count+=1
print(all_students)