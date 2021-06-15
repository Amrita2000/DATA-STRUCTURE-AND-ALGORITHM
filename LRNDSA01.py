try:
	while True:
		user_input = int(input())
		if(user_input!=42):
			print(user_input)
		else:
			break
except EOFError:
	pass
