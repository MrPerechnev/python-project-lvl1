from random import randint
NUMBER_MIN = 1
NUMBER_MAX = 100
STEP_MIN = 1
STEP_MAX = 10
NUMBER_START = 0
NUMBER_END = 10
LENGTH = 10

TASK = 'What number is missing in the progression?'


def get_progression(first_number, length, step):
    list = []
    for _ in range(length):
        first_number = first_number + step
        list.append(str(first_number))
    return list


def generate():
    length = LENGTH
    step = randint(STEP_MIN, STEP_MAX)
    first_number = randint(NUMBER_MIN, NUMBER_MAX)
    list = get_progression(first_number, length, step)
    missing_number = randint(NUMBER_START, NUMBER_END - 1)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
