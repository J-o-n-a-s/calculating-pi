def calc(number: int, value: float, next: int) -> float:
    if number % 2 != 0:
        return [value + (4 / next), next + 2]
    else:
        return [value - (4 / next), next + 2]
    

next: int = 1
result: float = 0
i: int = 1

while True:
    result, next = calc(i, result, next)

    if i < 100000000:
        i += 1
    else:
        break
    
    
print(result, i * 2)
