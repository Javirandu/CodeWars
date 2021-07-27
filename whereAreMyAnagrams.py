"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none
"""

"""
//coments//
For loop  will save each word as a posible result. Each word will be listed
in order to sort them easily and then, they will be compared one by one with the
main word, if it's true, the posible_result we'll be appended into a list.
"""
def anagrams(word, words):
    main_word_listed = list(word)
    main_word_listed.sort()
    main_word_sorted=''.join(main_word_listed)
    words_list_sorted = ''
    result=[]

    for i in words:
        posible_result= i
        words_listed = list(i)
        words_listed.sort()
        words_sorted=''.join(words_listed)
        if main_word_sorted == words_sorted:
            result.append(posible_result)
    return result 


