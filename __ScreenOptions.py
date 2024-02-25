"""
This includes methods for the different screens of the program
"""

class Screen:
    def home(): #Main Menu home page screen
        for i in range(100):
            print("=", end="")
        print("")
        print("What would you like to do?")
        print("1. Create Transcript")
        print("0. Exit the program")
        mainMenuChoice = input("Choose what you wish to do by entering the corresponding number above: ")
        for i in range(100):
            print("=",end="")
        print("")
        return mainMenuChoice
     
    def transcript(): # (Transcript Creation Screen)
        for i in range(100):
            print("=", end="")
        print("")
        print("What would you like to do to the Transcript?")
        print("1. Add a semester")
        print("2. Display Transcript")
        print("0. Go back without saving the transcript")
        transcriptChoice = input("Choose what you wish to do by entering the corresponding number above: ")
        for i in range(100):
            print("=",end="")
        print("")
        return transcriptChoice
    
    def semester():
        for i in range(100):
            print("=", end="")
        print("")
        print("1. add course")
        print("0. save and exit")
        semesterChoice = input("Your choice: ")
        for i in range(100):
            print("=", end="")
        print("")
        return semesterChoice


    def programClose(): # Screen for Exiting the program
        print("GOODBYE!!")
        