from part1 import parseFile, checkUpdate

def applyPatch(update, rules):
    while checkUpdate(update, rules) == 0:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                index1 = update.index(rule[0])
                index2 = update.index(rule[1])
                if index1 > index2:
                    buff = update[index1]
                    update[index1] = update[index2]
                    update[index2] = buff
    return update

if __name__ == "__main__":
    file = open("input.txt")
    [rules, updates] = parseFile(file)
    file.close()
    amount = 0
    for update in updates:
        if checkUpdate(update, rules) == 0:
            data = applyPatch(update, rules)
            print(data)
            amount += data[int(len(data)/2)]
    print(f"Total Amount = {amount}")
