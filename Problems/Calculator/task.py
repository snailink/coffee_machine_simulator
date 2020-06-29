# put your python code here
def operation_function(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "/":
        if second_number == 0.0:
            return "Division by 0!"
        else:
            return first_number / second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "mod":
        if second_number == 0.0:
            return "Division by 0!"
        else:
            return first_number % second_number
    elif operation == "pow":
        return first_number ** second_number
    elif operation == "div":
        if second_number == 0.0:
            return "Division by 0!"
        else:
            return first_number // second_number


def main():
    first_number = float(input())
    second_number = float(input())
    operation = input()
    print(operation_function(first_number, second_number, operation))


main()
