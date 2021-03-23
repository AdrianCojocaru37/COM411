#Program that imitates a small database in the sense that it can
#insert new students and their max
#keep continually add students
#print out stundent's name and their max
#find out the maximum mark

#all_students =[("Gary",67),("Uzma,82"),("Mihai,76")]
#print(all_students[0])


def generate_stds():
  print("Enter the name: ")
  name = input()
  print("Enter the grade: ")
  grade = int(input())
  return name, grade

def all_stds():
  all_students =[]
  while True:
    all_students.append(generate_stds())
    print("To stop adding students, type 0")
    x = input()
    if x == '0':
      break
  return all_students


def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")

#print_students(all_stds())

def avr_mark(lista):
  total =0
  for std in lista:
    total += std[1]
  return total/len(lista)


print(avr_mark(all_stds()))