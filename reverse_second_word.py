#Reverse every other word in a given string, then return the string
def reverse_alternate(string):
    new_string = string.split()
    for i in new_string:
        if (new_string.index(i)+1)%2 == 0:
            new_string[new_string.index(i)] = i[::-1]
    final_result = " ".join(i.strip() for i in new_string)
    return final_result

print(reverse_alternate('Hello my name is Unknown'))