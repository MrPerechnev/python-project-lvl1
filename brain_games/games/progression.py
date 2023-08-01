from random import randint

task = 'What number is missing in the progression?'


def main():
    first_number = randint(1, 100)
    step = randint(1, 10)
    list = []
    for _ in range(10):
        first_number = first_number + step
        list.append(str(first_number))
    missing_number = randint(0, 9)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
