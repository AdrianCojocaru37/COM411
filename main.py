
def movements():
  path =["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return(path)

def run():
  print("Moving...")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")

<<<<<<< HEAD
run()
=======

def short_pattern():
  pattern = {"sequence":101,"occurrences":5}
  return(pattern)
def medium_pattern():
  pattern = {"sequence":111000,"occurrences": 25}
  return(pattern)
def long_pattern():
  pattern ={"sequence":1100110011001100,"occurrences": 50}
  return(pattern)
def run():
  print("Analysing patterns...")
  dict ={"short sequence":short_pattern,"medium sequence": medium_pattern, "long sequence": long_pattern}
  for key, value in dict.items():
    print(f"{key}: {value}")
run()


  

  

>>>>>>> 3819b3539623fd68e70d3ca04705dd7d85d15a03
