# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dohkim <dohkim@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 16:17:39 by dohkim            #+#    #+#              #
#    Updated: 2020/04/14 16:26:40 by dohkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

for i in languages.keys():
	print(f'{i} was created by {languages[i]}')