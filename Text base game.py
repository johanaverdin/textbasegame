import time
print("Welcome to Woods adeventure!!!")
def introinstructions():
    instruction_answer = input("Would do like to recieve instructions? Yes or No. " ).capitalize()
    if instruction_answer == "Yes":
         print(" ")
         print("You will be in the wood for a total of three days. There you will")
         print("encounter many different obstacles that you will have to over come,")
         print("so prepare your bags and yourself")
         print(" ")
         def readyresponse():
             time.sleep(3)
             ready = input("Are you ready to begin? ").capitalize()
             if ready == "Yes":
                print("Lets begin!!")
             if ready == "No":
                print("I will you give 4 seconds to prepare.")
                time.sleep(4)
                print("Its time to begin")
         readyresponse()
    if instruction_answer == "No":
         print("no instructions")
introinstructions()



