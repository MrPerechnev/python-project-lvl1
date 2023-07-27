import prompt


def start_game(game):
    index = 0
    attempts = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.task)
    while index < attempts:
        question, correct_answer = game.main()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
            index = index + 1
        elif user_answer != correct_answer:
            return f"{user_answer} is wrong answer ;(.\
 Correct answer was {correct_answer}.\nLet's try again, {name}!"
    return f"Congratulations, {name}!"
