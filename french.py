import sys
dict = {'Yes':['Oui','wee'],'NO':['Non','nong'],'Please':['S\'il vous plait','seel voo play'],'Thank':['mer','mair'],'You':['ci','see']}
french = []
pronounciation = []
n = input("Enter your  sentence: ")
a = n.split(" ")
length = len(a)
for i in range(length):
         if i in dict.keys():
             french.append(dict.get(i)[0])
             pronounciation.append(dict.get(i)[1])
         else:
             french.append(dict.get(i))
             pronounciation.append(dict.get(i))
c=french+pronounciation
print("IN FRENCH",c)
french.clear()
pronounciation.clear()