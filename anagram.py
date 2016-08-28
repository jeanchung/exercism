def detect_anagrams(word, list):
    """Returns a sublist of anagrams for word from given list."""
    word = word.lower()
    letters = {}
    anagrams = []
    
    # Save letters in word as dict with letter counts
    for char in word:
        if char in letters.keys():
            letters[char] += 1
        else:
            letters[char] = 1
    
    # Iterates through list, adding anagrams to new list
    for option in list:
        if option.lower() == word:
            pass
        else:
            comparison = {}
            for letter in option:
                if letter.lower() in comparison.keys():
                    comparison[letter.lower()] += 1
                else:
                    comparison[letter.lower()] = 1
            if letters == comparison:
                anagrams.append(option)
    
    return anagrams