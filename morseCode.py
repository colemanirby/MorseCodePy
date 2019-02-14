import time

from gpiozero import LED

# Morse Alphabet

MorseAlphabet = {

    'A': ['.', '-'],

    'B': ['-', '.', '.', '.'],

    'C': ['-', '.', '-', '.'],

    'D': ['-', '.', '.'],

    'E': ['.'],

    'F': ['.', '.', '-', '.'],

    'G': ['-', '-', '.'],

    'H': ['.', '.', '.', '.'],

    'I': ['.', '.'],

    'J': ['.', '-', '-', '-'],

    'K': ['-', '.', '-'],

    'L': ['.', '-', '.', '.'],

    'M': ['-', '-'],

    'N': ['-', '.'],

    'O': ['-', '-', '-'],

    'P': ['.', '-', '-', '.'],

    'Q': ['-', '-', '.', '-'],

    'R': ['.', '-', '.'],

    'S': ['.', '.', '.'],

    'T': ['-'],

    'U': ['.', '.', '-'],

    'V': ['.', '.', '.', '-'],

    'W': ['.', '-', '-'],

    'X': ['-', '.', '.', '-'],

    'Y': ['-', '.', '-', '-'],

    'Z': ['-', '-', '.', '.']

}
led = LED(17)

delayBetweenDashesAndDots = 0.25

delayBetweenLetters = 0.5

delayBetweenWords = 1

delayForDot = 0.10

delayForDash = 0.25


def main():
    # wait for user input

    # User input maps should take words and make NxY maps

    # how hello world would look:

    # ['h', 'e', 'l', 'l', 'o', '_', 'w', 'o', 'r', 'l', 'd']

    userInput = input("Type What you want to translate: ")

    userInputArray = userInputToArray(userInput)

    blinkMorseCode(userInputArray)


def blinkMorseCode(userInputArray):
    for letter in userInputArray:

        if letter is '_':

            time.sleep(delayBetweenWords)

            # print("  ", end="")

        else:

            blinkMorseCodeForLetter(letter)

            time.sleep(delayBetweenLetters)


def blinkMorseCodeForLetter(letter):
    letterMorse = getLetterMorse(letter)

    for dashOrDot in letterMorse:
        if dashOrDot is '.':
            led.on()

            time.sleep(delayForDot)

            led.off()

        if dashOrDot is '-':
            led.on()

            time.sleep(delayForDash)

            led.off()

        time.sleep(delayBetweenDashesAndDots)

        # print(dashOrDot, end="")
        # 
        # print("", end=" ")


def userInputToArray(userInput):
    userInputArray = []

    for letter in userInput:

        if letter == ' ':

            userInputArray.append('_')

        else:

            userInputArray.append(letter)

    return userInputArray


def getLetterMorse(letter):
    return MorseAlphabet[letter.upper()]


if __name__ == '__main__':
    main()