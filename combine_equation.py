#planning
import math

def pick():
    print("\nA - Linear equation")
    print("B - Quadratic equation")
    print("C - Cubic equation")
    print("D - Quartic equation")
    choices = input("Please choose an equation to continue: ")
    
    if choices == "A":
        linear()
    elif choices == "B":
        quadratic()
    elif choices == "C":
        cubic()
    elif choices == "D":
        quartic()
    else:
        print("Choose again blud")
        return pick()
    
def linear():
    print("Hello world")
    
def quadratic():
    print("\nCondition: a != 0")
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))
    delta = b*b - 4*a*c
    
    if delta < 0:
        print(f"\nDelta: {delta}")
        print("The equation has no distinct real roots.")
        return pick()
    elif delta == 0:
        print(f"\nDelta: {delta}")
        print("The equation has one repeated real root.")
        x = -b/(2*a)
        print(f"X: {x}")
        return pick()
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"\nDelta: {delta}")
        print("The equation has two distinct real roots.")
        print(f"X1: {x1}")
        print(f"X2: {x2}")
        return pick()
    else:
        print("Bruh how?")
        return pick()
    
def cubic():
    print("Hello world")         
def quartic():
    print("Hello world")
pick()