import random
import os
q = 0
# Deck of cards
class Cards_Values():
    def __init__(self):
        self.deck = []
        card_list = ['♣', '♥', '♠', '♦']
        self.card_list = card_list
        A = 1 or 11
        King = 10
        Queen = 10
        Jack = 10
        card_numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.card_numbers = card_numbers
        for num in self.card_numbers:
            for cards in self.card_list:
                self.deck.append(str(num) + ' of ' + str(cards))
class Display():


    def __init__(self):
        i = random.randint(0,51)
        self.actual_card = full_deck[i]

    def card_num(self):
        self.pre_number_value = []
        self.number_value = []
        for num in full_deck:
            for char in num:
                if char in ['1','2','3','4','5','6','7','8','9','A','J','Q','K']:
                    self.pre_number_value.append(char)
        for charec in self.pre_number_value:
            numbers = charec.replace('1','10')
            self.number_value.append(numbers)

    def card_symbol(self):
            self.card_symbols = []
            for symbol in full_deck:
                for char in symbol:
                    if char in ['♣', '♥', '♠', '♦']:
                        self.card_symbols.append(char)

    def display_deck(self):
        print(' ----------- ')
        print('|           |')
        print('| -----------')
        print('||           |')
        print('|| -----------')
        print('|||           |')
        print(' ||           |')
        print(' ||    deck   | ')
        print('  |           |')
        print('  |           |')
        print('   ----------- ')




    def player_board(self):
        if self.number_value[q] == '10':
            string = ' ----------- '
            string1 = '|  '+self.card_symbols[q]+'        |'
            string2 = '|           |'
            string3 = '|    '+self.number_value[q] + '     |'
            string4 = '|           |'
            string5 = '|           |'
            string6 = ' ----------- '
        else:
            string = ' ----------- '
            string1 = '|  '+self.card_symbols[q]+'        |'
            string2 = '|           |'
            string3 = '|    '+self.number_value[q] + '      |'
            string4 = '|           |'
            string5 = '|           |'
            string6 = ' ----------- '

        if self.number_value[q+2] == '10':
            strin = '\t ----------- '
            strin1 = '\t|  '+self.card_symbols[q+2]+'        |'
            strin2 = '\t|           |'
            strin3 = '\t|    '+self.number_value[q+2]+'     |'
            strin4 = '\t|           |'
            strin5 = '\t|           |'
            strin6 = '\t ----------- '
        else:
            strin = '\t ----------- '
            strin1 = '\t|  '+self.card_symbols[q+2]+'        |'
            strin2 = '\t|           |'
            strin3 = '\t|    '+self.number_value[q+2]+'      |'
            strin4 = '\t|           |'
            strin5 = '\t|           |'
            strin6 = '\t ----------- '


        fin_string = string + strin
        fin_string1 = string1 + strin1
        fin_string2 = string2 + strin2
        fin_string3 = string3 + strin3
        fin_string4 = string4 + strin4
        fin_string5 = string5 + strin5
        fin_string6 = string6 + strin6

        print('\n')
        print('Player')
        print('\n')
        print(fin_string)
        print(fin_string1)
        print(fin_string2)
        print(fin_string3)
        print(fin_string4)
        print(fin_string5)
        print(fin_string6)

        self.fin_string = fin_string
        self.fin_string1 = fin_string1
        self.fin_string2 = fin_string2
        self.fin_string3 = fin_string3
        self.fin_string4 = fin_string4
        self.fin_string5 = fin_string5
        self.fin_string6 = fin_string6




    def computer_board(self):
        if self.number_value[q+1] == '10':
            com_string = ' ----------- '
            com_string1 = '|  '+self.card_symbols[q+1]+'        |'
            com_string2 = '|           |'
            com_string3 = '|    '+self.number_value[q+1] + '     |'
            com_string4 = '|           |'
            com_string5 = '|           |'
            com_string6 = ' ----------- '
        else:
            com_string = ' ----------- '
            com_string1 = '|  '+self.card_symbols[q+1]+'        |'
            com_string2 = '|           |'
            com_string3 = '|    '+self.number_value[q+1] + '      |'
            com_string4 = '|           |'
            com_string5 = '|           |'
            com_string6 = ' ----------- '

        if self.number_value[q+3] == '10':
            com_strin = '\t ----------- '
            com_strin1 = '\t|           |'
            com_strin2 = '\t|           |'
            com_strin3 = '\t|           |'
            com_strin4 = '\t|           |'
            com_strin5 = '\t|           |'
            com_strin6 = '\t ----------- '
        else:
            com_strin = '\t ----------- '
            com_strin1 = '\t|           |'
            com_strin2 = '\t|           |'
            com_strin3 = '\t|           |'
            com_strin4 = '\t|           |'
            com_strin5 = '\t|           |'
            com_strin6 = '\t ----------- '


        fin_com_string = com_string + com_strin
        fin_com_string1 = com_string1 + com_strin1
        fin_com_string2 = com_string2 + com_strin2
        fin_com_string3 = com_string3 + com_strin3
        fin_com_string4 = com_string4 + com_strin4
        fin_com_string5 = com_string5 + com_strin5
        fin_com_string6 = com_string6 + com_strin6

        print('\n')
        print('Computer')
        print('\n')
        print(fin_com_string)
        print(fin_com_string1)
        print(fin_com_string2)
        print(fin_com_string3)
        print(fin_com_string4)
        print(fin_com_string5)
        print(fin_com_string6)

        self.fin_com_string = fin_com_string
        self.fin_com_string1 = fin_com_string1
        self.fin_com_string2 = fin_com_string2
        self.fin_com_string3 = fin_com_string3
        self.fin_com_string4 = fin_com_string4
        self.fin_com_string5 = fin_com_string5
        self.fin_com_string6 = fin_com_string6


    def score(self):
        if self.number_value[q] in ['J','K','Q']:
            pt1 = 10
        elif self.number_value[q] in ['A']:
            pt1 = 1
        else:
            pt1 = int(self.number_value[q])

        if self.number_value[q+2] in ['J','K','Q']:
            pt2 = 10
        elif self.number_value[q+2] in ['A']:
            pt2 = 1
        else:
            pt2 = int(self.number_value[q+2])

        player_score = pt1+pt2
        self.player_score = player_score

        if self.number_value[q+1] in ['J','K','Q']:
            com_pt1 = 10
        elif self.number_value[q+1] in ['A']:
            com_pt1 = 1
        else:
            com_pt1 = int(self.number_value[q+1])

        if self.number_value[q+3] in ['J','K','Q']:
            com_pt2 = 10
        elif self.number_value[q+3] in ['A']:
            com_pt2 = 1
        else:
            com_pt2 = int(self.number_value[q+3])

        com_score = com_pt1+com_pt2
        self.com_score = com_score

    def point_count(self):
        k = 4
        c = k + 1
        self.k = k
        self.c = c
        game_on = True
        while game_on == True:
            os.system('say Would you like to take a Hit or Stay?')
            game_q = input('\n Would you like to take a Hit or Stay? ')
            if game_q.lower().startswith('s'):
                os.system('say Stay it is')
                if self.player_score == self.com_score:
                    print('\nPlayer Score:', self.player_score)
                    print('\nComputer Score:',self.com_score)
                    print('\nIt is a tie!!!')
                    os.system('say It is a tie')
                    game_on = False
                elif self.player_score > 21:
                    print('\nPlayer Score:', self.player_score)
                    print('\nComputer Score:',self.com_score)
                    print('\nBUST!! You lost the game better luck next time!')
                    os.system('say BUST, You lost the game, better luck next time')
                    game_on = False
                elif self.com_score > 21:
                    print('\nPlayer Score:', self.player_score)
                    print('\nComputer Score:', self.com_score)
                    print('\nCongratulations!! You have won the game!!')
                    os.system('say Congratulations!! You have won the game')
                    game_on = False
                elif self.player_score < self.com_score:
                    print('\nPlayer Score:', self.player_score)
                    print('\nComputer Score:',self.com_score)
                    print('\nBUST!! You lost the game better luck next time!')
                    os.system('say BUST, You lost the game, better luck next time')
                    game_on = False
                else:
                    print('\nPlayer Score:', self.player_score)
                    print('\nComputer Score:',self.com_score)
                    print('\nCongratulations!! You have won the game!!')
                    os.system('say Congratulations!! You have won the game')
                    game_on = False

            elif game_q.lower().startswith('h'):
                os.system('say hit, it is ')
                if self.number_value[k] == '10':
                    car = '\t----------- '
                    car1 = '\t|  '+self.card_symbols[k]+'        |'
                    car2 = '\t|           |'
                    car3 = '\t|    '+self.number_value[k] + '     |'
                    car4 = '\t|           |'
                    car5 = '\t|           |'
                    car6 = '\t ----------- '
                else:
                    car = '\t ----------- '
                    car1 = '\t|  '+self.card_symbols[k]+'        |'
                    car2 = '\t|           |'
                    car3 = '\t|    '+self.number_value[k] + '      |'
                    car4 = '\t|           |'
                    car5 = '\t|           |'
                    car6 = '\t ----------- '

                self.fin_string = self.fin_string + car
                self.fin_string1 = self.fin_string1 + car1
                self.fin_string2 = self.fin_string2 + car2
                self.fin_string3 = self.fin_string3 + car3
                self.fin_string4 = self.fin_string4 + car4
                self.fin_string5 = self.fin_string5 + car5
                self.fin_string6 = self.fin_string6 + car6

                if self.number_value[k+1] == '10':
                    com = '\t----------- '
                    com1 = '\t|  '+self.card_symbols[c]+'        |'
                    com2 = '\t|           |'
                    com3 = '\t|    '+self.number_value[c] + '     |'
                    com4 = '\t|           |'
                    com5 = '\t|           |'
                    com6 = '\t ----------- '
                else:
                    com = '\t ----------- '
                    com1 = '\t|  '+self.card_symbols[c]+'        |'
                    com2 = '\t|           |'
                    com3 = '\t|    '+self.number_value[c] + '      |'
                    com4 = '\t|           |'
                    com5 = '\t|           |'
                    com6 = '\t ----------- '

                self.fin_com_string = self.fin_com_string + com
                self.fin_com_string1 = self.fin_com_string1 + com1
                self.fin_com_string2 = self.fin_com_string2 + com2
                self.fin_com_string3 = self.fin_com_string3 + com3
                self.fin_com_string4 = self.fin_com_string4 + com4
                self.fin_com_string5 = self.fin_com_string5 + com5
                self.fin_com_string6 = self.fin_com_string6 + com6


                print('\n ----------- ')
                print('|           |')
                print('| -----------')
                print('||           |')
                print('|| -----------')
                print('|||           |')
                print(' ||    deck   |')
                print(' ||           | ')
                print('  |           |')
                print('  |           |')
                print('   ----------- ')

                print('\n')
                print('Computer')
                print('\n')
                print(self.fin_com_string)
                print(self.fin_com_string1)
                print(self.fin_com_string2)
                print(self.fin_com_string3)
                print(self.fin_com_string4)
                print(self.fin_com_string5)
                print(self.fin_com_string6)

                print('\n')
                print('Player')
                print('\n')
                print(self.fin_string)
                print(self.fin_string1)
                print(self.fin_string2)
                print(self.fin_string3)
                print(self.fin_string4)
                print(self.fin_string5)
                print(self.fin_string6)

                if self.number_value[k] in ['J','K','Q']:
                    pt1 = 10
                elif self.number_value[k] in ['A']:
                    pt1 = 1
                else:
                    pt1 = int(self.number_value[k])

                if self.number_value[c] in ['J','K','Q']:
                    pt2 = 10
                elif self.number_value[c] in ['A']:
                    pt2 = 1
                else:
                    pt2 = int(self.number_value[c])



                self.player_score = self.player_score + pt1
                self.com_score = self.com_score + pt2

                if self.player_score > 21:
                    if self.player_score == self.com_score:
                        print('\nPlayer Score:', self.player_score)
                        print('\nComputer Score:',self.com_score)
                        print('\nIt is a tie!!!')
                        os.system('say It is a tie')
                        game_on = False
                    else:
                        print('\nPlayer Score:', self.player_score)
                        print('\nComputer Score:',self.com_score)
                        print('\nBUST!! You lost the game better luck next time!')
                        os.system('say BUST, You lost the game, better luck next time')
                        game_on = False
                elif self.com_score > 21:
                    if self.player_score == self.com_score:
                        print('\nPlayer Score:', self.player_score)
                        print('\nComputer Score:',self.com_score)
                        print('\nIt is a tie!!!')
                        os.system('say It is a tie')
                        game_on = False
                    else:
                        print('\nPlayer Score:', self.player_score)
                        print('\nComputer Score:',self.com_score)
                        print('\nCongratulations!! You have won the game!!')
                        os.system('say Congratulations!! You have won the game')
                        game_on = False
                else:
                    game_on == True
                    k += 2
                    c = k + 1
                    continue
            else:
                print('\nInavalid option, please try again!')
                os.system('say Inavalid option, please try again')
                continue
        else:
            os.system('say Would you like to play again')
            print('\n')
            replay = input('Would you like to play again!? ')
            if replay.lower().startswith('y'):
                game()
            else:
                print('\nThanks for playing!!')
                os.system('say Thanks for playing')
                print('\nCome back soon!!\n')
                os.system('say Come back soon')
                exit()

    def start(self):
        self.start_game = '\n\nHey there!! Welcome to BlackJack!'
        self.end_game = '\nThank You for playing hope you enjoyed it, do play again!!'
        self.ask = 'Are you ready to play the game!! '
        print(self.start_game)
        os.system('say Hey there, Welcome to BlackJack')
        os.system('say Hey player what is your name?')
        print('\n')
        player = input('Hey player what is your name? ')
        os.system('say Hello there ' + str(player))
        os.system('say Are you ready to play the game')
        ready_game = input('\n'+ str(self.ask))
        if ready_game.lower().startswith('y'):
            print('\nOkay!! get ready!\n')
            os.system('say Okay get ready')
        else:
            print(self.end_game)
            os.system('say Thank You for playing hope you enjoyed it, do play again')
            print('\nCome back soon!!\n')
            os.system('say Come back soon')
            exit()
all_cards = Cards_Values()
full_deck = all_cards.deck
dip = Display()
def game():
    random.shuffle(full_deck)
    dip.start()
    dip.card_num()
    dip.card_symbol()
    dip.display_deck()
    dip.computer_board()
    dip.player_board()
    dip.score()
    dip.point_count()
try:
    game()
except KeyboardInterrupt:
    print('\n\nLooks like you are busy, come back soon!!\n')
    os.system('say Looks like you are busy, come back soon')
    exit()
