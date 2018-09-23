from helpers import alphabet_position, rotate_character


def vigenere_encrypt(text, key):
    checker = 'abcdefghijklmnopqrstuvwxyz'

    key_number = []
    new_message = ''

    for each_letter in list(key):
        key_number.append(alphabet_position(each_letter.lower()))

    key = 0
    for each_char in list(text):
        if each_char.lower() not in checker:
            new_message += each_char.lower()

        else:

            new_message += rotate_character(each_char, key_number[key])
            key += 1
            if key == len(key_number):
                key = 0

    return new_message


def main():
    from sys import argv, exit

    message = input('Type a messsage to encrypt : ')
    try:
        if len(argv) >= 2:
            key_word = argv[1]
            if key_word.isalpha() is False:
                key_word = input(
                    '''
                    Please use a key word that has no
                    numbers/spaces/special characters
                    the vigenere cypher :
                    ''')
        else:
            key_word = input('What is your key word? ')
            if key_word.isalpha() is False:
                key_word = input(
                    '''
                    Please use a key word that has no
                    numbers/spaces/special characters
                    for the vigenere cypher :
                    ''')
    except ValueError:
        print('Woops you did not use a word please try again!')
        exit()

    if len(key_word) <= 1:
        key_word = input('Please use a word that is atleast 2 characters long :')

    print(vigenere_encrypt(message, key_word))


if __name__ == '__main__':
    main()
