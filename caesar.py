from helpers import rotate_character


def caesar_encrypt(text, rot):
    checker = 'abcdefghijklmnopqrstuvwxyz'

    new_message = ''

    for each_char in list(text):
        if each_char.lower() not in checker:
            new_message += each_char.lower()

        else:
            each_char in list(text)
            new_message += rotate_character(each_char, rot)

    return new_message


def main():
    from sys import argv, exit

    message = input('Type a messsage to encrypt : ')
    try:
        if len(argv) >= 2:
            rotation_by = int(argv[1])
        else:
            rotation_by = int(input('Rotate by how many? '))
    except ValueError:
        print('Woops you did not put a number for the rotation try again!!')
        exit()
    print(caesar_encrypt(message, rotation_by))


if __name__ == '__main__':
    main()
