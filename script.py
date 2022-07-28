input = open("C:/Users/ennea/Downloads/rosalind_ini2.txt",'r')
a,b = input.readline().split()
a = int(a)
b = int(b)
c = a**2 + b**2
print(c)
input.close()
