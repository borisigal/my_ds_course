"""
data structures 

dictionaries ex1
----------------
"""
dictionary1={'a': ['apple','action','alien'],'b': ['break','bed','bill'],'c': ['cherry','china','copy']}
#print(dictionary1)

dictionary1['a'].append('avenue')
dictionary1['b'].append('black')
dictionary1['c'].append('coach')


dictionary1['d']=['dwell','done','directory']

dictionary1.pop('c')

print(dictionary1)
list1=dictionary1.values()
print(list1)

print("\n\n\n")
"""
dictionaries ex2
----------------

sets ex1
--------
"""

string1='barry'
string2='avy'
set1=set(string1)&set(string2)
print(len(set1))
print("\n\n\n")

"""
sets ex2
--------
"""
sunday_visitors = ['abe', 'bob', 'carl', 'dave', 'ed',
                   'heinrich', 'isabel', 'abe', 'fred']
monday_visitors = ['abe', 'gale', 'ed', 'fred']
tuesday_visitors = ['ed', 'bob', 'jack', 'fred', 'abe',
                    'abe', 'jack', 'kent', 'gal']


sunday_unique_visitors=set(sunday_visitors) #set1
monday_unique_visitors=set(monday_visitors) #set2
tuesday_unique_visitors=set(tuesday_visitors) #set3
total_unique_visitors=sunday_unique_visitors|monday_unique_visitors|tuesday_unique_visitors #set4
#print(sunday_unique_visitors)
#print(monday_unique_visitors)
#print(tuesday_unique_visitors)

#print(total_unique_visitors) #1
#print("\n\n")
is_sunday_in_monday=sunday_unique_visitors<monday_unique_visitors
is_monday_in_sunday=sunday_unique_visitors>monday_unique_visitors

is_sunday_in_tuesday=sunday_unique_visitors<tuesday_unique_visitors
is_tuesday_in_sunday=sunday_unique_visitors>tuesday_unique_visitors

is_monday_in_tuesday=monday_unique_visitors<tuesday_unique_visitors
is_tuesday_in_monday=monday_unique_visitors>tuesday_unique_visitors


print("the answer for Is there a day, that every visitor of that day, had also visited on another day is: ",end=' ')
print(is_sunday_in_monday
      or is_monday_in_sunday
      or is_sunday_in_tuesday
      or is_tuesday_in_sunday
      or is_monday_in_tuesday
      or is_tuesday_in_monday) #2
print("\n\n\n")
# there is no such day, that every visitor of that day, had also visited on another day

set_sunday_and_monday=sunday_unique_visitors&monday_unique_visitors
set_monday_and_tuesday=monday_unique_visitors&tuesday_unique_visitors 
set_sunday_and_tuesday=sunday_unique_visitors&tuesday_unique_visitors
set_every_Day=sunday_unique_visitors&monday_unique_visitors&tuesday_unique_visitors
set_all_options=set_sunday_and_monday|set_monday_and_tuesday|set_sunday_and_tuesday|set_every_Day
print('visited more than one day:',end=' ')
print(set_all_options)
print("\n\n\n")
print('visited every day:',end=' ')
print(set_every_Day)
print("\n\n\n")

set_tuesday_only=tuesday_unique_visitors-sunday_unique_visitors-monday_unique_visitors
print('visited on tuesday only:',end=' ')
print(set_tuesday_only)
print("\n\n\n")
set_exactly_on_sunday_and_monday=set_sunday_and_monday-tuesday_unique_visitors
print('exactly on one of the days Sunday and Monday:',end=' ')
print(set_exactly_on_sunday_and_monday) #nobody
print("\n\n\n")


"""
class_ex_Review Data Structures
-------------------------------
"""

test = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},
1000,
2000,
3000,
['hat', 't-shirt', 'jeans', {'socks1': 'red', 'socks2': 'blue'}]]

print(test[2])
print(test[0])
print(test[4])
print(test[0]['Arizona'])
print(test[4][2])
print(test[4][3]['socks2'])

list1= [1,1,1,2,3,4,5,6,6]
list_unique_items=list((set(list1)))
print(list_unique_items)
print(len(set(list1)))
print(len(list1)-len(set(list1)))