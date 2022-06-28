import re

def arithmetic_arranger(problems, show_answer=False):
    # receives a list of strings that are arithmetic problems
    # we want to arrange them vertically and side by side
    # we want to provide an optional second parameter,
    # and when that parameter is True, the answers should also be displayed
    first_line = ""
    second_line = ""
    lines = ""
    sol = ""
    solLine = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for prob in problems:
        if re.search("[^\s0-9.+-]", prob):
            if re.search("[/]", prob) or re.search("[*]", prob):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        
        splitp = prob.split()
        num1 = str(splitp[0])
        num2 = str(splitp[2])
        op = str(splitp[1])

        if len(num1) >= 5 or len(num2) >= 5:
            return "Error: Numbers cannot be more than four digits."
            
        if op == '+':
            sol = int(splitp[0]) + int(splitp[2])
            sol = str(sol)
        elif op == '-':
            sol = int(splitp[0]) - int(splitp[2])
            sol = str(sol)
        else:
            return 'Error: Operator must be '+' or '-'.'

        length = max(len(splitp[0]), len(splitp[2])) 
        hzLine = '-' * (length + 2)
        top = num1.rjust(length + 2)
        bottom = op + ' ' + num2.rjust(length)
        solutions = sol.rjust(length + 2)
        
        if prob != problems[-1]:
            first_line += top + '    '
            second_line += bottom + '    '
            lines += hzLine + '    '
            solLine += solutions + '    '
        else:
            first_line += top
            second_line += bottom
            lines += hzLine
            solLine += solutions
        
    if show_answer:
        final = first_line + '\n' + second_line + '\n' + lines + '\n' + solLine
    else:
        final = first_line + '\n' + second_line + '\n' + lines

    return final
            