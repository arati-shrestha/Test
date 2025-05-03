def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists to hold the components of the problems
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        # Split each problem into its components
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
        
        num1, operator, num2 = parts
        
        # Check for valid operator
        if operator not in ('+ , -'):
            return "Error: Operator must be '+' or '-'."
        
        # Check if both operands are numbers
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check the length of the operands
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate the answer
        if operator == '+':
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))
        
        # Find the maximum width for formatting
        max_length = max(len(num1), len(num2)) + 2  # +2 for operator and space
        
        # Format each line
        first_line.append(num1.rjust(max_length))
        second_line.append(operator + ' ' + num2.rjust(max_length - 2))
        dashes.append('-' * max_length)
        answers.append(answer.rjust(max_length))

    # Join the lines together with 4 spaces in between
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dashes)
    
    # Add answers if requested
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))