def is_pangram(sentence):
    """A function that determines whether a sentence is a pangram."""
    
    full_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = sentence.lower()
    
    for letter in sentence:
        if letter in full_alphabet:
            full_alphabet.remove(letter)
            
    if len(full_alphabet) == 0:
        return True
    
    else:
        return False
