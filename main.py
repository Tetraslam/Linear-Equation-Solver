import time

def solve_equation(a, b):
    start_time = time.time() # Measures efficiency
    if a == 0:
        if b == 0:
            print("This equation has an infinite number of solutions.")
        else:
            print("This equation has no solutions.")
    else:
        x = -b / a
        print("The solution to this equation is x =", x)
    elapsed_time = time.time() - start_time
    print("Time elapsed: ", elapsed_time, " seconds")

a = float(input("Enter the coefficient of x: "))
b = float(input("Enter the constant term: "))
solve_equation(a, b)
