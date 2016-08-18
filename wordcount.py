def word_count(phrase):
    """Given a phrase, counts the number of times each word occurs in the phrase."""

    # Deals with unicode for Python 2
    try:
        phrase = phrase.decode('utf-8')
    except AttributeError:
        pass
    
    # Deals with non-alphanumeric characters
    if not phrase.isalnum():
        phrase_stripped = []
        for i, char in enumerate(phrase):
            # Letters and numbers pass through
            if char.isalnum():
                phrase_stripped.append(char)
            # Apostrophes pass through if preceded and followed by letters (contractions)    
            elif char == "'" and phrase[i-1].isalpha() and phrase[i+1].isalpha():
                phrase_stripped.append(char)
            # All other characters are replaced with a space
            else:
                phrase_stripped.append(" ")
        phrase = "".join(phrase_stripped)
    
    words = phrase.lower().split()
    word_dict = {}
    
    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
                
    return word_dict
    
    
