counter = int(input())
answer = ""

for i in range(counter):
	brackets = input()
	a = int(len(brackets)/2)

	left = []
	right = []
	for i in brackets:
		left.append(i)


	for i in left:
		if i == '(' or i == '{' or i == '[':
			a = left.pop()
			right.append(a)
		elif i == ')' or i == '}' or i == ']':
			break
		else:
			answer = answer + "NO "

	
	for i in range(len(left)):
		if left[i] == '[' and right[i] == ']':
			if i == len(left) - 1:
				answer = answer + "YES "
			else:
				continue
		elif left[i] == '{' and right[i] == '}':
			if i == len(left) - 1:
				answer = answer + "YES "
			else:
				continue
		elif left[i] == '(' and right[i] == ')':
			if i == len(left) - 1:
				answer = answer + "YES "
			else:
				continue

		else:
			answer = answer + "NO "



answers = answer.split()
for i in answers:
	print(i)