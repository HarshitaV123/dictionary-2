sentence=input("Enter a sentence: ").lower()
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
for ch in sentence:
    if ch in vowels:
        vowels[ch]=vowels[ch]+1
print(vowels)