meme_dict = {'CRINGE': ':something wierd or embarrasing', 'LOL': 'something funny', 'sigma': 'someome cool', 'rizz': 'good pickup lines'}
word = input('write your unknown word(with big letters):')

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("word not found in the dictionary")
