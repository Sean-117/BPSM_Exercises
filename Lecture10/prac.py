import re


#1
sequence="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("number of A:",sequence.count("A"))
print("number of B:",sequence.count("T"))
print(sequence.count("A")+sequence.count("T")/len(sequence))

#2
s2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
s2r=""
for i in range(0,len(s2)-1):
    if s2[i]=="A":
        s2r+="T"
    elif s2[i]=="G":
        s2r+="C"
    elif s2[i]=="C":
        s2r+="G"
    elif s2[i]=="T":
        s2r+="A"
print(s2r)

#3
s3=s2
position=re.search("G*AATTC",s3)
print(position)

