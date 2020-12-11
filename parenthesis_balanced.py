# -*- coding: utf-8 -*-

def is_balanced(brackets):
    open_brackets = "({["
    close_brackets = ")}]"
    stack = []
    balanced = False

    balanced_string = ""

    print("String_2_Balance: {}".format(brackets))

    for bracket in brackets:
        print("bracket_eval: {}: ".format(bracket))
        if bracket in open_brackets:
            stack.append(bracket)
            balanced_string += bracket
        elif len(stack) == 0:
            return False
        elif bracket in close_brackets:
            balanced_string += bracket
            stacked = stack.pop()

            closed_bracket_position = close_brackets.index(bracket)

            stack.append(closed_bracket_position)

            open_bracket = open_brackets[closed_bracket_position]

            if stacked != open_bracket:
                balanced_string += stacked
                return False
            elif stacked != close_brackets:
                balanced_string += bracket
                return True

            if stack[closed_bracket_position] in open_brackets:
                balanced_string += stack[closed_bracket_position]
            elif open_bracket in close_brackets:
                balanced_string += open_brackets

        print("balanced_string: ", balanced_string)

        print("stack_list: {}".format(stack))

    return not len(stack)


def is_bracket_closed(bracket):
    is_closed = False
    brackets_closed = [')', ']', '}']

    if bracket in brackets_closed:
        is_closed = True
    return is_closed


def is_bracket_open(bracket):
    is_open = False
    brackets_open = ['(', '[', '{']

    if bracket in brackets_open:
        is_open = True
    return is_open


def braces(values):
    response = []
    for string in values:
        if is_balanced(string):
            response.append(True)
        else:
            response.append(False)

    return response


if __name__ == '__main__':
    # samples1 = "{}[]()"
    samples2 = "{[}]}"
    # sample3 = "{[}]}]]]]"
    # samples = [samples1, samples2, sample3]
    samples = [samples2]

    print(braces(samples))

    # input_data = ""
    # output_data = ""
    # print(parenthesis_balancer(input_data))

    # input_data = "()"
    # output_data = "()"
    # print(parenthesis_balancer(input_data))

    # input_data = "()[]{}"
    # output_data = "()[]{}"
    # print(parenthesis_balancer(input_data))

    # input_data = "([{"
    # output_data = "([{}])"
    # print(parenthesis_balancer(input_data))
