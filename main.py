from chat import chatbot

count = 0
print('type `exit` to stop conversation')
print('')
while count >= 0:
	sentence = None
	if count==0:
		sentence = 'hi'
	else:
		sentence = input('you: ')

	if sentence == 'exit':
		print(f'bot: goodbye')
		break

	res = chatbot(sentence)
	print(f'bot: {res}')
	count += 1

# import torch
# print(torch.__version__)
