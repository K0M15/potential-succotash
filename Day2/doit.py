from sys import argv

def process_dampener(elem:list[int]):
	asc = elem[0] < elem [1]
	has_problem = 0
	for i in range(len(elem)-1):
		if asc:
			if elem[i] < elem[i + 1] and elem[i + 1] - elem[i] < 4:
				continue
			elif has_problem == 0:
				has_problem += 1
				continue
			return 0;
		else:
			if elem[i] > elem[i + 1] and elem[i] - elem[i + 1] < 4:
				continue
			elif has_problem == 0:
				has_problem += 1
				continue
			return 0;
	return 1

def process(elem:list[int]):
	asc = elem[0] < elem [1]
	for i in range(len(elem)-1):
		if asc:
			if elem[i] < elem[i + 1] and elem[i + 1] - elem[i] < 4:
				continue
			return 0;
		else:
			if elem[i] > elem[i + 1] and elem[i] - elem[i + 1] < 4:
				continue
			return 0;
	return 1

if __name__ == "__main__":
	# if len(argv) != 2:
	# 	print("Wrong args")
	# 	exit()
	# file = open(argv[1], "r")
	file = open("Day2/input.txt", "r")
	result = 0;
	result_damp = 0;
	total_count = 0;
	for line in file:
		line = [int(x) for x in line.split(" ")]
		result += process(line)
		result_damp += process_dampener(line)
		total_count += 1
	print(f"Good Reports {result}/{total_count}")
	print(f"Dampend Reports {result_damp}/{total_count}")