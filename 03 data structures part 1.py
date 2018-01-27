#ex1

boys=['moshe','haim','david']
girls=['anael','rachel','yafa']
boys.append('levi')
girls.insert(0,'mila')
#print(boys)
#print(girls)
bride=girls.pop() #'yafa'
print("bride: ",bride)
groom=boys.pop(0)
print("groom: ",groom)
#print(boys[len(boys)-1])
boys.remove(boys[len(boys)-1])
#print(boys)

names=boys+girls
print(names) #extend is a method of which returns nothing. because of that extend will return nothing into names if we try to use it.

#ex2

list_moshe=['moshe',33,bool(1)]
list_haim=['haim',40,bool(0)]
list_david=['david',18,bool(1)]

list_moshe[1]=34
guys=[list_moshe,list_haim,list_david]
list_yanai=['yanai',28,bool(1)]
guys.append(list_yanai)
guys[1][1]=41
guys.pop()
guys.remove(list_moshe)
print(guys)



#ex3


sentence="i love my wife"
new_sentence=sentence.replace(' ','\n')
letter_to_find='m'

print(new_sentence)
print(sentence.count(letter_to_find))

counter=0

for letter in sentence:
    counter+=1 if letter==letter_to_find else 0
print(counter)