def main():       
    with open('Input/Names/names.txt', mode='r') as names_file:
        names = names_file.readlines()      

    with open('Input/Letters/starting_letter.txt', mode='r') as letter_file:
        lines = letter_file.readlines()
        
    for name in names:
        for line in lines:
            new_line = line.replace('[name]', name.strip())            
            with open(f'Output/ReadyToSend/Letter_for_{name.strip()}.txt', mode='a') as output:
                output.write(new_line)


if __name__ == '__main__':
    main()