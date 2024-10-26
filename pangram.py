sentence=input("Enter a sentence: ").lower()
letters="abcdefghijklmnopqrstuvwxyz"
def pangram(sentence):
    for ch in letters:
        if ch not in sentence:
            return False
    return True        
if pangram(sentence):
    print("This sentence is a pangram!")
else:
    print("This sentence is not a pangram!")
