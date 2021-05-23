import matplotlib.pyplot as plt
import random as rnd

def data():
  paths={}
  type_line = input("What line would you like?")
  colour=input("What color would the line should be?")
  style_marker=input("What style marker would you like?")

  paths["type_line"]=type_line
  paths["color"]= colour
  paths['style_marker']=style_marker

  return paths

  def generate():
    number_lines=input("How many lines would you like to display?")

    for count in range(number_lines):
      values=data()
      x = rnd.sample(range(1, 10), 5)
      y = rnd.sample(range(1, 10), 5)
      format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
    plt.plot(x, y, format)
  
  plt.show()

  def run():
    print("Running...")
    generate()
    print("Done!")
  run()
