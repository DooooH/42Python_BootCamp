# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dohkim <dohkim@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 20:32:20 by dohkim            #+#    #+#              #
#    Updated: 2020/04/13 22:40:34 by dohkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(s="default"):
	upper = 0
	lower = 0
	punct = 0
	space = 0
	if s == "default":
		print("What is the text to analyse?")
		s = input()
	punctuations = (',','.','-','?','!',';',':','\'','"','[',']','{','}','(',')')
	for i in s:
		if i.islower():
			lower += 1
		elif i.isupper():
			upper += 1
		elif i == ' ':
			space += 1
		else :
			for j in punctuations:
				if j == i:
					punct += 1
					continue
	length = len(s)
	content = f'The text contains {length} characters:\n\n- {upper} upper letters\n\n- {lower} lower letters\n\n- {punct} punctuation marks\n\n- {space} spaces'
	print(content)