
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
user_name = input('Enter the User Name:')
for char in user_name:
    if char.lower() in vowels:
        vowel_count +=1
print('Out of {} letters, {} has, {} vowels'.format(len(user_name), user_name, vowel_count))
