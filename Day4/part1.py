
from io import TextIOWrapper

def count_in_str(str:str, target:str):
    amount = 0
    while len(str) >= len(target):
        if str.startswith(target):
            amount += 1
        str = str[1:]
    return amount

def read_to_list(file:TextIOWrapper):
    x = list[str]()
    for l in file:
        x.append(l)
    return x;

def rotate_clockwise(data:list[str]):
    result = list[str](["" for x in range(len(data))])
    for line in data:
        for i in range(len(line)):
            result[i] = "".join([result[i], line[i]])
    return result

def get_falling_words(data:list[str]):
    size = len(data)
    result = []
    for x in range(2 * size - 1):
        diagonal = []
        for row in range(max(0, x - size + 1), min(x + 1, size)):
            col = x - row
            diagonal.append(data[row][col])
        result.append("".join(diagonal))
    return result

def get_rising_words(data:list[str]):
    size = len(data)
    result = []
    for x in range(2 * size - 1):
        diagonal = []
        for row in range(max(0, x - size + 1), min(x + 1, size)):
            col = size - 1 - x + row
            diagonal.append(data[row][col])
        result.append("".join(diagonal))
    return result

if __name__ == "__main__":
    file = open("input.txt")
    data = read_to_list(file)
    file.close()
    total = 0
    target = "XMAS"
    # Horizontal
    for line in data:
        total += count_in_str(line, target)
        total += count_in_str(line, target[::-1])
    # Vertial
    drot = rotate_clockwise(data)
    print (drot)
    for line in drot:
        total += count_in_str(line, target)
        total += count_in_str(line, target[::-1])
    # Diagonal Rising
    dris = get_rising_words(data)
    for line in dris:
        total += count_in_str(line, target)
        total += count_in_str(line, target[::-1])
    # Diagonal Falling
    dfal = get_falling_words(data)
    for line in dfal:
        total += count_in_str(line, target)
        total += count_in_str(line, target[::-1])
    print(total)
