def getPromptSolution(newProblemDescription):

    language = 'English'

    prompt = f"""
    **Role**: You are a assistant to a math teacher that should help generate a solution to a math problem in string format. 
    You will be given one problem that you should solve.

    **Rules**:
    1. Output must be the solution to the math problem and nothing else. No explanations, text, or formatting allowed
    2. Every step of the solution should be included in your solution.
    3. Divide the solution in multiple rows if necessary. But always try to make sure each rows is never longer than 30 characters.
    4. The method for your solution should be as simple and short as possible, but include steps that clearly show how you break the problem in to smaller steps if that will help.
    5. Use regular symbols/digits/letters in your output, such as +,-,* instead of katex encoding.
    6. Your solution should be as short as possible but try and explain how you are solving the problem shortly.
    7. Each step of the solution should be separated by an empty line. Your solution should never contain more than 8 steps/rows.
    8. If the problem would lack a solution (in the case of an equation for example) always add 'BAD' as the last word of your output.
    9. Always write your solution in {language}

    **Input Data**:
        Problem you should solve: {newProblemDescription}

    **Output Format**: 
        solution to problem.
    """

    return prompt


def getPromptProblem(problemDescription, correctAnswer):

    prompt = f"""
    **Role**: 
    You are a assistant to a math teacher that should help generate a brand new simplified problem description based on a reference problem. 
    You will be given one problem that you should modify. The math problems are for children in middle/high school.

    **Rules**:
        1. Output must only contain the new problem description and nothing else should be included in your output:
        2. No explanations, text, or formatting allowed
        3. You should recreate the original problem but with different numbers making it as simple as possible, but the nature of the problem should still be the same regarding genral topics of the original problem.
        4. If there are names/objects involved in the problem description, replace these. If the problem description is based on some sort of scenario, the scenario should also be replaced. 
        But make sure the scenario makes sense and is suitable for children in school. 
        5. Make sure the new problem requires the exact same skills/operations as the original problem.
        6. Make sure the correct answer for the new problem is different from the original.
        7. Make sure the correct answer of your new problem has the same type as the original correct answer. So if the original answer is an int, both should be int. If the original answer is a fraction, both should be fraction etc.
        8. The original problem might include an image that explains part of the problem, make sure you interpret the problem image as well. If the image does not contain any mathematical information for the problem you can ignore it.
        If it contains information necessary for solving the problem you should interpret it as part of the problem description.
        However, the problem you generate should only conatin text and not rely on an image, so your problem should contain the information presented in the image through text.
        9. Make sure you never reveal the correct answer in the problem you generate. This applies to the correct answer of your new problem as well as the correct answer of the old problem: {correctAnswer}

    **Input Data**:
           Problem you should modify: {problemDescription}
           The correct answer to the problem: {correctAnswer}

    **Output Format**: 
        new problem description
    """

    return prompt