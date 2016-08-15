def to_rna(dna):
    """Given a DNA strand, returns its RNA complement."""
    
    rna = []
    
    for char in dna:
        if char == "G":
            rna.append("C")
        elif char == "C":
            rna.append("G")
        elif char == "T":
            rna.append("A")
        elif char == "A":
            rna.append("U")
    
    return "".join(rna)
