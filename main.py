def calc(p_number: int, p_value: float, p_next: int) -> list:
    if p_number % 2 != 0:
        return [p_value + (4 / p_next), p_next + 2]
    else:
        return [p_value - (4 / p_next), p_next + 2]


if __name__ == '__main__':
    next: int = 1
    result: float = 0
    i: int = 1

    while True:
        result, next = calc(i, result, next)

        if i < 1000000000:
            i += 1
        else:
            break

    print(result, i * 2)
