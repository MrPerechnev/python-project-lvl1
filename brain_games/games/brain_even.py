#!/usr/bin/env python3
from random import randint
from brain_games.the_same_logic import start_game


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    start_game()
    question = randint(1, 100)
    correct_answer = even(question)
    return question, correct_answer


if __name__ == '__main__':
    main()
