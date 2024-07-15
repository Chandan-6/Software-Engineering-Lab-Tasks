# | Hard-coded values |

def temp(a,b,c,t):
  return round(a*t**2+b*t+c) # round will the values such as 13.399999999999999
a=4.1
b = -2.0
c = 1.0
t = 2
print("At time ",t,",the temperature is : ",temp(a,b,c,t))