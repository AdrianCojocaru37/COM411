print("How many bars should be charged?")
bars = int(input())
number_bars = 0
while( number_bars < bars):
  print("Charging:", "u\275F" * number_bars)
  number_bars = number_bars +1
print("Batter is fully charged")