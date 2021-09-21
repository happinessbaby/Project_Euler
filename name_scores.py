import string


def create_alphabet():
    s = string.ascii_uppercase
    alphabet = list(s)
    al_scores, i = {}, 1
    for num in alphabet:
        al_scores[num] = i
        i += 1
    return al_scores

def read_file():
    names = []
    with open('p022_names.txt', 'r') as file:
        for line in file:
            n = line.split(",")
            for name in n:
                name = name.strip('\"')
                names.append(name)
    file.close()
    return names

def add_scores():
    al_scores = create_alphabet()
    sorted_names = sorted(read_file())
    order = 1
    total_scores = 0
    for name in sorted_names:
        score = 0
        for char in name:
            score += al_scores[char]
        score = score * order
        total_scores += score
        order += 1
    return total_scores

print(add_scores())
