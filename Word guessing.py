import numpy as np

tuple_of_words = ("computer","astana","london","france","italy","argon","pinarello","python","table")
tuple_of_hints = ("What would you use to play Doom-2?","The capital of one Asian country","Tha capital of the Great Britan","Country of the Europe","Country of the Europe","Inert gas","Bicycle brand","Computer language","The place where you have a dinner")
position = np.random.randint(8)
the_word = tuple_of_words[position]

sector_prize_position = np.random.randint(len(the_word)-1)
points1 = 0
points2 = 0
y = 0

board = list("*" * len(the_word))
two_players = ["1st player","2nd player"]
game_over = False


def func(z):
    if z==0:
        z+=1
    else:
        z-=1
    return z


while not game_over:
    one_of_them = two_players[y]
    print("")
    print("------------------------------")
    print(f"{one_of_them}'s turn")
    print(f"1st player's points = {points1}")
    print(f"2nd player's points = {points2}")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint : {tuple_of_hints[position]}")
    user_guess = input("Enter a word or a letter: ").lower()
    x = 0
    if user_guess in board:
            print("There is already such letter.")
            continue
    if len(user_guess) == 1:
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
                if i == sector_prize_position:   #сектор приз
                    print('You are in Sector Prize!')
                    prize = int(input('Prize or Money?\nPrize = 0, Money = any other number\n'))
                    if prize == 0:
                        print('You have a prize')
                    else:
                        print('You have 1000$')
                        
                elif (i != sector_prize_position) and (the_word[i] != the_word[sector_prize_position]):  #очко    
                    if one_of_them == "1st player":
                        points1 += np.random.randint(1,5)
                    else:
                        points2 += np.random.randint(1,5)
                        
                if ''.join(board) == the_word:
                    print(f"Correct! {one_of_them} wins!")
                    game_over = True
                x+=1
        if x==0:
            print("There is no such letter.")
            y = func(y)
    else:
        if user_guess == the_word:
            print(f"Correct! {two_players[y]} wins!")
            game_over = True
        else:
            print("Incorrect, next players turn.")
            y = func(y)
