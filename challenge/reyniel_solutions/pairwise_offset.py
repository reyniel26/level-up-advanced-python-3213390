# Hehe no import

def pairwise_offset(sequence, fillvalue='*', offset=0):
    a_sequence = [item for item in sequence]
    a_sequence.extend([fillvalue for num in range(offset)])
    b_sequence = [fillvalue for num in range(offset)]
    b_sequence.extend([item for item in sequence])
    
    return [(a_sequence[num],b_sequence[num]) for num in range(len(a_sequence))]
