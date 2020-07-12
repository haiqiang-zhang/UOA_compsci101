def update_guess(answer, guess, character):
    for index in range(len(answer)):
        if answer[index] == character:
            guess = guess[:index]+answer[index]+guess[index+1:]
    return guess





answer = "ladder"
guess = "******"
guess = update_guess(answer, guess, "d")
print(guess)
guess = update_guess(answer, guess, "e")
print(guess)

answer = "explosion"
guess = "#########"
guess = update_guess(answer,guess,"o")
print(guess)
guess = update_guess(answer,guess,"x")
print(guess)






