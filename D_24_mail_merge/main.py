def main():       
    with open('Input/Names/names.txt', mode='r') as names_file:
        names = names_file.readlines()      

    with open('Input/Letters/starting_letter.txt', mode='r') as letter_file:
        full_letter = letter_file.read()
        
    for name in names:
        new_letter = full_letter.replace('[name]', name.strip())
        with open(f'Output/ReadyToSend/Letter_for_{name.strip()}.txt', mode='w') as output:
            output.write(new_letter)


if __name__ == '__main__':
    main()