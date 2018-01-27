flow control|
------------|



flow control ex 1
-----------------

sentence = 'hello i am python'
char_to_search='m'
counter=0
for char in sentence:
    counter+=1 if char==char_to_search else 0
print(counter)


flow control ex 2
-----------------

sentence = 'hello i am python'
lower_sentence=sentence.lower()
unique_lower_sentence=set(lower_sentence)
vowels=('a','e','i','o','u')
counter=0
unique_counter=0
for vowel in vowels:
    counter+=lower_sentence.count(vowel)
    print(vowel,' ',lower_sentence.count(vowel))

for vowel in vowels:
    unique_counter+=1 if vowel in unique_lower_sentence else 0
print('\n')   
    
print(counter)
print(unique_counter)



flow control ex 3
-----------------
list1=[1,2,3,4,5,6]
list2=[]
list1_len=len(list1)

for i in list1:
   # print(i)
    list2.append(list1[list1_len-i])
print(list2)
list1.reverse()
print(list1)

-----------------


flow control ex 4
-----------------

import statistics
people=        {'barry':34
               ,'anael':32
               ,'maayan':1
               ,'david':72
               ,'mila':66
               ,'diana':43
               ,'tal':15
               ,'amir':9
               ,'avraham':63
               ,'rachel':53}
print(people)
people_length=len(people)
age_average=statistics.mean(people.values())
to_remove_list=[]
print(age_average)

#print(people_length)
for person in people.items():
        if person[1]<age_average:
            to_remove_list.append(person[0]) 

print(to_remove_list)
for i in range(0,len(to_remove_list)):
    name=to_remove_list[i]
    people.pop(name)
print(people)

------------------|
list comprehension|
------------------|


list comprehension ex 1
-----------------------

sentence='hello i am python'
char_to_find='o'
counter=[]
counter=[char for char in sentence if char==char_to_find]
print(len(counter))



list comprehension ex 2
-----------------------

list=['word'+str(n) for n in range(1,11)]
list.append('word')
print(list)
length_list=[len(length) for length in list]
print(length_list)
four_letter_list=[word for word in list if len(word)>4]
print(four_letter_list)


list comprehension ex 3
-----------------------

list=['word'+str(n) for n in range(1,11)]
list.append('word')
print(list)
reversed_list=[list[len(list)-i-1] for i in range(0,len(list))]
print(reversed_list)


list comprehension ex 4
-----------------------

string1='moshe  haim'
string2='david levi m'
common=[char for char in string1 if (char in string2 and char not in common) ]
print(common)



------|
while |
------|


while ex 1
----------
sum_all=0
index=0
while sum_all<1000:
    #print(index)
    sum_all+=index
    index+=1
print(sum_all)


while ex 2
----------

number=int(input())
iteration=2
not_prime=0

#print(number,iteration)
while iteration<number/2 and not_prime==0:
    not_prime=1 if number%iteration==0 else 0
    iteration+=1

print('the number is not prime') if not_prime==1 else print('the number is prime')


join and split example
----------------------

string='barry'
string2=' '.join(string)
print(string2)
string2='b,a,r,r,y'
string2=string2.split(' ')
print(string2)


abcd/efghi
----------------------

number1=1000
number2=100000
len_number2=len(str(number2))
len_number1=len(str(number1))
digits1 = [int(x) for x in str(number1)]
digits2 = [int(x) for x in str(number2)]
digits1_set=set(digits1)
digits2_set=set(digits2)

index_number1=number1
index_number2=number2
while index_number1 < 9876:
        while index_number2 < 98765:
            digits1 = [int(x) for x in str(index_number1)]
            digits2 = [int(x) for x in str(index_number2)]
            digits1_set=set(digits1)
            digits2_set=set(digits2)
            if len(digits1_set)==len(digits1) and len(digits2_set)==len(digits1) and index_number1/index_number2==1/3:
                print('true') 
            index_number2+=1
        index_number1+=1
                
"""
print('the sum of digits1 is:',sum(digits1))
print('the sum of digits2 is:',sum(digits2))

print('the length of number1 is:',len_number1)
print('the length of number2 is:',len_number2)
print(digits1)
print(digits2)

    