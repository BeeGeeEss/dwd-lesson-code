text = ("A random paragraph can also be an excellent way for a writer to tackle writers' block. Writing block can often happen due to being stuck with a current project that the writer is trying to complete. By inserting a completely random paragraph from which to begin, it can take down some of the issues that may have been causing the writers' block in the first place.")



text = text.replace("'", " ")
text = text.replace(".", " ")
text = text.replace(",", " ")

words = text.lower().strip().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nWord Frequency Dictionary:")
print(word_counts)

print("\nFormatted Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")


print(words.sort())