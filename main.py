# Mail Merging.

letter = open('./Input/Letters/starting_letter.txt')
letter = letter.read()
# print(letter)

name_file = open('./Input/Names/invited_names.txt')
names = name_file.readlines(0)
print(names)

for i in names:
    txt = i.strip("\n")
    file = open(f'./Output/ReadyToSend/Letter_to_{txt}.txt', mode='w')
    x = letter.replace('[name]', txt)
    file.write(x)
    file.close()


