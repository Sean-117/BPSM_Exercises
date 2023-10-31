def count_undetermined_1(dna):
    total_good_bases = 0
    for base in ['A', 'T', 'G', 'C']:
        total_good_bases = total_good_bases + dna.upper().count(base)
    return len(dna) - total_good_bases

