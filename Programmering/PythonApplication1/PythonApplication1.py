import random

List = []

for i in range(random.randint(1,10)):
    List.append(random.randint(-10,10)) 

print("The list:", List)
print("")

dictionary = {}

for i in range(len(List)):
    for j in range(i+1, len(List)+1):
        subarray = List[i:j]
        subarray_sum = sum(subarray)
        dictionary_key = "Subarray " + str(i) + "-" + str(j-1)
        dictionary[dictionary_key] = (subarray, subarray_sum)

for key, value in dictionary.items():
    print(key + ": " + str(value[0]) + ", Sum = " + str(value[1]))
print("")

largest_sum = max(value[1] for value in dictionary.values())

biggest_subarrays_keys = [key for key, value in dictionary.items() if value[1] == largest_sum]

print("Subarrays with the largest sum:")
for key in biggest_subarrays_keys:
    print(key + ": " + str(dictionary[key][0]) + ", Sum = " + str(dictionary[key][1]))