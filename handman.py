from random import randrange

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


world = ["Перец", "Яблоко", "Морковь", "Уксус", "Глаз", "Двойка", "Вода"]
game = True

while game:
    error = 0
    guessed = 0
    total = 0
    secret_word_riddle = []
    word_riddle = world[randrange(len(world))]
    for i in range(len(word_riddle)):
        secret_word_riddle.append("*")

    while game:
        print(*secret_word_riddle)
        print("Угадайте слово!")
        char = input("Введите букву: ").lower()
        if char in secret_word_riddle or char.upper() in secret_word_riddle:
            print("Вы уже называли данную букву!")
            continue
        total = 0
        for i in range(len(word_riddle)):
            if word_riddle[i] == char.upper():
                secret_word_riddle[i] = word_riddle[i].upper()
                guessed += 1
                total += 1
            elif word_riddle[i] == char:
                secret_word_riddle[i] = word_riddle[i]
                guessed += 1
                total += 1
        if total == 0:
            error += 1
            print("Вы допустили ошибку и стали на шаг ближе к виселице!")
            print(f"Ваше количество ошибок {error} из 6")
            print(display_hangman(tries=6 - error))
            if error == 6:
                print("Вы были повешенны. Еще долго в воздухе ощущался запах поражения :)")
                break
        if guessed == len(word_riddle):
            print("Вы отгадали и спасли свою жизнь!")
            print(*secret_word_riddle, sep="")
            secret_word_riddle = []
            break
    game = input("Желаете продолжить игру? да / нет: ").lower() == "да"
    if game:
        continue
    else:
        print("В следующий раз возьмите веревку покрепче :)")