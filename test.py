s=list(input().split())
for i in range(len(s)):
    if s[i][-1] != s[i+1][0]:
        print("y")
  