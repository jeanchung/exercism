def distance(strand1, strand2):
    """Calculates the Hamming difference between two DNA strands."""
    
    assert len(strand1) == len(strand2), "The two strands must be the same length."
    
    differences = 0
    
    for i, char in enumerate(strand1):
        if strand1[i] != strand2[i]:
            differences += 1
    
    return differences