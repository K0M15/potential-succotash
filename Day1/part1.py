from set import data

def find_distance(set_one:list[int], set_two:list[int]):
    result = 0
    for i in range(len(set_one)):
        result += abs(set_one[i] - set_two[i])
    return result

if __name__ == "__main__":
    set_one = [x[0] for x in data]
    set_two = [x[1] for x in data]

    set_one.sort()
    set_two.sort()
    print(find_distance(set_one, set_two))