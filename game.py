secret_num = 40
guess = ""
guess_count = 0
guess_limit = 6
out_of_guesses = False

while guess != secret_num and not(out_of_guesses) :
    if guess_count < guess_limit:
        guess = input('Guess The Number:')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses :
    print('YOU LOSE')

else:
    print('YOU WIN')


     
