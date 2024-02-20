triangle_nums = [0.5 * i * (i + 1) for i in range(1, 40)]
triangle_nums = set(triangle_nums)
print(triangle_nums)


def alpha_score(word):
    return sum(ord(letter) - 96 for letter in word)


with open('0042_words.txt', 'r+') as f:
    words = f.read().split(',')
    words = [word[1:-1].lower() for word in words]
    print(len(words))
    print(sum(1 for word in words if alpha_score(word) in triangle_nums))
