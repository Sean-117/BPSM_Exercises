protein_seq="MSRSLLLRFLLFLLLLPPLP"

#eeeeeee1111111
def percentcount(protein_seq, aa_code):
    count = protein_seq.count(aa_code.upper())
    return count/len(protein_seq)
aa_code = input("enter your wanted aa residue code:")
print(aa_code+":","{}%".format(percentcount(protein_seq, aa_code)))

#assertions:
assert round(100*percentcount(protein_seq,"M"))==round(5)
assert round(100*percentcount(protein_seq,"r"))==round(10)
assert round(100*percentcount(protein_seq,"L"))==round(50)
assert round(100*percentcount(protein_seq,"Y"))==round(0)

#eeeeeeee2222222







