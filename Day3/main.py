
import re

def find_pattern(str:str) -> list[str]:
	return re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))", str)

if __name__ == "__main__":
	data = find_pattern(open("input.txt").read())
	result = 0
	enabled = True
	print(data)
	for elem in data:
		if elem.startswith('mul') and enabled:
			[part1, part2] = elem.split(',', 1)
			part1 = part1[4:]
			part2 = part2[:-1]
			result = result + int(part1)*int(part2)
		elif elem.startswith('do()'):
			enabled = True
		elif elem.startswith("don't()"):
			enabled = False
		else:
			print(f"Encountered {elem}")
	print(result)