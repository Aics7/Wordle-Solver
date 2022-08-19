#variables
answers = []
word = ''
color = ''

#prints list of words
def printList(list_of_words):
    index = 1
    toPrint = '\nThe answer is one of these words \n'
    for word in list_of_words:
        toPrint += str(index) + ' ' + word + '\n'
        index+=1
    print(toPrint)

def start():
    #sets up list of possible solutions
    f1 = open('wordle-answers-alphabetical.txt','r')
    lines = f1.readlines()
    for line in lines:
        answers.append(line[:5])
    f1.close()

    #First print
    print('\n_____===_____Wordle Helper_____===_____')

start()
while word != 'exit' or colors != 'exit':
    # takes input and checks if user wants to exit or restart
    print('\n\nYou can type \"exit\" to exit or \"restart\" to restart')

    word = input('\nType word:\n').lower().strip()
    if word == 'restart':
        answers.clear()
        start()
        continue
    
    elif word == 'exit':
        break
    
    colors = input('\nType colors. Valid colors are b, y and g:\n').lower().strip()
    if colors == 'restart':
        answers.clear()
        start()
        continue
    elif colors == 'exit':
        break

    #check lengths
    if len(word) != 5 or len(colors) != 5:
        print('Invalid length for word or colors')
        continue
    
    #narrows down list of words based on word typed and colors
    for i in range(len(word)):
        letter = word[i]
        color = colors[i]
        if color == 'b':
            new_answers = []
            for answer in answers:
                if letter not in answer:
                    new_answers.append(answer)
            answers = new_answers
            
        elif color == 'y':
            new_answers = []
            for answer in answers:
                if letter in answer and answer[i] != letter:
                    new_answers.append(answer)
            answers = new_answers
            
        elif color == 'g':
            new_answers = []
            for answer in answers:
                if answer[i] == letter:
                    new_answers.append(answer)
            answers = new_answers
            
        else:
            print('\n\n\nInvalid color found! \nType \"restart\" if you want to restart \n\n')
    printList(answers)

print('***###___Thank you for using Wordle Helper___###***')
input('Press enter to exit')
