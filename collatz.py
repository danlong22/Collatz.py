def collatz(uInput):
	#change the string returned by the input() function to an integer
	uInput = int(uInput)
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
#checks to make sure that the user input is valid
finished = False
while finished == False:
	number = input('Please Enter an integer.\n')
	try:
		collatz(number)
		break
	except:
		print('That is not an integer.')
		number = input('Please Enter an integer.\n')
		
		



