import json
import difflib

fname = open('data.json').read()
data = json.loads(fname)

def getMeaning(w):
    key = w.lower()
    if key in data:
        return data[key]
    else:
        similarWord = difflib.get_close_matches(key,data.keys(), cutoff=0.8)
        if len(similarWord) <= 0 : return "Entered word doesn't exist"
        i = 0
        showNext = True
        while showNext and i < len(similarWord):
            print("Did you mean" , similarWord[i], "? Y or N")
            answer = input("")
            if answer == 'Y' or answer == 'y':
                showNext = False
                print(similarWord[i])
                meaning = getMeaning(similarWord[i])
                return meaning
            elif answer == 'N' or answer =='n':
                i += 1
            else:
                return "We didnt understand your entry"
        if showNext:
            return "Entered word doesn't exist. Please check the spelling"
        else:
            return
        

word = input("Enter a word ")
output = getMeaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)





