def is_uppercase(new, old):

    if old.istitle() is True:
        return new.upper()
    else:
        return new.lower()


def alphabet_position(letter):
    numeric_position = 'abcdefghijklmnopqrstuvwxyz'

    if letter.lower() in numeric_position:
        return numeric_position.index(letter)


def rotate_character(char, rot):
    new_letter = 'abcdefghijklmnopqrstuvwxyz'

    new_position = alphabet_position(char.lower()) + rot

    if new_position >= 26:
        new_position = new_position % 26
        new_char = new_letter[new_position]
        return is_uppercase(new_char, char)
    else:
        new_char = new_letter[new_position]
        return is_uppercase(new_char, char)
