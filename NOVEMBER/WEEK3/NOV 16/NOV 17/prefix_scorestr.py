
def prefix_scoresum(words):
    total = 0

    for word in words:
        total = total + len(word)

    children = [[-1] * 26 for i in range(total + 1)]
    count = [0] * (total + 1)

    node_count = 0

  
    for word in words:
        node = 0

        for j in range(len(word)):
            k = ord(word[j]) - ord('a')

            if children[node][k] == -1:
                node_count = node_count + 1
                children[node][k] = node_count

            node = children[node][k]
            count[node] = count[node] + 1

    ans = [0] * len(words)

    for i in range(len(words)):
        node = 0
        score = 0

        for j in range(len(words[i])):
            k = ord(words[i][j]) - ord('a')

            node = children[node][k]
            score = score + count[node]

        ans[i] = score

    return ans



words = ["abc", "ab", "bc", "b"]

answer = prefix_scoresum(words)

print("Output:", answer)
