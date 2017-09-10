import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other!'

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern, text):
        print("Match")
    else:
        print("no match")

# Notice that re.search returns a regular expression match object.
match = re.search('term1', text)
print(type(match))


# Splitting a string by a character
split_term = '@'
email = 'user@gmail.com'

print(re.split(split_term, email))


print(re.findall('match', 'test phrase match in match middle'))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd...ssddd..ssdddsd...ds..dddssss.sddd'

test_patterns = ['sd*']  # Find s followed by 0 or more d's.

multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd+']  # Find s followed by 1 or more d's.
multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd{3}']  # Find s followed by 3 d's.
multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd{1,3}']  # Find s followed by 1 or 3 d's.
multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[^!.?]+']
multi_re_find(test_patterns, test_phrase)

