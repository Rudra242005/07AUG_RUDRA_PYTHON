"""Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

a = ''' the state for any person of being extremely poor. It is the not extreme situation when
     a person feels lack of essential items required to continue the life such as shelter, 
     adequate food, clothing, medicines, etc.'''


# sub_not = "not"
# sub_poor = "poor"

not_occ = a.find('not')
poor_occ = a.find('poor')

print(not_occ)
print(poor_occ)

if not_occ > poor_occ :
    
