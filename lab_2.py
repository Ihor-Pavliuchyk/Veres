import math
x = 2

while True:
    if x > 5: 
        break 
    elif x < 3:
        result = (math.cos(x**0.3))
    elif 3 <= x < 4:
        result = ((x**3 + math.log10(x))**0.5)
    else:
        result = (1 / math.tan(x**2))
    print(result)
    x += 0.2

