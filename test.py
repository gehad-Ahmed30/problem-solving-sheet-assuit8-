s=list(input().strip())
for i in s:
  if s[i]==s[::-1]:
    print(s)