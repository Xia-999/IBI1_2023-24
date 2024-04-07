import os
import re
sequence=input("please input one of two repetitive sequence (GTGTGT or GTCTGT):")
os.getcwd()
os.chdir("c:\\Users\\lenovo\\IBI1\\IBI1_2023-24\\IBI1_2023-24\\Practical8")
os.getcwd()
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'rt')
input_file = file.read().split(sep='\n')  #open the file
output_file=open(sequence+"_duplicate_genes.fa","w") #create the new file

firstfile={}     #create a dictionary to store DNA name and sequence
for line in input_file:
    if line.startswith(">"):
        name=line
        firstfile[name]=""
    else:
        firstfile[name]+=line.replace("\n","")

xfile={}  #create a dictionary to store deplicated genes' names and sequences and repetitive sequence'number
for i in firstfile.keys():
    if "duplication" in i and sequence in firstfile[i]:
        seq=str(firstfile[i])
        num=seq.count(sequence)
        name=i.split()[0]+" "+str(num)
        xfile[name]=firstfile[i]

for i in xfile.keys():  #write the new file
    output_file.write(i)
    output_file.write("\n")
    output_file.write(xfile[i])
    output_file.write("\n")
file.close()
