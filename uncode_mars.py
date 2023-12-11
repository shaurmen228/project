"""102608947"""
import sys
import string


def uncoding_mars(encrypted_string: str) -> str:
    stack, temporary_num, temporary_line = [], 0, ''

    for symbol in encrypted_string:
        if symbol == '[':
            stack.append((temporary_line, temporary_num))
            temporary_num, temporary_line = 0, ''
        elif symbol == ']':
            now_line, now_factor = stack.pop()
            temporary_line = now_line + now_factor * temporary_line
        elif symbol in string.ascii_letters:
            temporary_line += symbol
        else:
            temporary_num = temporary_num * 10 + int(symbol)

    return temporary_line


if __name__ == '__main__':
    code: str = sys.stdin.readline().rstrip()
    print(uncoding_mars(code))
