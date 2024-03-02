#planning
import time
import math

def pick():
    print("\nA - Linear equation")
    print("B - Quadratic equation")
    print("C - Cubic equation")
    print("D - Quartic equation")
    print("E - Quit equation")
    choices = input("Please choose an equation to continue: ")
    
    if choices == "A" or "a":
        linear()
    elif choices == "B" or "b":
        quadratic()
    elif choices == "C" or "c":
        cubic()
    elif choices == "D" or "d":
        quartic()
    elif choices == "E" or "e":
        print()
    else:
        print("Choose again blud")
        return pick()
    
def linear():
    print("\n1. One variable")
    print("2. Two variables")
    choose = int(input("Please choose one: "))
    
    if choose == 1:
        print("\nAx + B = C")
        A = float(input("A : "))
        B = float(input("B : "))
        C = float(input("C : "))
        print(f"\n=> {A}x + {B} = {C}")
        X = (C - B)/A
        print(f"⇒ x = {X} ")
        time.sleep(2)
        return pick()
    elif choose == 2:
        print("\nAx + By = C\nDx + Ey = F")
        A = float(input("A : "))
        B = float(input("B : "))
        C = float(input("C : "))
        D = float(input("D : "))
        E = float(input("E : "))
        F = float(input("F : "))
        print(f"\n{A}x + {B}y = {C}\n{D}x + {E}y = {F}")
        time.sleep(1)
        if A == 0 and B == 0 or D == 0 and E == 0:
            print("Simultameous equation without solution.")
            time.sleep(1)
            return linear()
        elif A==0 and B==0 and D==0 and E==0:
            print("Simultameous equation with infinite solutions.")
            time.sleep(1)
            return linear()
        elif A or B and D or E != 0:
            Y = (-D*C + F*A)/(A*E - D*B)
            X = (C - B*Y)/A
            print(f"⇒ x = {X}; y = {Y}")
            time.sleep(1)
            return pick()
        else:
            print("Mistake!")
            return linear()
    else:
        print("Try again!")
        return linear()
    
def quadratic():
    print("\nCondition: a ≠ 0")
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))
    delta = b*b - 4*a*c
    
    if delta < 0:
        print(f"\n∆ : {delta}")
        print("The equation has no distinct real roots.")
        return pick()
    elif delta == 0:
        print(f"\n∆ : {delta}")
        print("The equation has one repeated real root.")
        time.sleep(1)
        x = -b/(2*a)
        print(f"X: {x}")
        return pick()
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"\n∆ : {delta}")
        print("The equation has two distinct real roots.")
        time.sleep(1)
        print(f"X1: {x1}")
        print(f"X2: {x2}")
        return pick()
    else:
        print("Bruh how?")
        time.sleep(3)
        return pick()
    
def cubic():
    print("Hello world")  
    
    
     
def quartic():
    print("Hello world")
    
pick()
