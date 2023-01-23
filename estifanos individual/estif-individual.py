#Name Estifanos Zerihun    ID:1743/12    
print("Enter the string")
string=input()
dic={}
for ch in string:
    if ch in dic:
        dic[ch]=dic[ch]+1
    else:
        dic[ch]=1
print("In the String",string,"there are")
print("character","        ","Frequency")
for key in dic:
    print("  ",key,"---------------->",dic[key])       