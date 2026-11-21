
def countMatches(items, ruleKey, ruleValue):
    count = 0

    for i in range(len(items)):

        if ruleKey == "type":
            if items[i][0] == ruleValue:
                count = count + 1

        elif ruleKey == "color":
            if items[i][1] == ruleValue:
                count = count + 1

        elif ruleKey == "name":
            if items[i][2] == ruleValue:
                count = count + 1

    return count


# Main program
items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]

ruleKey = "color"
ruleValue = "silver"

answer = countMatches(items, ruleKey, ruleValue)

print("Output:", answer)
