def temp(a, b, c, t):
  return a * t**2 + b * t + c
with open('task3.txt', 'r') as f:
  l = f.readlines()
  a = float(l[0].strip())
  b = float(l[1].strip())
  c = float(l[2].strip())
  t = float(l[3].strip())
print("At time ",t,",the temperature is : ",temp(a,b,c,t))