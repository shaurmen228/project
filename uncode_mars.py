"""102538247"""
import sys


def uncoding_mars(encrypted_string) -> str:
    stack: list = []
    temporary_num: int = 0
    temporary_str: str = ''

    for symbol in encrypted_string:
        if symbol == '[':
            stack.append(temporary_str)
            stack.append(temporary_num)
            temporary_num = 0
            temporary_str = ''
        elif symbol == ']':
            now_factor: int = stack.pop()
            now_string: str = stack.pop()
            temporary_str = now_string + now_factor * temporary_str
        elif symbol.isdigit():
            temporary_num = temporary_num * 10 + int(symbol)
        else:
            temporary_str += symbol

    return temporary_str


if __name__ == '__main__':
    code: str = sys.stdin.readline().rstrip()
    print(uncoding_mars(code))
