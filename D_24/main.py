""" with open('text_note.txt', mode='r') as file:
    content = file.read()
    print(content) """

with open('text_note2.txt', mode='w') as file:
    file.write('Replace text.')
