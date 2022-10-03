import sys
import requests
import os
import pathlib
import bs4  # pip install beautifulsoup4
import random


class Hangman():
    '''Hangman'''

    def __init__(self):
        '''init'''
        self.phrase = ''
        self.hidden_phrase = []
        self.used_letters = []
        self.web_phrases_list = []
        self.file_phrases_list = []
        self.number_of_tries = 5  # to do: metoda pytajaca o ilosc mozliwych bledow
        self.link = r'https://pl.wiktionary.org/wiki/Aneks:Przys%C5%82owia_polskie_-_A'
        self.myfile_path = os.path.join(pathlib.Path(
            __file__).parent.resolve(), "saved_phrases.txt")
        self.all_links = []

    def file_phrases(self):
        '''phrases from saved file'''
        with open(self.myfile_path, 'r', encoding='utf-8') as myfile:
            for line in myfile.readlines():
                line = line.upper()
                self.file_phrases_list.append(line)

    def get_phrase(self, source):
        '''get phrase'''
        if source == 'web' or source == 'all':
            self.get_links()
            self.website_phrase()
        if source == 'txt' or source == 'all':
            self.file_phrases()
        if source == 'web':
            self.phrase = random.choice(self.web_phrases_list)
        if source == 'txt':
            self.phrase = random.choice(self.file_phrases_list)
        if source == 'all':
            self.phrase = random.choice(
                self.file_phrases_list+self.web_phrases_list)

    def __get_web_content(self, web_address):
        '''get content of website'''
        r = requests.get(web_address)
        try:
            r.raise_for_status()
        except Exception as exc:
            print(f'There was a problem: {exc}')

        return bs4.BeautifulSoup(r.content, 'html.parser')

    def get_links(self):
        '''get links from first site'''
        soup = self.__get_web_content(self.link)
        alphabet_soup = soup.select('a')
        # loop to find every letter with link
        for letter in alphabet_soup[3:30]:
            self.all_links.append(self.link[:-1]+letter.getText())

    def website_phrase(self):
        '''phrase from website'''
        for address in self.all_links:
            soup = self.__get_web_content(address)
            li_soup = soup.find_all('li')
            phrase_soup = li_soup[:-40]
            for line in phrase_soup:
                self.web_phrases_list.append(line.getText().upper())

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

    def play(self, source):
        '''play'''
        self.get_phrase(source)
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
                print(f'Odkryte haslo to: {self.phrase}')
                break
            print(f'{self.hidden_phrase}')


if __name__ == '__main__':
    wisielec = Hangman()
    wisielec.play('all')
