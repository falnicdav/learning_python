def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 1:
                guess = input('Sorry wrong answer. Try again.')
            attempt = attempt + 1
    if attempt == 2:
        print('The correct answer is ' + answer)
score = 0
print('How well do you know Fallon?')
guess1 = input('What is my favorite color?')
check_guess(guess1, 'green')
guess2 = input('What is my favorite dessert?')
check_guess(guess2, 'rice pudding')
guess3 = input('What is my "lucky" number?')
check_guess(guess3, '3')
guess4 = input('Which is not one of my favorite shows?\n \
A) Sherlock Holmes\n B) Sword Art Online\n C) Unfortunate Events\n D) Inuyasha\n \
Type A, B, C, or D')
check_guess(guess4, 'C')
guess5 = input('I had lizards called Woohoo and Weehoo. True or False? ')
check_guess(guess5, 'True')
print('Your score is ' + str(score))
guess6 = input('press any key to end')

