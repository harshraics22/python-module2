from collections import Counter

with open('sample.txt') as f:
    word_count = Counter(f.read().split())

print(word_count)