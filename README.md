# Arithmetic-Formatter

## Arithmetic Formatter project for freecodecamp.org Scientific Computing with Python course

The function is used to develop a simple arthemertic operator, "235 + 52" becomes: <br>
<figure>
  <img width="128" alt="example 1" src="https://github.com/semereab-merry/Arithmetic-Formatter/assets/59441158/711507a0-0bf1-42a8-8305-7c00f50626f2">
</figure>

 <br>
It receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed like this: <br>
<figure>
<img width="377" alt="example 2" src="https://github.com/semereab-merry/Arithmetic-Formatter/assets/59441158/9dac579c-2ac8-41c9-9013-c0f99ad8101e">
</figure>

 <br>
 
### Situations that will return an error: <br>
1. If there are too many problems supplied to the function.
The limit is five, anything more will return: *Error: Too many problems.*
2. The appropriate operators the function will accept are addition and subtraction.
Multiplication and division will return an error. The error returned will be: *Error: Operator must be '+' or '-'.*
3. Each number (operand) should only contain digits. Otherwise, the function will return: *Error: Numbers must only contain digits.*
4. Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: *Error: Numbers cannot be more than four digits.*
<br>

### If the user supplied the correct format of problems, the conversion you return will follow these rules: <br>
1. There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, and both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
2. Numbers should be right-aligned.
3. There should be four spaces between each problem.
4. There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
<br>

### Test and Deployment
<figure>
<img width="580" alt="colole image" src="https://github.com/semereab-merry/Arithmetic-Formatter/assets/59441158/7714c989-ecc4-4804-8984-17733ce5b93d">
</figure>

