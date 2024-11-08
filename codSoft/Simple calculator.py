# Define function for Addition..
def add(num_1, num_2):
    return num_1 + num_2

# Define function for Substraction...
def Sub(num_1, num_2):
    return num_1 - num_2

# Define function for Multiplication..
def mul(num_1, num_2):
    return num_1 * num_2

# Define function for Division 
def div(num_1, num_2):
    if num_2 == 0: #Invalid when User Enter Zero
        raise ZeroDivisionError("Can not Divided By Zero")
    return num_1 / num_2

# Define function for the Operation we are going to perform..
def operation():
    num_1 = float(input("Enter the first Number :-")) # Enter First Number By User 
    num_2 = float(input("Enter the Second Number :-")) # Enter Second Number By User

     # Your Choice 
    print("\n Choice of operator :- ")
    print("1. For Addition of two number :-")
    print("2. For Subtraction of two number :-")
    print("3. For Multiplication of two number :-")
    print("4. For Division of two number :-")
    choice = input("Enter the operator You want to choose fron above (1,2,3,4):-")

    # Validate User's Operation Choice..... 
    if choice not in ['1','2','3','4']:
        print("Invalid Operator! Please Choose valid Oprator")
        return
    
# Check Whether  User Enter Invalid Operator..
    try:
        if choice == '1':
            res = add(num_1, num_2) # Result Of Addition
        elif choice == '2':
            res = Sub(num_1, num_2) # Result Of Substraction
        elif choice == '3':
            res = mul(num_1, num_2) # Result Of Multiplication
        elif choice == '4':
            res = div(num_1, num_2) # Result Of Division
        print(f"\n Result is :-{res}")
    except ZeroDivisionError as e:
        print(f"\n Error Because u Enter 0 in Deominator {e}")
# Call Function for Operaton .....
operation()
