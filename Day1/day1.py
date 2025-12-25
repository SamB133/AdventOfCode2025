# Advent of Code 2025 - Day 1

# Part 1 - Read how many times the dial stops on 0
number_of_zeros = 0
curr_number = 50
dial_numbers = [i for i in range(100)]  # Dial numbers from 0 to 99

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		#print("Current line:", line.strip())
		if line.startswith('R'):
			steps = int(line[1:])
			curr_number = (curr_number + steps) % 100
		elif line.startswith('L'):
			steps = int(line[1:])
			curr_number = (curr_number - steps) % 100
		
		if curr_number == 0:
			number_of_zeros += 1
		
		#print("Updated curr_number:", curr_number)
print("Part 1:", number_of_zeros)

# Part 2 - Read how many times the dial goes past or stops on 0
number_of_zeros_or_past = 0
curr_number = 50

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		#print("Current line:", line.strip())
		if line.startswith('R'):
			steps = int(line[1:])
			for _ in range(steps):
				curr_number = (curr_number + 1) % 100
				if curr_number == 0:
					number_of_zeros_or_past += 1
		elif line.startswith('L'):
			steps = int(line[1:])
			for _ in range(steps):
				curr_number = (curr_number - 1) % 100
				if curr_number == 0:
					number_of_zeros_or_past += 1
		
		#print("Updated curr_number:", curr_number)
print("Part 2:", number_of_zeros_or_past)