"""100032587"""

import sys


def robots_and_platform(robots_list: list[int],
                        limit: int) -> int:
    result: int = 0
    actions: int = 0
    left_pointer: int = 0
    right_poiner: int = len(robots_list) - 1
    while left_pointer < right_poiner:
        pointer_sum: int = (robots_list[left_pointer] +
                            robots_list[right_poiner])
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
    if actions < len(robots_list):
        result += 1
    return result


if __name__ == '__main__':
    robots_weight_list: list[int] = [int(robot_weight) for robot_weight in
                                     sys.stdin.readline().
                                     rstrip().split(' ')]
    robots_weight_list.sort()
    limit: int = int(sys.stdin.readline().rstrip())
    robots_and_platform(robots_weight_list, limit)
