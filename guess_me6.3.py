# Assigning value to variable
guess_me = 5

# Using a for loop to iterate over range(10)
for number in range(10):
    if number < guess_me:
        print('Too low')
    elif number == guess_me:
        print('Found it!')
        break
    else:
        print('Oops')
        break
