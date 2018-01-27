#Ex1

weight_in_kilograms=70
height_in_meters=1.75
bmi=weight_in_kilograms/height_in_meters**2
print("My height is %.2f meters, my weight is %d KGS and my BMI is %.2f "%(height_in_meters,weight_in_kilograms,bmi))

#Ex2

import string
first_name="Barry"
last_name="Sigal"
full_name=first_name+" "+last_name
full_name_length=len(full_name)

#Ex3

print("the length of %s is %d"%(full_name,full_name_length))
full_name_A=full_name.replace('a','A')
full_name_E=full_name_A.replace('e','E')
full_name_I=full_name_E.replace('i','I')
full_name_O=full_name_I.replace('o','O')
full_name_U=full_name_O.replace('u','U')
print(full_name_U)


same_city="true" if me_city==friend_city else "false"
is_older="true" if me_age==friend_age else "false"
diff_gender= "true" if me_gender==friend_gender else "false"
both_married= "true" if me_martial_status==friend_martial_status else "false"