import numpy as np

tuple_of_words=("computer","astana","london","france","italy","argon","pinarello","python","table")
tuple_of_hints=("What would you use to play Doom-2?","The capital of one Asian country","Tha capital of the Great Britan","Country of the Europe","Country of the Europe","Inert gas","Bicycle brand","Computer language","The place where you have a dinner")
position=np.random.randint(9)
the_word = tuple_of_words[position]

game_over = False
board = list("*" * len(the_word))

points1=0
points2=0
y=0
two_players=["1st player","2nd player"]
while not game_over:
    one_of_them=two_players[y]
    print("")
    print("------------------------------")
    print(f"1st player's points = {points1}")
    print(f"2nd player's points = {points2}")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {tuple_of_hints[position]}")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    x=0
    if user_guess in board:
            print("There is already such letter.")
            continue
    if len(user_guess) == 1:
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
                if one_of_them=="1st player":
                    points1+=1
                else:
                    points2+=1
                if ''.join(board)==the_word:
                    print(f"Correct! {two_players[y]} wins!")
                    game_over = True
                x+=1
        if x==0:
            print("There is no such letter.")
            print("Next players turn")
            if y==0:
                y+=1
            else:
                y-=1
        elif (x!=0) and (game_over==False):
            print("Your turn")
        
            
    else:
        if user_guess == the_word:
            print(f"Correct! {two_players[y]} wins!")
            game_over = True
        else:
            print("Incorrect, next players turn.")
            if y==0:
                y+=1
            else:
                y-=1
            
# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.
