from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def diffNucleotides(seq1, seq2):
    c, j = 0, 0
    for i in seq1:
# this will check if character extracted from seq1 is present in seq2 or not(seq2.find(i) 
# return 1 if not found and j == seq2.find(i) is used to  
# avoid the counting of the duplicate characters 
# present in seq1 found in seq2 
        if seq1.find(i) <= 0 and j == seq2.find(i):
            c += 1
        j += 1
    print("Diffrence Between two Sequence is {}".format(c))
# Function For Global Alignment
def global_allignment(seq1, seq2):
    # 2 - scoring for identical match
    # -1 - scoring for non identical match
    #  -0.5 - score for a gap penalty
    #  -0.1 - score for extending gap
    alignments = pairwise2.align.globalxx(seq1, seq2)
    print("Global_Alignment")
    for a in alignments:
        print(format_alignment(*a))
# Funtion for Local Alignment
def local_allignment(seq1, seq2):
    # identical match will have score 1 otherwise 0 and no gap penalties
    alignments2 = pairwise2.align.localxx(seq1, seq2)
    print("Local Alignment")
    for a in alignments2:
        print(format_alignment(*a))
    
if __name__ == "__main__":
    # Convert input sequence in Uppercase
    s1 = input("Enter 1st sequence: ").upper()
    s2 = input("Enter 2nd sequence: ").upper()
    # Check which sequence is Bigger, set Bigger one as seq 1 and other as Seq2
    if len(s1) > len(s2):
        seq1 = s1
        seq2 = s2
    else:
        seq1 = s2
        seq2 = s1
    diffNucleotides(seq1, seq2)
    global_allignment(seq1, seq2)
    local_allignment(seq1, seq2)