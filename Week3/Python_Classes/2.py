def myFunc(fahrenheit):
    celsius = (fahrenheit - 32) * float(5/9)
    return celsius
fahrenheit_deg = float(input())
celsius_deg = myFunc(fahrenheit_deg)
print("Celsius:",celsius_deg)