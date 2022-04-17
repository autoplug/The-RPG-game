def isValidSubsequence(array, sequence):
    # Write your code here.
    result = []
    for x in sequence:
        if x in array:
            result.append(array.index(x))
    print(result)
    for x in range(len(result)-1):
        if result[x] > result[x+1]:
            return False
    return True


# print(isValidSubsequence([1, 2, 3, 4, 5], [4, 30]))
for x in set([1, 6, -1, -1]):
    print(x)
