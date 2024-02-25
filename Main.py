"""
This program will generate unofficial transcripts
and it will calculate total GPA and Credit per semester and cumulative
"""

import numpy as np
from __ScreenOptions import Screen
from __DataBase import DataBase
import __Backend as Backend


Screen = Screen
DataBase = DataBase()

while(True): # program main menu screen
    mainMenuChoice = Screen.home()
    if(mainMenuChoice == "1"): #main menu > Create Transcript
        DataBase.createDatabase()
        #__________________________________________________________________________#
        while(True): # Transcript Creation Page
            transcriptChoice = Screen.transcript()
            if(transcriptChoice == "1"): #Transcript > Add Semester
                DataBase.addSemester()
                #+++++++++++++++++++++++++++++++++++++++++++++++++++++++#
                while(True): #Semester Course Adding Page
                    semesterChoice = Screen.semester()
                    if(semesterChoice == "1"): # Semester > Add Course
                        DataBase.addCourse()
                    elif(semesterChoice == "0"): # Semester > Save the Semester and Exit
                        DataBase.saveSemester()
                        break
                #+++++++++++++++++++++++++++++++++++++++++++++++++++++++#
                    
            elif(transcriptChoice == "2"): # Transcript > Display Transcripts
                #Backend.displayTranscript
                Backend.displayTranscript(DataBase)
                break
            elif(transcriptChoice == "0"):
                break
        #________________________________________________________________________#
    elif(mainMenuChoice == "0"): # main menu > Exit Program
        Screen.programClose()
        break