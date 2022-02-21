import random as r
from csvFile import edit_csv, more_stats

tableStr = """[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ]"""


def start():
    print("""\033[1;255mWelcome to my version of wordle!
Green means that the letter is in the word and in the correct spot;
Yellow means that the letter is in the word, but not in the correct spot;
Gray means the letter is not in the word.
Type \"stop\" to exit.
Have fun!\n""")
    player = input("\033[0mWho is playing? (First name)\n").title()
    game(player)


def get_word():
    with open("answerable_words.txt", "r") as file:
        word = list(map(str, file.read().split()))
        return r.choice(word)


def game(player):
    print("\033[0mStarting game:")
    table = list(tableStr)
    with open("allowed_words.txt", "r") as file:
        all_words = list(map(str, file.read().split()))
    with open("answerable_words.txt", "r") as file:
        all_words += list(map(str, file.read().split()))
    guesses = 6
    wordstr = get_word()
    word = list(wordstr)
    color = 0
    while guesses > 0:
        guessstr = input().lower()
        if guessstr == "stop" or guessstr == "quit" or guessstr == "exit":
            return
        guess = list(guessstr)
        times = 0
        if len(guess) == 5:
            if ''.join(guess) in all_words:
                for i in range(0, len(word)):
                    guesscnt = guessstr.count(guess[i])
                    wordcnt = wordstr.count(guess[i])
                    if guesscnt == 1:
                        times = 0
                    else:
                        try:
                            if guess[i] != guess[i - 1]:
                                times = 0
                        except IndexError:
                            times = 0
                    try:
                        if guess[i] == word[i]:
                            # Detects if the letter is in the word and in the correct spot. 32 is green, 37 is gray.
                            if guesscnt > 1:
                                if wordcnt > 1:
                                    if times < wordcnt:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;32m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 0
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                                        times += 1
                                    else:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;37m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 2
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                                else:
                                    if times == 0:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;32m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 0
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"

                                        times += 1
                                    else:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;37m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 2
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                            else:
                                table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;32m["
                                table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                color = 0
                                if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                    table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                else:
                                    table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                        elif guess[i] in word:
                            # Detects if the letter is in the word but not in the correct spot. 33 is yellow, 37 is gray.
                            if guesscnt > 1:
                                if wordcnt > 1:
                                    if times < wordcnt:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;33m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 1
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                                        times += 1
                                    else:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;37m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 2
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                                else:
                                    if times == 0:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;33m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 1
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                                        times += 1
                                    else:
                                        table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;37m["
                                        table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                        color = 2
                                        if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                        else:
                                            table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                            else:
                                table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;33m["
                                table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                                color = 1
                                if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                    table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                                else:
                                    table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                        else:
                            # Does this if the letter is not in the word. 37 is gray
                            table[(6 - guesses) * 20 + (i * 4)] = f"\033[1;37m["
                            table[(6 - guesses) * 20 + (i * 4) + 1] = guess[i]
                            color = 2
                            if (6 - guesses) * 20 + (i * 4) + 3 != 19 + (6 - guesses) * 20:
                                table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m "
                            else:
                                table[(6 - guesses) * 20 + (i * 4) + 3] = "\033[1;37m\n"
                    except IndexError:
                        if color == 0:
                            table[118] = "\033[1;32m]"
                        elif color == 1:
                            table[118] = "\033[1;33m]"
                        elif color == 3:
                            table[118] = "\033[1;37m]"
                print(''.join(table))
                if guess == word:
                    print("\033[0mYou got the word!\n")
                    edit_csv(player, 'True', 'False', str(7-guesses), wordstr)
                    choice = input("\033[0mDo you want to see more stats? (y/n)\n")
                    if choice == 'y':
                        print("Exit out of the bar graph program to continue.")
                        more_stats(player)
                        game(player)
                    else:
                        game(player)
                else:
                    guesses -= 1
            else:
                print("\033[0mWord not found.")
        else:
            print("\033[0mGuess has to be 5 characters.")
    print(f"\033[0mYou lost. The word was {wordstr}")
    edit_csv(player, 'False', 'True', 'NA', wordstr)
    choice = input("\033[0mDo you want to see more stats? (y/n)\n")
    if choice == 'y':
        print("Exit out of the bar graph program to continue.")
        more_stats(player)
        game(player)
    else:
        game(player)


start()
print("Program stopping.\nThanks for playing!")