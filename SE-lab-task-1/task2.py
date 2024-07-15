# | Input values from user |

def temp(a,b,c,t):
  return round(a*t**2+b*t+c)
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))
t = float(input("Enter Time: "))
print("At time ",t,",the temperature is : ",temp(a,b,c,t))