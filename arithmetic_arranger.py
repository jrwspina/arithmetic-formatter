def operation(problem):
    if problem[1] == '+':
        return str(int(problem[0]) + int(problem[2]))
    elif problem[1] == '-':
        return str(int(problem[0]) - int(problem[2]))
    
def validate(problems):
    for problem in problems:
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')
        if not(problem[0].isdigit()) or not(problem[2].isdigit()):
            raise Exception('Error: Numbers must only contain digits.')
        if problem[1] != '+' and problem[1] != '-':
            raise Exception("Error: Operator must be '+' or '-'.")
            
def arithmetic_arranger(problems, display_ans="False"):
    if len(problems) > 5:
        return "Error: Too many problems."

    parsed_problems = []
    for problem in problems:
        parsed_problems.append(problem.split())
 
    try:
        validate(parsed_problems) 
    except Exception as e:
        return str(e.args[0])
    
    for problem in parsed_problems:
        problem.append(operation(problem))

    lines = ["", "", "", ""]
    for problem in parsed_problems:
        width = max(len(problem[0]), len(problem[2])) + 2

        lines[0] += problem[0].rjust(width, ' ')                  + ' '*4
        lines[1] += problem[1] + problem[2].rjust(width - 1, ' ') + ' '*4
        lines[2] += '-' * width                                   + ' '*4
        lines[3] += problem[3].rjust(width, ' ')                  + ' '*4

    for i in range(len(lines)):
      lines[i] = lines[i].rstrip()
    
    if(display_ans is True):
         return lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3]
    return lines[0] + "\n" + lines[1] + "\n" + lines[2]