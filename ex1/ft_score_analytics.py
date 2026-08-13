# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ealiman <ealiman@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/12 17:53:32 by ealiman           #+#    #+#              #
#    Updated: 2026/08/13 13:23:15 by ealiman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class ErrorValue(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class ErrorInput(Exception):
    def __init__(self, message=None):
        super().__init__(message)


def valid_score(score: str) -> None:
    try:
        score = int(score)
    except:
        raise ErrorValue("Invalid parameter: ")


def parse_scores() -> list:
    score_list = sys.argv[1:]
    for score in score_list:
        try:
            valid_score(score)
        except ErrorValue as e:
            print(e, "'", score, "'", sep="")
    return score_list


def error_managment() -> None:
    scores = parse_scores()
    if len(scores) < 5:
        raise ErrorInput("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")


def ft_score_analytics() -> None:
    try:
        error_managment()
        score_list = []
        for score in sys.argv[1:]:
            score = int(score)
            score_list.append(score)
        print("Scores processed:", score_list)
        print("Total players:", len(score_list))
        avg = sum(score_list) / len(score_list)
        print("Average score:", avg)
        print("High score:", max(score_list))
        print("Low score:", min(score_list))
        print("Score range:", (max(score_list) - (min(score_list))))
    except ErrorInput as e:
        print(e)


def main():
    print("=== Player Score Analytics ===")
    ft_score_analytics()


if __name__ == "__main__":
    main()