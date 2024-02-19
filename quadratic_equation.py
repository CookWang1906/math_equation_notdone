import math

def pick():
    print("\n1. Solve quadratic equation")
    print("2. End solving equation")
    choice = int(input("Choose 1 or 2: "))
    
    if choice == 1:
        quadratic()
    elif choice == 2:
        print()
    else:
        print("What blud doing?")
        return pick()

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
pick()