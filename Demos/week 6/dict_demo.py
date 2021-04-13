def shop():
  items = {
    "eggs": 1.99,
    "milk": 0.99,
    "Cereals":2.99,
    "steak": 4.79,
    "beer": 2.99,
    "sausage": 1.29,
    "vinegar":2.49,
    "bread":1.49

  }
  return items

def view_all(products ={}):
  for i in products:
    print(i)

def basket():
  basket =[]
  while True:
    item = input("Enter item(or \"stop\")")
    if items == "stop":
      break
    else:
      basket.append(item)

  return basket
def till(basket =[]):
  shoplist = shop()
  total = 0.0
  for item basket:
    total+=soplist[item]
  return total

def run():
  print("Welcome to Pete shop !")
  chosen_items =basket()
  while True:
    print("Are you ready to pay?")
    if input().lower()=="yes":
      to_pay = till(chosen_items)
      print(f"Please pay£{to_pay:.2f} by cash or card")
      break
    else:
      chosen_items += basket()
      run()
run()