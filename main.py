# pip3 install numpy pandas pillow google-generativeai google-genai
import pandas as pd
from prompts import *
from solutionImage import *
from solutionString import *
from newProblem import *
from helpers import *

if __name__ == "__main__":

    df = pd.read_csv('inData/testData.csv')

    for i in df.index:
        
        problemDescription = df['problemDescription'][i]
        problemImage = df['problemImage'][i]
        correctAnswer = df['correctAnswer'][i]

        #Repeat while solution is not solvable
        good = False
        while good == False:

            #task 1
            print('Getting new problem')
            promptProblem = getPromptProblem(problemDescription, correctAnswer)
            newProblem = getNewProblem(problemImage, promptProblem) 

            #task 2
            print('Getting solution')
            promptSolution = getPromptSolution(newProblem)
            newSolution = getSolutionString('missing', promptSolution)

            if newSolution[-3:] != 'BAD':
                good = True
            else:
                print('BAD PROBLEM!')

        #task 3
        solImagePath = getSolutionImage(newSolution, f'outData/{i}.png')
        go = input('NEXT:')