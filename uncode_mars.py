"""102504902"""
import sys


def uncoding_mars(code):
    stack = []
    temporary_num = 0
    temporary_str = ''

    for symbol in code:
        if symbol == '[':
            stack.append(temporary_str)
            stack.append(temporary_num)
            temporary_num = 0
            temporary_str = ''
        elif symbol == ']':
            now_factor = stack.pop()
            now_string = stack.pop()
            temporary_str = now_string + now_factor * temporary_str
        elif symbol.isdigit():
            temporary_num = temporary_num * 10 + int(symbol)
        else:
            temporary_str += symbol

    return temporary_str


if __name__ == '__main__':
    code = sys.stdin.readline().rstrip()
    print(uncoding_mars(code))
