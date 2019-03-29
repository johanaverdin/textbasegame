import time
def welcome():
    print("Welcome to Woods adeventure!!!")
####Rewrite and include the amount of can goos ypu brought
def introinstructions():
         print(" ")
         print("You will be in the woods for a day. There you will encounter many different")
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
    ready = input("Are you ready to begin? (Yes, No) ").capitalize()
    if ready == "Yes":
        print("Lets begin!!")
    if ready == "No":
        print("I will you give 4 seconds to prepare.")
        time.sleep(4)
        print("Its time to begin.")
def firstmove():
    time.sleep(2)
    print(" ")
    print("As you are leaving home and start walking to the woods you come across a young hurt woman. You have" )
    time.sleep(2)
    print("the option to help or walk away.")
    print(" ")
    help1 = input("Do you want to help or keep walking? (Help, Walk away) ").capitalize()
    if help1 == "Help":
        print("")
        print("The woman will need one of the only shirts to you brought along to cut the excessive blood flow")
        time.sleep(2)
        print("You take the only extra shirt you have in your backpack and help cut the blood flow.")
        time.sleep(2)
        print("She tells you that she has been in the woods for a day without eating anything. She asks you for food.")
        print(" ")
        ifstayedtohelp()
    if help1 == "Walk away":
        hungrybears()
####Come back and finsh        
def ifstayedtohelp ():
    food1 = input("Do you want to share one of the can goods you brought? (Share, Walk) ")
    if food1 == "Share":
        print("You have fed her but you have lost valuable food resources.")
             
def hungrybears ():
    print("You keep walking and go the wrong way. Yoou face a pair of hungry bears. Ohh no what are you going to do.")
    print(" ")
    bearchoice = input("You throw them two can goods but you must hide or run. What do you prefer? (Run, Hide) ").capitalize()
    if bearchoice == "Hide":
        print("The bears have found you. YOU ARE DEAD.")
    if bearchoice == "Run":
        print("Your luck. Its start raining you slip into a muddy puddle. Your backpack is open so everything falls out.")
        pickupstuff()
###finish   
def pickupstuff ():
    print(" ")
    pickup = input("Do you want to pick up your stuff? (Yes, No) ").capitalize()
    if pickup == "Yes":
        print("pick up")
    if pickup == "No":
        print("Dont pick up")

welcome()
introinstructions()
readyresponse()
firstmove()



