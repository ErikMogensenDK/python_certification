def arithmetic_arranger(problems, display_answers=False):

	if len(problems) > 5:
		return 'Error: Too many problems.'

	if invalid_operator(problems):
		return "Error: Operator must be '+' or '-'."

	if too_many_digits(problems):
		return 'Error: Numbers cannot be more than four digits.'

	# check if all characters are numbers
	if non_int_character_in_input(problems):
		return 'Error: Numbers must only contain digits.'

	# intialize arrays for variables used later
	prints_list, lengths = create_arrays(problems)
	
	# initialize lines
	arranged_problems = arrange_problems(prints_list)
	if display_answers:
		arranged_problems = add_answers(problems, arranged_problems, lengths)

	#print(arranged_problems)
	return arranged_problems

def make_indentation(lengths):
	indentations = []
	maximum = max(lengths)
	indentations.append(' ' *(maximum - lengths[0] + 2))
	indentations.append(' ' *(maximum - lengths[2] + 1))
	#indentations.append(' ' * (maximum + 2))
	indentations.append('-' * (maximum + 2))
	return indentations

def make_prints(indents, split_problem):
	prints = []
	prints.append(indents[0] + split_problem[0])
	prints.append(split_problem[1] + indents[1] + split_problem[2])	
	prints.append(indents[2])
	return prints

def calc_diff(problem):
	split_problem = problem.split()
	int_1 = int(split_problem[0])
	int_2 = int(split_problem[2])
	if split_problem[1] == '+':
		answer = int_1 + int_2
	else:
		answer = int_1 - int_2
	return str(answer)

def get_lengths(split_problem):
	lengths = [len(elem) for elem in split_problem]
	return lengths

def invalid_operator(problems):
	for problem in problems:
		split_problem = problem.split()
		operator = split_problem[1]
		if operator != '+' and operator != '-':
			return True

	return False

def too_many_digits(problems):
	for problem in problems:
		lengths = get_lengths(problem.split())
		if max(lengths) > 4:
			return True
	return False

def non_int_character_in_input(problems):
	for problem in problems:
		split_problem = problem.split()
		for char in split_problem[0]:
			if not char.isnumeric():
				return True
		for char in split_problem[2]:
			if not char.isnumeric():
				return True
	return False	

def arrange_problems(prints_list):
	line_1 = ''
	line_2 = ''
	line_3 = ''
	space = '    '
	for i in range(len(prints_list)):
		if i == (len(prints_list)-1):
			space = ''
		line_1 += str(prints_list[i][0]) + space  
		line_2 += str(prints_list[i][1]) + space 
		line_3 += str(prints_list[i][2]) + space 
	arranged_problems = f'{line_1}\n{line_2}\n{line_3}'
	return arranged_problems

def add_answers(problems, arranged_problems, lengths):
	answer = ''
	for i in range(len(problems)): 
		temp_answer = calc_diff(problems[i])
		maximum = max(lengths[i])
		indent = ' ' * (maximum - len(temp_answer) + 2)
		if i != (len(problems) - 1):
			answer += f'{indent}{temp_answer}    '
		else:
			answer += f'{indent}{temp_answer}'
	arranged_problems = f'{arranged_problems}\n{answer}'
	return arranged_problems

def create_arrays(problems):
	prints_list = []
	lengths = []
	for problem in problems:
		split_problem = problem.split()
		length = get_lengths(split_problem)
		lengths.append(length)
		indents = make_indentation(length)
		prints = make_prints(indents, split_problem)
		prints_list.append(prints)
	return prints_list, lengths
	