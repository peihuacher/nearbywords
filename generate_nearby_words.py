import itertools

def is_word(word):
    words = ['cat', 'bat', 'car']
    if word in words:
        return True
    else:
        return False

def generate_perm_order(word_nearby_char, word):
    perm = list(itertools.product(word_nearby_char[0], word_nearby_char[1], word_nearby_char[2]))

    words = []
    for newword in perm:
        order = False
        for i in range(len(word)):
            if newword[i] in word_nearby_char[i]: # position character exist in order 
                order = True
            else:
                order = False
        if order: # all three position of character is in order
            words.append(''.join(newword))
    return words

def get_nearby_chars(char):
    nearby_char = { # nearby words in alphabetical order
        'c': ['c','b','d'],
        'a': ['a','z','b'], 
        't': ['t','s','u']
    }
    nearby_qwerty_char = { # nearby words in qwerty keyboard
        'c': ['c','x','d','f','v'],
        'a': ['a','q','w','s','x','z'],
        't': ['t','r','5','6','y','h','g','f']
    }
    return nearby_char[char]

def generate_nearby_words(word):
    word_nearby_char = []
    for ch in word:
        word_nearby_char.append(get_nearby_chars(ch))
    
    words = generate_perm_order(word_nearby_char, word)
    print(words)
    newwords = [word for word in words if is_word(word)]
    print(newwords)
    
generate_nearby_words('cat')
