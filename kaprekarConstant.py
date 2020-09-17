def kaprekar(n):
	if n == 0:
		return -1 
	counter = 0
	while n != 6174:
		counter += 1
		asc, desc = 0, 0
		digits = []

		for i in range(4):
			digits.append(n % 10)
			n //= 10

		digits.sort()

		for i in range(len(digits)):
			asc = asc * 10 + digits[i]

		digits.sort(reverse = True)

		for i in range(len(digits)):
			desc = desc * 10 + digits[i]

		while len(digits) < 4:
			digits.append(0)
			desc *= 10

		diff = abs(desc - asc)

		if diff == 6174:
			return counter

		n = diff

	return 0

n = int(input())
print(kaprekar(n))