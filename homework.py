list = ['this' , 'is', 'a', 'sentence', '.']

def reverse(list):
    a_list = []
    for word in list:
        a_list.append(word[::-1])


    left = 0
    right = len(a_list)-1
    while left <= right:
        a_list[left], a_list[right] = a_list[right], a_list[left]
        left+=1
        right-=1

    return a_list

print(reverse(list))

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
word_list = []
my_dict = {}
for word in a_text.lower().split(" "):
    word_list.append(word)
                
for word in word_list:
    try:
        my_dict[word] += 1
    except:
        my_dict[word] = 1

print(my_dict)

nums_list = [10,23,45,70,11,15]
target = 70

def linear_search(list, target):
    for num in list:
        if num == target:
            return "Target Found"
        
    return -1

print(linear_search(nums_list, target))




