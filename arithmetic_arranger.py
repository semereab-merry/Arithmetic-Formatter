import re

def arithmetic_arranger(problems, output = False):
  # the second input for the function is indicating if the program should solve the equation or not, the default is false so that the program will only operate the sum/subtract of the input numbers 

  # we need to check if there are <= 5 problems given before we start to work
  if (len(problems) > 5):
    return "Error: Too many problems."
    
  # after we check the num of inputs, we define some variables that are useful for the output

  firstLine = ""    # the first line of numbers 
  secondLine = ""    # the second line of numbers with + or -
  dashLine = ""      # the dashes equal to digits of the highest num
  sumNums = ""        # the output of sum or subtract 
  finalString = ""      # the final string output 

  # first we are going to get each problem from the problems list in the input 

  for problem in problems:
    # we will use the re package to check if the given input contains digits and +/- only 
    
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    # then we can assign each of the inputs to separate variables
    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    # check the number of digits for each operand 
    if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return "Error: Numbers cannot be more than four digits."

    # the sum or subtract of two nums  
    sumDiv = ""
    if (operator == '-'):
      sumDiv = str(int(firstNumber) - int(secondNumber))  #str(): because the variable is string only string values must be assigned to it 
    elif (operator == '+'):
      sumDiv = str(int(firstNumber) + int(secondNumber))  #int(): to operate the two digits they must be converted from str to int type 

    # we create a length variable that compares the length of of the 2 operands and take the maximum one; this length will be the length of of the output for single operation 
    # the 2 added for the length are for the operator and the white space after the operator  
    length = max(len(firstNumber), len(secondNumber)) + 2

    # each operation will be adjust accoring to the length of maximum operand , we use rjust (adjust to right)
    top = str(firstNumber).rjust(length)
    # we adjust length - 1, as 1 space will be used by the operator 
    bottom = operator + str(secondNumber).rjust(length-1)
    
    # now we have arranged the top and bottom lines accordingly, whats left is the dashes between the last operand and the result 
    dashes = ""
    for i in range(length):
      dashes += "-"

    # lastly, the result; adjusted to the right 
    resul = str(sumDiv).rjust(length)
    
    # we need to add each of the problems to the variables we have defined at the beginning of this function 
    if problem != problems[-1]:
      # if the operation is not the last one, we will add 4 whitespaces in between the operations 
      firstLine += top + '    '
      secondLine += bottom + '    '
      dashLine += dashes + '    '
      sumNums += resul + '    '

    else:
      firstLine += top
      secondLine += bottom
      dashLine += dashes
      sumNums += resul

  # after we finish assigning we have to final results to the 'finalString' string, accordingly to the True/False input 
  if output:
    finalString = firstLine + "\n" + secondLine + "\n" + dashLine + "\n" + sumNums
  else: 
     finalString = firstLine + "\n" + secondLine + "\n" + dashLine 

  # we return the final string 
  return finalString