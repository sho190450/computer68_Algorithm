def MainMenu():
    print("" \
    "Press Enter Q = Exit\n " \
    "C = calculate")
    inp = input(" : ")
    if(inp == "Q" or inp == "q"):
        exit
    elif(inp == "C" or inp == "c"):
        Calculate()
    else:
        MainMenu()


def Calculate():
   print("+ = Plus\n" \
   "- = Minus\n" \
   "* = Multiply\n" \
   "/ = Divide\n" \
   "M = Main/Home\n" \
   "** = Power")
   inp = input(" : ")

   if(inp == "+"):
         inp = input("N : ")
         total = 0
         N = int(inp)
         for x in range(N):
            total += int(input("Number : "))
         print("Total = ", total)
         Calculate()
   elif(inp == "-"):
         inp = input("N : ")
         N = int(inp)
         total = int(input("Number : "))
         for x in range(N-1):
            total -= int(input("Number : "))
         print("Total = ", total)
         Calculate()
   elif(inp == "*"):
         inp = input("N : ")
         N = int(inp)
         total = 1
         for x in range(N):
            total *= int(input("Number : "))
         print("Total = ", total)
         Calculate()
   elif(inp == "/"):
         inp = input("N : ")
         N = int(inp)
         total = int(input("Number : "))
         for x in range(N-1):
            total /= int(input("Number : "))
         print("Total = ", total)
         Calculate()
   elif(inp == "**"):
         base = float(input("N : "))
         power = float(input("Number : "))
         total = base ** power
         print("Total = ", total)
         Calculate()
   elif(inp == "M" or inp == "m"):
         MainMenu()
   else:
         Calculate()
MainMenu()