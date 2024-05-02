def to_rna(dna_strand):
    dna_to_rna = {
    'G' : 'C',
    'C' : 'G',
    'T' : 'A',
    'A' : 'U'
    }
    
    rna_output = ''

    for dna in dna_strand:
        rna_output = rna_output + dna_to_rna[dna]
    
    return rna_output
