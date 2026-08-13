# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ealiman <ealiman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/11 16:44:33 by ealiman           #+#    #+#              #
#    Updated: 2026/08/12 17:58:40 by ealiman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def command_quest() -> None:
    print("Program name:", sys.argv[0])
    if len(sys.argv[1:]) >= 1:
        print("Arguments received:", len(sys.argv[1:]))
        for i in range(1, len(sys.argv[1:])):
            print("Argument ", i, ": ", sys.argv[i], sep="")
    else:
        print("No arguments provided!")
    print("Total arguments:", len(sys.argv))


def main():
    print("=== Command Quest ===")
    command_quest()


if __name__ == "__main__":
    main()
