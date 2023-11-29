"""100032587"""
import sys


def main() -> int:
    result: int = 0
    actions: int = 0
    robots_weight_list: list[int] = sorted([int(x) for x in
                                            sys.stdin.readline().
                                            rstrip().split(' ')])
    limit: int = int(sys.stdin.readline().rstrip())
    left_pointer: int = 0
    right_poiner: int = len(robots_weight_list) - 1
    while left_pointer < right_poiner:
        pointer_sum: int = (robots_weight_list[left_pointer] +
                            robots_weight_list[right_poiner])
        if pointer_sum == limit:
            result += 1
            left_pointer += 1
            right_poiner -= 1
            actions += 2
        elif pointer_sum > limit:
            result += 1
            right_poiner -= 1
            actions += 1
        else:
            result += 1
            left_pointer += 1
            right_poiner -= 1
            actions += 2
    if actions < len(robots_weight_list):
        result += 1
    return result


if __name__ == '__main__':
    main()
