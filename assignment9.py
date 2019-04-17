import sys
import operator as op

if len(sys.argv) != 3:
	print("Error: Incorrect number of arguments. You must include exactly two files.")
	exit(1)

erasures = ['\n','\t','.','?','!',',',';',':','\'','\"','(',')']
words = []
skip_words = []
occurrences = {} # contains how many times a given word pair is seen

# read in skip_Words
with open(sys.argv[2], 'r') as skip_file:
	for line in skip_file:
		skip_words.extend(line.split(','))

# read in words, removing punctuation and lowercasing all words.
with open(sys.argv[1], 'r') as story_file:
	for line in story_file:
		line = line.casefold()
		for char in erasures:
			line = line.replace(char, '')
		words.extend(line.split())

words.pop() # remove the EOF

# remove skip_words from words
for skip_word in skip_words:
	words = [word for word in words if word != skip_word]

for a,b in zip(words[:-1],words[1:]):
	if (a + " " + b) in occurrences:
		occurrences[a + " " + b] += 1
	else:
		occurrences[a + " " + b] = 1

pairs = sorted(occurrences.items(), key=op.itemgetter(1), reverse=True)

print("Story file name: " + sys.argv[1])
print("Skip word file name: " + sys.argv[2])
print("Skip words: ", end='')
print(skip_words)
print("The five most frequently occurring word pairs are: ")
for i in range(5):
	print(pairs[i])

			