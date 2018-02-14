https://www.w3resource.com/python-exercises/dictionary/

1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

import operator

# sorting a dictionary
mydict = {'a':1, 'z':3, 'x':8}
# add 1 more pair
mydict['k'] = 7

# sort key, asc
sorted_mydict = sorted(mydict.items(), key=operator.itemgetter(0))

# sort key, desc
sorted_mydict = sorted(mydict.items(), key=operator.itemgetter(0), reverse=true)


# to sort by value, change the 0 to 1




2. Write a Python script to add a key to a dictionary
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

sdict = {0:10, 1:20}
print(sdict)
sdict[2] = 30
print(sdict)

or

sdict.update({2:30})


3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

newdict = dic1 + dic2 + dic3