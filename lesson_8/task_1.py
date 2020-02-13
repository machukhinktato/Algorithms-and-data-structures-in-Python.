# task 1
# program to check each substring in entered phrase or in another input
import hashlib


def substring_counter(text):
    hashed_set = set()
    substring_set = set()

    for sub_length in range(1, len(text)):
        for i in range(len(text)):
            hashed_sub = hashlib.sha1(text[i:i + sub_length]
                                      .encode('utf-8')).hexdigest()
            hashed_set.add(hashed_sub)
            substring_set.add(text[i:i + sub_length])
    return f'In entered text - "{text}" found {len(substring_set)}' \
           f' unique substrings: \n{substring_set}'


def task_1_launcher():
    text = input('Please, enter any kind of text, you can use a different '
                 'symbols: ')
    print(f' {substring_counter(text)}')


task_1_launcher()

# Please, enter any kind of text, you can use different symbols: i love python
# In entered text - "i love python" found 88 unique substrings:
# {'love pytho', 'n', ' python', ' love p', 'i love ', 'ython', 'yth', 've py',
# 'thon', 'e py', ' l', 'i love py', ' py', 'ove python', ' love pytho', 'tho',
# 've pyth', ' love python', 've p', 'on', 'i lo', 'e pytho', 'ove', ' p', 'hon',
# 'python', 've pytho', 'pyth', ' pytho', 'love python', ' lov', 'ove py', 've',
# 'e python', ' pyt', 't', 've python', 'o', ' love pyth', 'ove pyt', 'e pyt',
# 'i love', 'ov', ' pyth', ' love py', 'pytho', 'ove p', 'love py', 'i l',
# ' love', 'e p', 'e', 'ove ', 'p', 'ytho', 'v', 've ', 'i love pytho', 'pyt',
# ' lo', 'ove pyth', 'love pyth', 'ove pytho', 'e pyth', 'yt', 'py', 'i love p',
# 'love pyt', 'love', 'y', 'love p', 'i love pyth', 'lov', 'i lov', 'i love pyt',
# 'ho', 'l', 'th', ' love ', ' love pyt', 'h', 'i ', 'lo', 'e ', 'i', ' ',
# 've pyt', 'love '}
