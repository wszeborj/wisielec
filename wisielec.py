import sys

number_of_tries = 5
word = 'wszebor'
hidden_word = ['_' for _ in range(len(word))]
used_letters = []


while True:
    letter_found = False
    letter = input('podaj literke: ')
    # print(f'wybrales literke {letter}')
    for i in range(len(word)):
        if letter == word[i]:
            letter_found = True
            print('Dobrze! kontynuuj ;)')
            hidden_word[i] = word[i]
    
    if not letter_found:
        number_of_tries-= 1
        print(f'Nie zgadles, zostalo ci {number_of_tries} prob')
    
    if number_of_tries==0:
        print('Niepoprawnie zgadles literke zbyt wiele razy. PRZEGRALES')
        break

    if '_' not in hidden_word:
        print('BRAWO! WYGRALES!')
        break
    
    print(hidden_word)

sys.exit(0)