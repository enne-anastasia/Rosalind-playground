#input = open("C:/Users/ennea/Downloads/rosalind_ini2.txt",'r')
input = open("/home/enne/Documents/GitHub/Rosalind-playground/rosalind_fibo.txt",'r')
output = open("/home/enne/Documents/GitHub/Rosalind-playground/output.txt",'w')
n = int(input.readline())
f = [0,1]
for i in range(2,n+1):
    f.append(f[i-2]+f[i-1])
output.write(str(f[n]))
input.close()
output.close()
