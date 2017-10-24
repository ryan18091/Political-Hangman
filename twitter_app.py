
from sys import exit
import string
import textwrap
from twitterAPItest import twitterAPImain


### Get rid of Emojies in word


# Html_file = open("/Users/ryan.erickson/PycharmProjects/Full-Stack/Twitter_App/library/Trump-Tweets.txt", 'w')
# Html_file.truncate()

infile = open('/Users/ryan.erickson/PycharmProjects/Full-Stack/Twitter_App/Trump-Tweets.txt', 'r')
lastLine = (list(infile)[-1])

alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '8', '9', '0']


word = [lastLine] #Gets list object from lastline
word = ','.join(word) # converts list object to str
# Following three functions get (word) into correct formatting for the game
word = word.lower()


word = word[:-1]  # I'm getting an unkown character at the end of the string that needs to be removed


translator = str.maketrans('', '', string.punctuation)  # removes puctuation and non letters/nums.
word = (word.translate(translator)) ### Need to remove emojies
print(word)

word_guess = []
# l = len(word)


#Algorithem for determining the number of turns based upon the length of the string
l = 1000

l = int(l/10)

if l >= 10:
    turns = 4
if l <=9 and l >=7:
    turns = 5
if l <=6 and l >=5:
    turns = 6
if l <=4 and l >=3:
    turns = 7
if l <=2:
    turns = 8


for char in word:
    if char == ' ':
        word_guess.append(' ')
    else:
        word_guess.append('_')

joined_word = (' '.join(word_guess))

joined_word = (textwrap.fill(joined_word, 30))
# print(joined_word)



from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def Landing_page():

    global turns
    global wrapped_word
    global joined_word
    global lastLine

    if request.method == 'GET':


        remaining_letters = textwrap.fill(', '.join(alpl), 52)
        #
        #
        # guess_phrase = joined_word


        # comp_word = ''.join(word_guess)  # creates an un-joined instance of the word to compare to the guess_word for a win

        # if comp_word == word:
        #     print('Win')
        #     return render_template('win.html')

        return render_template('twitter2.html', turns=turns, remaining_letters=remaining_letters)
        # return render_template('twitter2.html', remaining_letters=remaining_letters)


    elif request.method == 'POST':

        # message_line = ''
        #
        #
        # global politician
        # global politician_id
        #
        # politician = request.form['politician']
        #
        # from tweetdict import t_dict
        #
        # politician_id = t_dict[politician]
        #
        #
        # from twitterAPItest import twitterAPImain
        #
        # twitterAPImain()
        #
        # from twitterAPItest import i
        #
        # print(politician)
        #
        # print(politician_id)
        #
        # print(i)
        #
        # lastLine = i
        # word = [lastLine]  # Gets list object from lastline
        # word = ','.join(word)  # converts list object to str
        # # Following three functions get (word) into correct formatting for the game
        # word = word.lower()
        # word = word[:-1]  # I'm getting an unkown character at the end of the string that needs to be removed
        #
        # translator = str.maketrans('', '', string.punctuation)  # removes puctuation and non letters/nums.
        # word = (word.translate(translator))  ### Need to remove emojies
        #
        # word_guess = []
        # # l = len(word)
        #
        # # Algorithem for determining the number of turns based upon the length of the string
        # l = 1000
        #
        # l = int(l / 10)
        #
        # if l >= 10:
        #     turns = 4
        # if l <= 9 and l >= 7:
        #     turns = 5
        # if l <= 6 and l >= 5:
        #     turns = 6
        # if l <= 4 and l >= 3:
        #     turns = 7
        # if l <= 2:
        #     turns = 8
        #
        # for char in word:
        #     if char == ' ':
        #         word_guess.append(' ')
        #     else:
        #         word_guess.append('_')
        #
        # joined_word = (' '.join(word_guess))
        # print(joined_word)
        #
        # joined_word = ' '
        #
        # guess_head = 'The latest tweet from %r' % politician
        #
        # choice = request.form['Char_Choice']
        #
        # print(choice)
        #
        # if choice not in alpl:
        #     message_line = "That letter has already been chosen."
        #
        # if choice not in word:
        #     message_line = 'That choice is not in the phrase'
        #     turns = (turns - 1)
        #
        # for letter in range(len(word)):
        #     if choice == word[letter]:
        #         word_guess[letter] = choice
        #     elif ' ' == word[letter]:
        #         word_guess[letter] = ' '
        #
        # comp_word = ''.join(word_guess)  # creates an un-joined instance of the word to compare to the guess_word for a win
        #
        # print(lastLine)
        #
        # if comp_word == word:
        #     print('Win')
        #     return render_template('win.html', lastLine=lastLine)
        #
        # if choice in alpl:
        #     alpl.remove(choice)
        #
        # remaining_letters = textwrap.fill(', '.join(alpl), 52)
        #
        # guess_phrase = (' '.join(word_guess))
        # # guess_phrase = (textwrap.fill(joined_word, 30))



        guess_head = 'The Latest Tweet'
        message_line =' '

        # polititian = request.form['polititian']
        # print(polititian)
        # print(polititian)

        choice = request.form['Char_Choice']
        print(choice)


        if choice not in alpl:
            message_line = "That letter has already been chosen."

        if choice not in word:
            message_line = 'That choice is not in the phrase'
            turns = (turns - 1)

        for letter in range(len(word)):
            if choice == word[letter]:
                word_guess[letter] = choice
            elif ' ' == word[letter]:
                word_guess[letter] = ' '

        comp_word = ''.join(word_guess)  # creates an un-joined instance of the word to compare to the guess_word for a win


        if comp_word == word:
            print('Win')
            return render_template('win.html', lastLine=lastLine)

        if choice in alpl:
            alpl.remove(choice)

        # guess_phrase = (textwrap.fill(joined_word, 30))
        guess_phrase = (' '.join(word_guess))

        remaining_letters = textwrap.fill(', '.join(alpl), 52)

        print(guess_phrase)






        if turns == 0:
            message_line = 'GAME OVER'

        return render_template('twitter2.html', guess_head=guess_head, remaining_letters=remaining_letters,turns=turns,
                               message_line=message_line, guess_phrase=guess_phrase, choice=choice)

@app.route('/Hangman', methods=['POST','GET'])
def Hangman():
    if request.method == 'GET':


@app.route('/About', methods=['GET'])
def About():
    if request.method == 'GET':
        return render_template('About.html')
