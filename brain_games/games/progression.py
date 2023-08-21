from random import randint
NUMBER_MIN = 1
NUMBER_MAX = 100
STEP_MIN = 1
STEP_MAX = 10
NUMBER_START = 0
NUMBER_END = 10
LENGTH = 10

TASK = 'What number is missing in the progression?'


def get_progression(initial_term, length, common_difference):
    list = []
    for _ in range(length):
        initial_term = initial_term + common_difference
        list.append(str(initial_term))
    return list


def generate():
    length = LENGTH
    common_difference = randint(STEP_MIN, STEP_MAX)
    initial_term = randint(NUMBER_MIN, NUMBER_MAX)
    list = get_progression(initial_term, length, common_difference)
    missing_number = randint(NUMBER_START, NUMBER_END - 1)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
