import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


number = 25100
milliseconds = 2123
square_root_after_delay(number, milliseconds)
