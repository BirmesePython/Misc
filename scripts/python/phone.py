PHONE_NUM = '6825743296'
WORDS = set(open('words_alpha.txt').read().split())
FOUND_WORDS = []
NUMS_TO_LETTERS = [
    [],
    [],
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
    ['j','k','l'],
    ['m','n','o'],
    ['p','q','r','s'],
    ['t','u','v'],
    ['w','x','y','z']
]

phoneNumber = PHONE_NUM.replace('1', '').replace('0', '')
theseLetters = [NUMS_TO_LETTERS[int(num)] for num in phoneNumber]

def isWord(word):
    return word in WORDS

def wordRecurse(curStr, idx):
    if isWord(curStr):
        FOUND_WORDS.append(curStr)

    if idx >= len(theseLetters):
        return

    for ch in theseLetters[idx]:
        wordRecurse(curStr + ch, idx + 1)

wordRecurse('', 0)

print(set(FOUND_WORDS))
