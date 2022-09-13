#Реализуйте алгоритм перемешивания списка.
import random

# test_list = [12, 4, 5, 6, 3, 9]
 
# print (test_list)
# random.shuffle(test_list)
# print(test_list)

test_list = [12, 4, 5, 6, 3, 9]
 
print (test_list)
 
for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    test_list[i], test_list[j] = test_list[j], test_list[i]
     

print (test_list)
