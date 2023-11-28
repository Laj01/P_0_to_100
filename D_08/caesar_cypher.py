from caesar_alphabet import alphabet


def main():
    direction = input('Type "encode" to encrypt or "decode" to decrypt text.\n')
    text = input('What is the text you would like to encode/decode?\n')
    shift = int(input('Shift number:\n'))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, direction=direction)

def caesar(start_text, shift_amount, direction):
    end_text = ''
    if direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)        
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f'The {direction}d text is: {end_text}')


if __name__ == '__main__':
    main()