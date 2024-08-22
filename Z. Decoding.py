def decoding(n, s):
    output = []
    for i in range(n):
        remaining_length = n - i
        if remaining_length % 2 == 0:
            output.insert(0, s[i])   # Insert at the start when remaining length is even
        else:
            output.append(s[i])      # Append to the end when remaining length is odd
    return ''.join(output)

n = int(input())
s = input()
result = decoding(n, s)
print(result)

