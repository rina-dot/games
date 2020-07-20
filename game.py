import random

computer_integer = random.randint(1, 20)


while True:
    try:
        your_int = int(input("Input number: "))
    except:
        print("ENTER NUMBERS")
        continue



    if your_int > computer_integer:
        print("too much")
    elif your_int < computer_integer:
        print("too low")
    else:
        print ("cool")
        break
