from Bio import SeqIO
with open("/path/to/output/file1","a") as f:
    
    for i in SeqIO.parse("/path/to/input/file", "fasta"):
        if (i.seq).count("C") <=4 and (i.seq).count("C") > 1: 
            f.write(">"+str(i.id)+"\n"+str(i.seq)+"\n")
            

with open("/path/to/output/file2","a") as f2:
    
    for i in SeqIO.parse("/path/to/input/file", "fasta"):
        if (i.seq).count("C") > 4 :
            f2.write(">"+str(i.id)+"\n"+str(i.seq)+"\n")
