string = "Huba buba is the best"
count = 0
char = 'a'

for x in string:
    if x == char:
        count += 1

print(count)


s = "The quick brown fox jumps over the lazy dog."
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))