dots = '.....'
for val in range(5):
  for dot in range(5,val+1,-1):
    print('.', end="")
  print(f'{val+1}')