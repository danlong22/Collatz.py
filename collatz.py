def collatz(uInput):
	print(uInput)
	#creates the Collatz sequence
	while uInput != 1:
		if uInput%2 ==0:
			uInput/=2
		else:
			uInput = (uInput*3)+1
		print(uInput)
	#prevents window from closing before the user can see the output
	input('Press Enter to exit.')

number = int(input('Please Enter an integer.\n'))
collatz(number)



