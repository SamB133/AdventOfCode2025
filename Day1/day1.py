# Advent of Code 2025 - Day 1

def get_lines_from_file(filename):
	with open(filename) as file:
		return file.readlines()

# Part 1 - Read how many times the dial stops on 0
def part_1(lines):
	number_of_zeros = 0
	curr_number = 50
	for line in lines:
		line = line.strip()
		steps = int(line[1:])
		if line.startswith('R'):
			curr_number = (curr_number + steps) % 100
		elif line.startswith('L'):
			curr_number = (curr_number - steps) % 100
		
		if curr_number == 0:
			number_of_zeros += 1
		
	print("Part 1:", number_of_zeros)

# Part 2 - Read how many times the dial goes past or stops on 0
def part_2(lines):
	number_of_zeros_or_past = 0
	curr_number = 50
	for line in lines:
		line = line.strip()
		steps = int(line[1:])
		if line.startswith('R'):
			number_of_zeros_or_past += (curr_number + steps) // 100
			curr_number = (curr_number + steps) % 100
		elif line.startswith('L'):
			if curr_number == 0:
				number_of_zeros_or_past += steps // 100
			elif steps >= curr_number:
				number_of_zeros_or_past += 1 + ((steps - curr_number) // 100)
			curr_number = (curr_number - steps) % 100
	print("Part 2:", number_of_zeros_or_past)

if __name__ == "__main__":
	lines = get_lines_from_file("input.txt")
	part_1(lines)
	part_2(lines)
