import itertools

def is_word(word):
    words = ['cat', 'bat', 'car']
    if word in words:
        return True
    else:
        return False

def generate_perm_order(word_nearby_char, word):
    perm = None
    perm = list(itertools.permutations(word_nearby_char, len(word)))
    
    words = []
    for newword in perm:
        order = False
        for i in range(len(word)):
            if newword[i] in get_nearby_chars(list(word)[i]): # position character exist in order 
                order = True
            else:
                order = False
        if order: # all three position of character is in order
            words.append(''.join(newword))
    return words

def get_nearby_chars(char):
    nearby_char = { # nearby words in alphabetical order
        'a': ['a','z','b'], 
        'b': ['b','a','c'], 
        'c': ['c','b','d'],
        'd': ['d','c','e'],
        'e': ['e','d','f'],
        'f': ['f','e','g'],
        't': ['t','s','u']
    }
    nearby_qwerty_char = { # nearby words in qwerty keyboard
        'c': ['c','x','d','f','v'],
        'a': ['a','q','w','s','x','z'],
        't': ['t','r','5','6','y','h','g','f']
    }
    return nearby_char[char]

def remove_duplicates(l):
    return list(set(l))

def generate_nearby_words(word):
    if not word:
        print("Error: word is empty.")
        print("Program exit.")
        return
    elif len(word) < 2:
        print("Error: words must be at least two characters.")
        print("Program exit.")
        return
        
    word_nearby_char = []
    for ch in list(word):
        for cha in get_nearby_chars(ch):
            word_nearby_char.append(cha)
    
    words = generate_perm_order(word_nearby_char, word)
    print(words)
    newwords = [word for word in words if is_word(word)]
    print(remove_duplicates(newwords))
    return remove_duplicates(newwords)
    
generate_nearby_words('cat')
