# odd /even labelling of list items

l =[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x : 'even' if x%2 == 0 else 'odd',l)))