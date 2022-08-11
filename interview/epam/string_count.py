string = 'zzzzddaaaabcccxxaaaaaaaaaay'


def counter(string):
    char_count = {}
    cur_char = None
    prev_char = None
    visited = []
    cntr = 0
    for cur_char in string:
        if cur_char != prev_char:
            if prev_char in char_count:
                if char_count[prev_char] < cntr:
                    char_count[prev_char] = cntr
            else:
                if prev_char is not None:
                    char_count[prev_char] = cntr
            cntr = 1
        else:
            cntr += 1
        prev_char = cur_char
    if prev_char in char_count:
        if char_count[prev_char] < cntr:
            char_count[prev_char] = cntr
    else:
        char_count[prev_char] = cntr

    return char_count


print(counter(string))
