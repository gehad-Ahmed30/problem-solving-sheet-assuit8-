def check(s):
    s = list(s)  # Convert string to list for mutability
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] == "?" and s[right] == "?":
            s[left] = s[right] = 'a'
        elif s[left] == "?":
            s[left] = s[right]
        elif s[right] == "?":
            s[right] = s[left]
        elif s[left] != s[right]:
            return -1
        
        left += 1
        right -= 1

    return ''.join(s)

s = input()
result = check(s)
if result == -1:
    print(result)
else:
    print(result)
