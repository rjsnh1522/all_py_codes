"""
    Reverse words of a string
"""
string = "ram is good boy"

def reverse_words_in_a_string(string):
    rev = ""
    temp = ""
    for st in string:
        if st == " ":
            rev = temp + " " + rev
            temp = ""
        else:
            temp += st
    return rev

"""
   Reverse the char inplace of a string
"""

def reverse_chars_of_words_of_string(string):
    rev = ""
    temp = ""
    for st in string:
        if st == " ":
            rev = temp + " " + rev
            temp = ""
        else:
            temp += st
    if temp != "":
        rev = temp +" "+ rev
    return rev


# print(reverse_chars_of_words_of_string(string))


def count_max_character_counting_in_string(string):
    counter_hash = {}
    for st in string:
        if st in counter_hash:
            counter_hash[st] += 1
        else:
            counter_hash[st] = 1

    max_ = -9999
    chare = ""
    for char in counter_hash:
        if counter_hash[char] > max_:
            max_ = counter_hash[char]
            chare = char

    print(max_, chare)
    print(counter_hash)
    return max_, chare

new_string = "some gibrish string here to check if its working or not"
print(count_max_character_counting_in_string(new_string))


"""
    return first n char and last n char of a string
"""
