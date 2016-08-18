def word_count(phrase):
    """Given a phrase, counts the number of times each word occurs in the phrase."""

    # Deals with unicode
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
    
    # Saves phrase as a list of words
    words = phrase.lower().split()
    
    # Dictionary to hold all words and their frequency in the phrase
    word_dict = {}
    
    for word in words:
    
        # Increases count for words already in dictionary
        if word in word_dict.keys():
            word_dict[word] += 1
        
        # Adds new words to dictionary with count of 1
        else:
            word_dict[word] = 1
                
    return word_dict
    
    