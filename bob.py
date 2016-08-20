from re import search

def hey(what):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question.

    He answers 'Whoa, chill out!' if you yell at him.

    He says 'Fine. Be that way!' if you address him without actually saying
anything.

    He answers 'Whatever.' to anything else.
    """

    # say nothing
    if what == "" or what.isspace():
        return "Fine. Be that way!"

    what = what.strip()
    
    # yelling
    if what == what.upper() and search("[a-zA-Z]", what):
        return "Whoa, chill out!"
    
    # question
    if what[-1] == "?":
        return "Sure."
    
    # all else    
    return "Whatever."
