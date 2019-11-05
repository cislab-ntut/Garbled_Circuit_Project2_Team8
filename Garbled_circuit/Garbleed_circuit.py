#input gate how many to many
#input line
#input output
a=0
b=0
c=0
counter=0
print ("Total line in the circuit:")
tline = int(input("tline:"))
eachlinedata1=[None]*tline
eachlinedata2=[None]*tline
print(eachlinedata1)
print(eachlinedata2)
print ("Total inputline in the circuit:")
inputline = int(input("inputline:"))
f = open("input.txt", "r")
s=f.read()
s=s.split()
for i in range(inputline):
    eachlinedata1[i]=s[i*2]
    eachlinedata2[i]=s[1+i*2]
print(eachlinedata1)
print(eachlinedata2)
print ("Total gates in the circuit:")
tgate = int(input("tgate:"))
gatelist1=[None]*tgate
gatelist2=[None]*tgate
gatelist3=[None]*tgate
gatelist4=[None]*tgate

def AND(a,b,c):
    if(eachlinedata2[a]==eachlinedata2[b]):
        gatelist1[counter]=("w"+str(a)+","+str(eachlinedata2[a])+" | "+"w"+str(b)+","+str(eachlinedata2[b])+" (w"+str(c)+",1"")")
    gatelist2[counter]=("w"+str(a)+","+str(eachlinedata1[a])+" | "+"w"+str(b)+","+str(eachlinedata2[b])+" (w"+str(c)+",0"")")
    gatelist3[counter]=("w"+str(a)+","+str(eachlinedata2[a])+" | "+"w"+str(b)+","+str(eachlinedata1[b])+" (w"+str(c)+",0"")")
    gatelist4[counter]=("w"+str(a)+","+str(eachlinedata1[a])+" | "+"w"+str(b)+","+str(eachlinedata1[b])+" (w"+str(c)+",0"")")
    eachlinedata1[c]='0'
    eachlinedata2[c]='1'
def OR(a,b,c):
    if(eachlinedata1[a]==eachlinedata1[b]):
        gatelist1[counter]=("w"+str(a)+","+str(eachlinedata1[a])+" | "+"w"+str(b)+","+str(eachlinedata1[b])+" (w"+str(c)+",0"")")
    gatelist2[counter]=("w"+str(a)+","+str(eachlinedata1[a])+" | "+"w"+str(b)+","+str(eachlinedata2[b])+" (w"+str(c)+",1"")")
    gatelist3[counter]=("w"+str(a)+","+str(eachlinedata2[a])+" | "+"w"+str(b)+","+str(eachlinedata1[b])+" (w"+str(c)+",1"")")
    gatelist4[counter]=("w"+str(a)+","+str(eachlinedata2[a])+" | "+"w"+str(b)+","+str(eachlinedata2[b])+" (w"+str(c)+",1"")")

f = open("circuit.txt", "r")
for x in f:
    x=x.split()
    print(x)
    a=int(x[0])-1
    b=int(x[1])-1
    c=int(x[3])-1
    if('AND'==x[2]):
        AND(a,b,c)
    if('OR'==x[2]):
        OR(a,b,c)
    counter=counter+1

print (gatelist1)
print (gatelist2)
print (gatelist3)
print (gatelist4)







