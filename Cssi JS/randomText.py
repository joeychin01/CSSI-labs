# length = raw_input("Please give how long your random sentance is going to be: ")
# keyLength = raw_input("Please give how long your seed is going to be (max 10): ")
length = 10
keyLength = 2
import random

def read_process_data():
    with open('res/hamlet.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content

wrd = read_process_data().split(" ")


word  = ["to", "be", "or", "not", "to", "be", "hello"]



map = {}
seed = []
for i in range(int(keyLength)):
    seed.append(word[i])
print(seed)
for i in range(len(word)):
    if tuple(seed) in map.keys():
        # map[tuple(seed)] = map[tuple(seed)].append(word[i+int(keyLength)%len(word)])
        arr = map[tuple(seed)]
        arr.append(word[i+int(keyLength)%len(word)])
        map[tuple(seed)] = arr

    else:
        map[tuple(seed)] = [word[(i+int(keyLength))%len(word)]]
    seed.append(word[(i+int(keyLength))%len(word)])
    seed.pop(0)
    # newKey = (word[i], word[i+length])
    #
    # if word[i] in map.keys():
    #     # map[word[i]] = map[(word[i])].append(word[i+1])
    #     arr = map[word[i]]
    #     arr.append(word[i+1])
    #     map[word[i]] = arr
    # else:
    #     map[word[i]] = [word[i+1]]
print(map)
startKey = []
randStart = random.randint(0, len(map.keys())) - 1
for i in range(randStart, (randStart + keyLength) % len(word)):
    startKey.append(word[i])
lastKey = startKey
for i in range(int(length)):
    possVal = map[lastKey]
    randNum = random.randint(0, len(possVal)-1)
    nextWord = possVal[randNum]
    lastKey = nextWord
    str = str + " " +nextWord
print(str)
