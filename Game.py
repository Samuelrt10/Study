import random 
import os 

def run():
    
    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    DB = [
        "televisor",
        "programacion",
        "comer",
        "correr"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
       os.system("clear") 
       for charater in spaces:
           print(charater, end=" ")        
        print(images[attemps])
        letter = input("elige una letra")

        found = False
        for idx, charater in enumerate(word):
           if charater == letter:
               spaces[idx] = letter
               found = True

        if not found:
            attemps-= 1

        if "_" not in spaces:
            os.system("clear")
            print("ganaste")
            break
            input()
        
        if attemps == 0:
            os.system("clear")
            print("perdiste")
            break
            input()

if __name__ == "__main__":
    run()
