# Array
# Arrays - Implementation
# Arrays - Basic Operations

li = []

# Insertion() − Adds an element at the given index.
for i in range(1, 101):
    li.append(i)

# Traverse() − accessing all the array elements one by one.
for i in range(1, 101):
    print(li[i])


# Update() − Updates an element at the given index.
# print(li[49], li[51])
# li[49] = 125

# print(id(50))

# Search() − Searches an element using the given index or by the value.
# method 1
for i in li:
    # print(i, end = '\t')
    if li[i] == 51:
        x = i
        break
# method 2
li[i] = 125
# print(li[50])
li[li.index(50)] = 125

# print(li[4:])

print(li[90:101], li[90:101][::-1], end='\n')

print(li[-10:], li[-10:][::-1])

for i in range(101, 201):
    li.append(i)
print(li)


# Deletion() − Deletes an element at the given index.
li.pop(2)
print(li)