'''
The following code shall get an input from the user and distinguish if the number is odd or even
'''

while True:
    selnum = input("Please provide a number between 1-1000 and I' ll let you know if its odd or even!\nIf you wish to stop the procedure type STOP.\n")
    if selnum == "STOP":
        quit()
    if selnum.isdigit():
        if "." or "," not in selnum:
            selnum = int(selnum)
            if selnum >=1 and selnum <=1000:
                if selnum % 2 == 0:
                    print("The number you entered is even\n\n")
                else:
                    print("The number you entered is odd\n\n")
        
            
