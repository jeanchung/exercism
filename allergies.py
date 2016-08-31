class Allergies(object):
    """
    Given a person's allergy score, can tell them whether or not they're
    allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * peanuts (2)
    * shellfish (4)
    * strawberries (8)
    * tomatoes (16)
    * chocolate (32)
    * pollen (64)
    * cats (128)
    """
    
    def __init__(self, score):
        self.score = score
        self.calculate_allergies()
        self.lst = [x for x in self.allergy_report.keys() if self.allergy_report[x]]
    
    def calculate_allergies(self):   
        allergens = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: 
                     "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}
        self.allergy_report = {}
                          
        for num in sorted(allergens.keys(), reverse=True):
            if self.score >= num:
                self.allergy_report[allergens[num]] = True
                self.score -= num
            else:
                self.allergy_report[allergens[num]] = False
                       
    def is_allergic_to(self, item):
        return self.allergy_report[item]
        
