def calculate_temperature(a, b, c, time):
  return a * time**2 + b * time + c


with open('task4.txt', 'r') as file:
  lines = file.readlines()

for line in lines:
  parts = line.strip().split()
  a = float(parts[0])
  b = float(parts[1])
  c = float(parts[2])
  time = float(parts[3])
  temperature = calculate_temperature(a, b, c, time)
  print(f"At time {time}, the temperature is {temperature}")
