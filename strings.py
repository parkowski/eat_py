myList = [1024, 3, True, 6.5]
myList.append(False)

print(myList)
1024, 3, True, 6.5, False

myList.insert(2,4.5)
print(myList)
1024, 3, 4.5, True, 6.5, False

print(myList.pop())
false

print(myList)
1024, 3, 4.5, True, 6.5

print(myList.pop(1))
3

print(myList)
1024, 4.5, True, 6.5

myList.pop(2)
true

print(myList)
1024, 4.5, 6.5

myList.sort()

print(myList)
4.5,6.5,1024

myList.reverse()
print(myList)
1024,6.5,4.5

print(myList.count(6.5))
1

print(myList.index(4.5))
2

myList.remove(6.5)


print(myList)
1024,4.5

del myList[0]

print(myList)
4.5