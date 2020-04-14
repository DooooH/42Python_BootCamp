# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dohkim <dohkim@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 18:23:06 by dohkim            #+#    #+#              #
#    Updated: 2020/04/13 19:05:18 by dohkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
	print("ERROR")
	sys.exit(0)
if sys.argv[1].isdigit():
	if int(sys.argv[1]) == 0:
		print("I'm Zero.")
	elif int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	elif int(sys.argv[1]) % 2 == 1:
		print("I'm Odd.")
else :
	print("ERROR")