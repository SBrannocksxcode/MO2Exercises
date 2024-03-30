# Assigning a secret number and taking a guess from the user
secret = 7  # Change the secret number as desired
guess = 5   # Change the guess number as desired

# Conditional tests to determine if the guess is too low, too high, or just right
if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
else:
    print('Just right'