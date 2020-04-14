# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dohkim <dohkim@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 17:30:54 by dohkim            #+#    #+#              #
#    Updated: 2020/04/13 18:22:03 by dohkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = len(sys.argv) - 1
while i > 0:
	s = sys.argv[i].swapcase()
	if (i != 1):
		print(''.join(reversed(s)), end='')
		print (' ', end='')
	else:
		print(''.join(reversed(s)))
	i -= 1