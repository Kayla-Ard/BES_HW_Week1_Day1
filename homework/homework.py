# Advanced Operations on Python Lists

# Task 1
# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter.

def squares(n):

    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

# Task 2
# Implement a function that has 3 parameters representing a list and 2 indices that will reverse a sublist within the list from index i to j (inclusive).

def reverse_sublist(lst, i, j):

    if i < 0 or j >= len(lst) or i > j:
        return lst  
    
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]  
        i += 1
        j -= 1
    
    return lst

# Task 3
# Implement a function to merge two sorted lists into a single sorted list without using the built-in sorted function of list.sort method. 

def merge_lists(list1, list2):

    merged = []
    count_1 = 0
    count_2 = 0
    
    while count_1 < len(list1) and count_2 < len(list2):
        if list1[count_1] <= list2[count_2]:
            merged.append(list1[count_1])
            count_1 += 1
        else:
            merged.append(list2[count_2])
            count_2 += 1
    
    while count_1 < len(list1):
        merged.append(list1[count_1])
        count_1 += 1
    
    while count_2 < len(list2):
        merged.append(list2[count_2])
        count_2 += 1
    
    return merged




# Dictionary Manipulation and Optimization
# Task 1
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary
# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}
# Expected Output
# {"a": 1, "b": 4, "c": 5, "d": 6}

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  
    
    for key in dict2:
        merged[key] = dict2[key] 
    
    return merged


# Task 2
# Implement a function to find the difference of two dictionaries, i.e., keys that are only in one of the dictionaries along with their values. 
# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}
# Expected Output
# {"a": 1, "d": 6}

def diff_dict(dict1, dict2):
    difference = {}
    
    for key in dict1:
        if key not in dict2:
            difference[key] = dict1[key]
    
    for key in dict2:
        if key not in dict1:
            difference[key] = dict2[key]
    
    return difference


# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. *Bonus* Ignore case 

def count_word_frequency(words):

    frequency = {}
    
    for word in words:
        
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

