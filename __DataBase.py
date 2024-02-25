import numpy as np
import __Calculations as calculate

class DataBase:
    def __init__(self,):
        self.transcriptName = ''
        self.semesterNumber = 0
        self.semesterNames = []
        self.semesterArrays = []

    def createDatabase(self):
        transcriptName = input("Enter the transcript name: ")
        self.transcriptName = transcriptName
        with open(R'__DB\\'+transcriptName+'.csv', "w") as file:
            pass
    
    def addSemester(self):
        self.semesterNumber += 1
        self.semesterNames.append("Semester "+str(self.semesterNumber))
        self.semesterArrays.append(np.empty((0,6),dtype=str))

    def addCourse(self):
        courseName = input("Course Name: ")
        courseGrade = input("Course Grade: ") 
        courseCredit = input("Course Credit: ")
        courseToAppend = np.array([self.semesterNames[-1],courseName,courseGrade,courseCredit,'',''])
        self.semesterArrays[-1] = np.vstack([self.semesterArrays[-1] ,courseToAppend])
    
    def saveSemester(self):
        # calculate semester GPA
        semGPA = calculate.semesterGPA(self.semesterArrays[-1])
        roundedSemGPA = str(np.round(semGPA,2))
        # calculate cumulative GPA
        cumGPA = calculate.cumulativeGPA(R'__DB\\'+self.transcriptName+'.csv',self.semesterArrays[-1])
        roundCumGPA = str(np.round(cumGPA,2))
        #append the Semester array with the new calculated values
        lineToAppend = np.array([self.semesterNames[-1]+' Totals','','','',roundedSemGPA,roundCumGPA])
        self.semesterArrays[-1] = np.vstack([self.semesterArrays[-1] ,lineToAppend])
        # store the new row of sem and cum GPA with the semester record
        with open(r"__DB\\"+self.transcriptName+".csv",'a') as file:
            np.savetxt(file,self.semesterArrays[-1],delimiter=',',fmt='%s')
