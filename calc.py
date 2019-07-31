while True:
    try:
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))

        operation = input('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ----------------------
        ''')
        print("-------------")

        if operation == '+':
            print('{} + {} = '.format(a, b),a + b)

        elif operation == '-':
            print('{} - {} = '.format(a, b),a - b)

        elif operation == '*':
            print('{} * {} = '.format(a, b),a * b)

        elif operation == '/':
            print('{} / {} = '.format(a, b),a / b)

        else:
            print('You have not typed a valid operator, please run the program again.')
        break
        
    except ValueError:
        print("-----------------------------------")
        print("Error ! Input has to be a number ! ")

    except ZeroDivisionError:
        print("------------------------------------------")
        print("Error ! It is impossible to divide by zero")

    finally:
        print("The 'try except' is finished\n")