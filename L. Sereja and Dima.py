def check(n, N):
    start = 0
    end = n - 1
    player1_score = 0
    player2_score = 0
    player = 0  # player 0 for player1 and player 1 for player2

    while start <= end:
        if N[start] >= N[end]:
            max_num = N[start]
            start += 1
        else:
            max_num = N[end]
            end -= 1

        if player % 2 == 0:
            player1_score += max_num
        else:
            player2_score += max_num

        player += 1  # Alternate player

    return player1_score, player2_score

n = int(input())
N = list(map(int, input().split()))
result = check(n, N)
print(' '.join(map(str,result)))
