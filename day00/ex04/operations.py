# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dohkim <dohkim@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 22:44:53 by dohkim            #+#    #+#              #
#    Updated: 2020/04/13 23:40:10 by dohkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0 :
	print("InputError: only numbers\n")
if len(sys.argv) != 3 or sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0:
	print(f'Usage: python operations.py <number1> <number2>\n\
Example:\n\
	python operations.py 10 3')
else :
	sum = int(sys.argv[1]) + int(sys.argv[2])
	sub = abs(int(sys.argv[1]) - int(sys.argv[2]))
	product = int(sys.argv[1]) * int(sys.argv[2])
	print(f'Sum:\t\t{sum}')
	print(f'Difference:\t{sub}')
	print(f'Product:\t{product}')
	try :
		quotient = int(sys.argv[1]) / int(sys.argv[2])
		print(f'Quotient:\t{quotient}')
		remainder = int(sys.argv[1]) % int(sys.argv[2])
		print(f'Remainder:\t{remainder}')
	except :
		print("Quotient:\tERROR (div by zero)")
		print("Remainder:\tERROR (div by zero)")
