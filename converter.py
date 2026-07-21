from morse import Morse


morseFunc = Morse()

class Converter():
    def __init__(self, word):
        self.morse_dict = morseFunc.retorno()
        self.word = word
        self.listaMorsed = []
        self.letter_dict = []
            
    def transformToMorse(self):
        listaWord = [letter for letter in self.word]
        if " " in listaWord:
            for letter in listaWord:
                if letter in self.morse_dict.keys():
                    self.letter_dict.append(letter)
                    self.listaMorsed.append(self.morse_dict[letter])
                else:
                    self.letter_dict.append(letter)
                    self.listaMorsed.append(" ")
            return [self.letter_dict,self.listaMorsed]
        else:
            for letter in listaWord:
                if letter in self.morse_dict.keys():
                    self.letter_dict.append(letter)
                    self.listaMorsed.append(self.morse_dict[letter])
            return [self.letter_dict,self.listaMorsed]


    