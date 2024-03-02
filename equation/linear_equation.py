import math

def pick():
    print("\n1. Solve linear equation")
    print("2. End solving equation")
    choices = int(input("Please choose one: "))
    
    if choices == 1:
        linear()
    elif choices == 2:
        print()
    else:
        print("Bruh")
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
        if A == 0 and B == 0 or D == 0 and E == 0:
            print("Simultameous equation without solution.")
            return linear()
        elif A==0 and B==0 and D==0 and E==0:
            print("Simultameous equation with infinite solutions.")
            return linear()
        elif A or B and D or E != 0:
            Y = (-D*C + F*A)/(A*E - D*B)
            X = (C - B*Y)/A
            print(f"⇒ x = {X}; y = {Y}")
            return pick()
        else:
            print("Mistake!")
            return linear()
    else:
        print("Try again!")
        return linear()
pick()