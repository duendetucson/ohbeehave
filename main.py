import sys
from turtle import pos

args = sys.argv
if len(args) < 7:
    print('Please enter all 7 letters of the puzzle')
    quit()

center_letter = args[1]
print("Center letter: %s" % center_letter)

match_letters = set(sys.argv[1:8])
print("Match letters: %s" % match_letters)
# quit()
f = '/usr/share/dict/words'
words_min_four_chars = set([])
matching_words = set([])
try:
    for word in open(f, 'r'):
        word_length = len(word)
        if word_length > 3 and word.find(center_letter) > 0:
            words_min_four_chars.add(word.strip("\n").lower())
except IOError:
    print(f, "not found!")
    quit()

for possible_match in words_min_four_chars:
    matching_word_letters = set(possible_match)
    # print("matching_word_letters: %s" % matching_word_letters)
    mismatch_count = len(matching_word_letters.difference(match_letters))
    # print("%s mismatches" % mismatch_count)
    if (len(matching_word_letters.difference(match_letters)) == 0):
        matching_words.add(possible_match)
match_count = len(matching_words)
if len(matching_words) > 0:
    print('Found %s words matching the letters %s' %
          (match_count, match_letters))
    for matching_word in matching_words:
        print(matching_word)
else:
    print('No words matching the letters %s were found' %
          match_letters)
