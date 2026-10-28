
def eatingspeed(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        hours = 0

        for bananas in piles:
            hours = hours + (bananas + mid - 1) // mid

        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
h = 8
print(eatingspeed(piles, h))
