"""
This Module contains backend handling functions
"""

from __DataBase import DataBase
import numpy as np

def displayTranscript(databaseObj):
    for i in range(25):
        print("|+|", end="")
    print("")
    print(databaseObj.transcriptName + " Transcript Information:")
    for i in range(50):
        print("_", end="")
    print("")

    transcriptArray = np.loadtxt(R"__DB\\"+databaseObj.transcriptName+".csv",delimiter=',',dtype=str)

    print("Semester\t\tClass Name\t\tGrade\t\tCredit\t\tSem-GPA\t\tCumulative GPA")
    for i in range(100):
        print("_", end="")
    print("")
    rowIndex = 0
    for row in transcriptArray[:,0]:
        print(row,"\t\t",transcriptArray[rowIndex,1],"\t\t"+transcriptArray[rowIndex,2],"\t\t",transcriptArray[rowIndex,3],"\t\t"+transcriptArray[rowIndex,4],"\t\t",transcriptArray[rowIndex,5])
        rowIndex+=1

# transcriptArray = np.loadtxt(R"__DB\final shit.csv",delimiter=',',dtype=str)

# print("Semester\t\tClass Name\t\tGrade\t\tCredit\t\tSem-GPA\t\tCumulative GPA")
# for i in range(100):
#     print("_", end="")
# print("")
# rowIndex = 0
# for row in transcriptArray[:,0]:
#     print(row,"\t\t",transcriptArray[rowIndex,1],"\t\t"+transcriptArray[rowIndex,2],"\t\t",transcriptArray[rowIndex,3],"\t\t"+transcriptArray[rowIndex,4],"\t\t",transcriptArray[rowIndex,5])
#     rowIndex+=1
