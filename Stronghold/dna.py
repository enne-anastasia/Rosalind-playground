#input = open("C:/Users/ennea/Downloads/rosalind_ini2.txt",'r')
input = open("/home/enne/Documents/GitHub/Rosalind-playground/Stronghold/rosalind_dna.txt",'r')
output = open("/home/enne/Documents/GitHub/Rosalind-playground/Stronghold/output.txt",'w')
string = input.readline().strip()
dictionary = {'A':0, 'C':0, 'G':0, 'T':0}
for i in string:
    dictionary[i] = dictionary[i] + 1
output.write(str(dictionary['A'])+' '+str(dictionary['C'])+' '+str(dictionary['G'])+' '+str(dictionary['T']))
input.close()
output.close()
