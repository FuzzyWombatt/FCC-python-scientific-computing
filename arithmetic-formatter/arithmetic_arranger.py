import re

def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  f_line = ''
  s_line = ''
  under_line = ''
  solved = ''
  space = "    "

  index = 0

  for problem in problems:
    index += 1
    
    operands = problem.split()

    if operands[1] not in  "+-":
      return "Error: Operator must be '+' or '-'."

    if len(operands[0]) > 4 or len(operands[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if re.search('[^\s0-9]',operands[0]) or re.search('[^\s0-9]',operands[2]):
      return "Error: Numbers must only contain digits."
     

    num = 0
    if solve is True:
      if operands[1] == '+':
        num += int(operands[0])+int(operands[2])
      elif operands[1] == '-':
        num += int(operands[0])-int(operands[2])
    
    width = max(len(operands[0]), len(operands[2]))+2
    
    if index != len(problems):
      f_line += f"{operands[0]:>{width}}"+space
      s_line += operands[1] + f"{operands[2]:>{width-1}}"+space
      under_line += '-'*width+space
      solved += f"{str(num):>{width}}"+space
    else:
      f_line += (f"{operands[0]:>{width}}"+"\n")
      s_line += operands[1] + f"{operands[2]:>{width-1}}"+"\n"
      under_line += ('-'*width)
      solved += f"{str(num):>{width}}"
    
    

  arranged_problems = ''
  if solve is True:
    arranged_problems += f_line+s_line+under_line+"\n"+solved
  else:
    arranged_problems += f_line+s_line+under_line

  print(arranged_problems)
  return arranged_problems
  