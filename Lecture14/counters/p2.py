# Function version 2
# look at each base in the DNA sequence individually and check if it's undetermined or not
def count_undetermined_2(dna):
        total_undetermined = 0
            for base in dna.upper():
                        if base not in ['A', 'T', 'G', 'C']:
                                        total_undetermined = total_undetermined + 1
                                            return total_undetermined
