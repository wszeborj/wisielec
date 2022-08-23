import sys
import requests


class Hangman():
    '''Hangman'''

    def __init__(self):
        '''init'''
        self.phrase = ''
        self.hidden_phrase = []
        self.used_letters = []
        self.number_of_tries = 5  # to do: metoda pytajaca o ilosc mozliwych bledow

    def get_phrase(self):
        '''get phrase'''
        self.phrase = 'Ala ma kota'
        self.phrase = self.phrase.upper()
    
    def website_phrase(self):
        '''phrase from website'''
        r = requests.get(r'https://pl.wiktionary.org/wiki/Aneks:Przys%C5%82owia_polskie_-_A')
        try:
            r.raise_for_status()
        except Exception as exc:
            print(f'There was a problem: {exc}')
        
        # with open('web_content.txt', 'w') as web_file:
        #     for chunk in r.iter_content(100000):
        #         web_file.write(str(chunk))


    # def prepare_phrase(self):
    #     '''preparing phrase'''
    #     return self.phrase.upper()

    def get_hidden_phrase(self):
        '''get hidden phrase'''
        for x in list(self.phrase):
            if x.isalpha():
                self.hidden_phrase.append('_')
            else:
                self.hidden_phrase.append(x)

    def get_letter(self) -> str:
        '''get letter from user'''
        while True:
            letter = input('podaj literke: ')
            if letter.isalpha():
                letter = letter.upper()
                self.used_letters.append(letter)
                return letter
            else:
                print('blad! sprobuj jeszcze raz.')

    def play(self):
        '''play'''
        self.get_phrase()
        self.get_hidden_phrase()

        while True:
            flag_letter_found = False

            user_letter = self.get_letter()

            for i in range(len(self.phrase)):
                if user_letter == self.phrase[i]:
                    flag_letter_found = True
                    self.hidden_phrase[i] = user_letter

            if flag_letter_found is False:
                self.number_of_tries -= 1
                print(f'Nie zgadles, zostalo ci {self.number_of_tries} prob')

            if self.number_of_tries == 0:
                print('Niepoprawnie zgadles literke zbyt wiele razy. PRZEGRALES')
                print(f'Haslo ktorego szukales to: {self.phrase}')
                break

            if '_' not in self.hidden_phrase:
                print('BRAWO! WYGRALES!')
                print('Odkryte haslo to: {self.phrase}')
                break
            print(f'{self.hidden_phrase}')


    # def find_phrase(self) -> str:
    #     '''find phrase'''
    #     r = requests.get(r'https://pl.wikiquote.org/wiki/Przys%C5%82owia_polskie')
    #     if r.status_code == 200:
    #         try:
    #             p = r.json()
    #         except json.decoder.JSONDecodeError:
    #             print('Niepoprawny format')
    #         else:
    #             print(p)
    #     else:
    #         print(f'Response of http: {r.status_code}')
if __name__ == '__main__':
    wisielec = Hangman()
    wisielec.play()
    # wisielec.website_phrase()
