
sentence = "Ram is good boy"
#out = "boy good is ram"

# with and without split

def revrse_word_of_sentence_with_split(sentence):
	sent_word = sentence.split()
	rev_words = sent_word[::-1]
	sent = " ".join(rev_words)
	return sent


def reverse_words_in_a_string(sentence):
    rev = ""
    temp = ""
    for st in sentence:
        if st == " ":
            rev = temp + " " + rev
            temp = ""
        else:
            temp += st
    if temp != "":
    	rev = temp +" "+ rev
    return rev





print(revrse_word_of_sentence_with_split(sentence))
print(reverse_words_in_a_string(sentence))