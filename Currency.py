'''Implement a program in python which will take a input value in 
floating number for INR currency and provide four different options 
1. To re-enter the INR currency
2. To convert the INR currency to USD Dollar
3. To convert the INR Currency to Japanese Yen
4. To convert the INR Currency to European Euro
After executing one of the four options further three options are provided 
A. To exit the program 
B. To go to the main menu
C. To Change the main options'''
INR=float(input("Enter the amount in INR: "))
print('''
      1.Re-enter the INR
      2.Conversion to USD DOLLAR
      3.Conversion to Japanese Yen
      4.Conversion to European Euro''')
n=int(input("Enter the conversion unit: "))
USD = 0.012
YEN = 1.7
EURO = 0.012
if n==1:
        INR=float(input("Enter the amount in INR: "))
        print('''
            1.Re-enter the INR            
            2.Conversion to USD DOLLAR
            3.Conversion to Japanese Yen
            4.Conversion to European Euro''')
        n=int(input("Enter the conversion unit: "))
        USD = 0.012
        YEN = 1.7
        EURO = 0.012
        if n==2:
            print("In USD: ",INR*USD)
        if n==3:
            print("In YEN: ",INR*YEN)
        if n==4:
            print("In EURO: ",INR*EURO)
        print('''
            5.EXIT PROGRAM:
            6.GO TO MAIN MENU:
            7.CHANGE THE MAIN OPTION:''')
        x=int(input("Enter Option: "))
        if x==5:
            print("You Successfully Exited the Program ")
        if x==6:
            INR=float(input("Enter the amount in INR: "))
            print('''
                1.Re-enter the INR
                2.Conversion to USD DOLLAR
                3.Conversion to Japanese Yen
                4.Conversion to European Euro''')
            n=int(input("Enter the conversion unit: "))
            USD = 0.012
            YEN = 1.7
            EURO = 0.012
            if n==1:
                print("Re-enter is",INR)
            if n==2:
                print("In USD: ",INR*USD)
            if n==3:
                print("In YEN: ",INR*YEN)
            if n==4:
                print("In EURO: ",INR*EURO)
            if x==7:
                print('''
                    1.Re-enter the INR
                    2.Conversion to USD DOLLAR
                    3.Conversion to Japanese Yen
                    4.Conversion to European Euro''')
                n=int(input("Enter the conversion unit: "))
                USD = 0.012
                YEN = 1.7
                EURO = 0.012
                if n==1:
                    print("Re-enter is",INR)
                if n==2:
                    print("In USD: ",INR*USD)
                if n==3:
                    print("In YEN: ",INR*YEN)
                if n==4:
                    print("In EURO: ",INR*EURO)
    
if n==2:
    print("In USD: ",INR*USD)
if n==3:
    print("In YEN: ",INR*YEN)
if n==4:
    print("In EURO: ",INR*EURO)
print('''
      5.EXIT PROGRAM:
      6.GO TO MAIN MENU:
      7.CHANGE THE MAIN OPTION:''')
x=int(input("Enter Option: "))
if x==5:
    print("You Successfully Exited the Program ")
if x==6:
        INR=float(input("Enter the amount in INR: "))
        print('''
                1.Re-enter the INR
                2.Conversion to USD DOLLAR
                3.Conversion to Japanese Yen
                4.Conversion to European Euro''')
        n=int(input("Enter the conversion unit: "))
        USD = 0.012
        YEN = 1.7
        EURO = 0.012
        if n==1:
         print("Re-enter is",INR)
        if n==2:
         print("In USD: ",INR*USD)
        if n==3:
         print("In YEN: ",INR*YEN)
        if n==4:
         print("In EURO: ",INR*EURO)
if x==7:
        print('''
            1.Re-enter the INR
            2.Conversion to USD DOLLAR
            3.Conversion to Japanese Yen
            4.Conversion to European Euro''')
        n=int(input("Enter the conversion unit: "))
        USD = 0.012
        YEN = 1.7
        EURO = 0.012
        if n==1:
            print("Re-enter is",INR)
        if n==2:
            print("In USD: ",INR*USD)
        if n==3:
            print("In YEN: ",INR*YEN)
        if n==4:
            print("In EURO: ",INR*EURO)
    

