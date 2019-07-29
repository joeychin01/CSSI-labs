def read_process_data():
    with open('res/dict1.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content
# def charMap(word):
#     result = {'m': 0, 'p': 0, 'i': 0, 'n': 0, 'd': 0, 'w': 0, 'k': 0, 'y': 0, 's': 0, 'b': 0, 'h': 0, 't': 0, 'u': 0, 'q': 0, 'g': 0, 'l': 0, 'e': 0, 'a': 0, 'j': 0, 'c': 0, 'o': 0, 'f': 0, 'v': 0, 'x': 0, 'z': 0, 'r': 0}
#     for letter in word:
#         if letter in result.keys():
#             result[letter] = result[letter] +  1
#     return result
# def isInside(word1, word2):
#     word1map = charMap(word1)
#     word2map = charMap(word2)
#     for letter in word1map.keys():
#         if word1map[letter] > word2map[letter]:
#             return False
#     return True
# # letters = raw_input("Please enter your phrase to anagram: ")
# # letters = letters.replace(" ", "")
# # letters = letters.lower()
# # letters = ''.join(sorted(letters))
# dict = read_process_data()
#
# def findAnagrams(word, dict):
#     nextDict = []
#     print(dict)
#     for words in dict:
#         if(isInside(word, words)):
#             nextDict.append(words)
#
#
# findAnagrams("barbarabush", dict)

dict = read_process_data().split()

def isPrefix(prefix, dict):    #if any word in dict starts with prefix
   st=0
   end=len(dict)-1
   while st<=end:
       mid=(st+end)/2
       curr=dict[mid]
       if len(prefix)<=len(curr) and curr[:len(prefix)]==prefix:
           return True
       elif prefix < curr:
           end=mid-1
       else:
           st=mid+1
   return False

bigList = []
def findAnagrams(commit, prefix, suffix):
    global bigList
    global dict
    if prefix == "" and suffix == "":
        if commit not in bigList:
            bigList.append(commit)
        return
    # if not isPrefix(prefix, dict):
    #     return
    if prefix in dict:
        findAnagrams(commit + [prefix], "", suffix)
    for char in suffix:
        findAnagrams(commit, prefix + char, removeLetterInside(suffix, char))

def find_anagram(commit, prefix, suffix):
   global big_list
   global dict
   if prefix == "" and suffix == "":
       if commit not in big_list:
           big_list.append(commit)
       return
   if not isPrefix(prefix, dict):
       return
   if prefix in dict:
       find_anagram(commit + [prefix], "", suffix)
   for char in suffix:
       find_anagram(commit, prefix + char, removeLetterInside(suffix, char))





def removeLetterInside(word, char):
    list = sorted(word)
    list.remove(char)
    finalString = ''
    for i in range(len(list)):
        finalString += list[i]
    return finalString

findAnagrams([], "", "barbarabush")
print(bigList)
