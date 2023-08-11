from random import randint

task = 'What number is missing in the progression?'


def get_progression():
    number_min = 1
    number_max = 100
    step_min = 1
    step_max = 10
    step = randint(step_min, step_max)
    list = []
    first_number = randint(number_min, number_max)
    for _ in range(10):
        first_number = first_number + step
        list.append(str(first_number))
    return list


def task_generation():
    number_start = 0
    number_end = 10
    list = get_progression()
    missing_number = randint(number_start, number_end - 1)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
