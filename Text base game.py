import time
def welcome():
    print("Welcome to Woods adeventure!!!")

def introinstructions():
         print(" ")
         print("You will be in the wood for a total of two days. There you will encounter many different")
         time.sleep(2)
         print("obstacles that you will have to over come, so prepare your bags and yourself. You will")
         time.sleep(2)
         print("encounter storms different routes and you wil have to tell me what path to choose by path")
         time.sleep(2)
         print("to choose by path names which will be provided. You will start with full health and will")
         time.sleep(2)
         print("decline with bad weather and so on. Yout goal is to get home safely.")
         print(" ")
def readyresponse():
    time.sleep(3)
    ready = input("Are you ready to begin? (Yes or No) ").capitalize()
    if ready == "Yes":
        print("Lets begin!!")
    if ready == "No":
        print("I will you give 4 seconds to prepare.")
        time.sleep(4)
        print("Its time to begin.")
def firstmove():
    time.sleep(4)
    print(" ")
    print("As you are leaving home and start walking to the woods you come across a young hurt woman. You have" )
    time.sleep(2)
    print("the option to help her out or keep walking.")
    print(" ")
    help1 = input("Do you want to help or keep walking? (Help or Walk) ").capitalize()
    if help1 == "Help":
        print("")
        print("The woman will need one of the only shirts to you brought along to cut the excessive blood flow")
        time.sleep(2)
        print("You take the only extra shirt you have in your backpack and help cut the blood flow.")
        time.sleep(2)
        print("She tells you that she has been in the woods for a day without eating anything. She asks you for food.")
        print(" ")
    if help1 == "Walk":
        print("Walk")
def ifstayedtohelp ():
    food1 = input("Do you want to share 1 out of the 5 can goods you brought? (Share, Walk) ")
   
    

welcome()
introinstructions()
readyresponse()
firstmove()
ifstayedtohelp()


