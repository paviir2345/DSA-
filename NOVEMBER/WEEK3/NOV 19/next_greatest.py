def next_greatest(letters,target):
    for i in range(len(letters)):
        if letters[i]>target:
            return letters[i]
    return[0]

letters = ["c", "f","j"]
target = "a"

print(next_greatest(letters,target))