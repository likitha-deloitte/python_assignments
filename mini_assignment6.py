class InteractiveCalculator(Exception): pass
class FormulaError(Exception): pass


def value(user_input):
    input_value = user_input.split()
    if len(input_value) != 3:
       raise InteractiveCalculator('enter three elements')
    n1, op, n2 = input_value
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
       raise FormulaError('Enter first and third values in numbers')
    return n1, op, n2

def calculate(n1, op, n2):

    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    raise InteractiveCalculator('{0} is not valid operator'.format(op))

while True:
    user_input = input('enter input: ')
    if user_input == 'quit':
        break
    n1, op, n2 = value(user_input)
    output = calculate(n1, op, n2)
    print(output)

