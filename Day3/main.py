
import re

def find_pattern(str:str) -> list[str]:
	return re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", str)

if __name__ == "__main__":
	data = find_pattern(open("input.txt").read())
	result = 0
	for elem in data:
		[part1, part2] = elem.split(',', 1)
		part1 = part1[4:]
		part2 = part2[:-1]
		result = result + int(part1)*int(part2)
	print(result)