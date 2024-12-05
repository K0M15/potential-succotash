from io import TextIOWrapper

def parseUpdate(line:str):
    return [int(x) for x in line.split(',')]

def parseRule(line:str):
    return [int(x) for x in line.split('|')]

def parseFile(file:TextIOWrapper):
    rules = []
    updates = []
    for line in file:
        if line[0] == '\n':
            break
        rules.append(parseRule(line))
    for line in file:
        updates.append(parseUpdate(line))
    return [rules, updates]

def checkUpdate(update:list[int], rules:list[list[int]]):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                print(f"Rule {rules.index(rule)}: {update} = {rule}")
                return 0
    return 1

if __name__ == "__main__":
    file = open("input.txt")
    [rules, updates] = parseFile(file)
    file.close()
    amount = 0
    for update in updates:
        if checkUpdate(update, rules) == 1:
            amount += update[int(len(update)/2)]
    print(f"Total Amount = {amount}")

