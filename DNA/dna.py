#DNA analysis for crime investigation
sample = ['GTA','GGG','CAC']
def read_dna(dna_file):
    dna_data = ""
    with  open(dna_file, "r") as f:
        for line in f:
            dna_data += line  
        return dna_data 
        
def dna_codons(dna):
    codons = []
    for i in range(0, len(dna)):
        if (i+3) < len(dna):
            codons.append(dna[i:i+3])  
    return codons
  
def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in dna:
            matches+=1  
    return matches
def is_criminal(dna_sample):  
    dna_data = read_dna(dna_sample)  
    
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
        print "The number of matches is %s" %(num_matches)
        print "Investigation should be continuing."
    else:
        print "The number of matches is %s" %(num_matches) 
        print " The suspect can be freed."
      
is_criminal("suspect1.rtf")  