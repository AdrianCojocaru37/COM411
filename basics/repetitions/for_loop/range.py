print("What level of brightness is required?")
level_brightness = int(input())

print("\nAdjust brightness...\n")
for brightness in range(2, level_brightness +1, 2):
  print("Beep brightness level : ", "*" * brightness)
  print("bop brightness level :", "*" * brightness)
print("Adjustments complete!!!!!")