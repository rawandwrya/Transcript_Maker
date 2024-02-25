"""
This Module contains the necessary calculations
for the Transcript Maker Program
"""
import numpy as np


def semesterGPA(semArray):
    """
    - The numpy array that contains the semester grades and credits in columns 2 and 3 respectively
    is needed as the input.
        + the values at col 2 and 3 must be convertable to float
    - The function returns the weighted average of column 2 (grades) wrt the weights at col 3 (credits)
    """
    semGrades = np.array([semArray[:,2].astype(np.float64)])
    semCredits = np.array([semArray[:,3].astype(np.float64)])
    semGPA = np.average(semGrades,weights=semCredits)
    return semGPA


def cumulativeGPA(transcriptPath, semArray):
    """
    - Transcript Database Path (path to the transcript's CSV file) + semArray are inputs
        + path must be RAW STRING
            +CSV file must have grades and credits (weights) at col 2 and 3
        + The numpy array that contains the semester grades and credits in columns 2 and 3 respectively
            is needed as the input.
        + the values at col 2 and 3 must be convertable to float
    
    - return the cumulative GPA as a single float dtype
    """

    # from the database, read all the previous grades and credits, but filter out the empty ones
    previousGrades = np.loadtxt(transcriptPath, delimiter=',', usecols=(2), dtype=str) #load the grades column
    previousGrades = previousGrades[previousGrades!=''] #filter out the empty rows
    previousGrades = (np.array(previousGrades)).astype(np.float64) #convert to np-array of floats

    previousCredits = np.loadtxt(transcriptPath, delimiter=',', usecols=(3), dtype=str) #load the grades column
    previousCredits = previousCredits[previousCredits!=''] #filter out the empty rows
    previousCredits = (np.array(previousCredits)).astype(np.float64) #convert to np-array of floats

    # from the current semester array read all the grades and grades
    semGrades = semArray[:,2].astype(np.float64) # only use the grade column and convert it to float
    semCredits = semArray[:,3].astype(np.float64) # only use the grade column and convert it to float

    # calculate cumulative GPA
    arrayOfAllGrades = np.hstack([previousGrades,semGrades])
    arrayOfAllCredits = np.hstack([previousCredits,semCredits])
    cumGPA = np.average(arrayOfAllGrades,weights=arrayOfAllCredits)
    # return Cumuative GPA
    return cumGPA


