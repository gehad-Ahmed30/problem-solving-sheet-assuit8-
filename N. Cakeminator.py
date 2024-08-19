def max_cake_cells(r, c, cake_grid):
    eatable_rows = [True] * r
    eatable_cols = [True] * c
    
    for i in range(r):
        if 'S' in cake_grid[i]:
            eatable_rows[i] = False
    
    for j in range(c):
        if any(cake_grid[i][j] == 'S' for i in range(r)):
            eatable_cols[j] = False
    
    total_cells = 0
    for i in range(r):
        if eatable_rows[i]:
            total_cells += c
    
    for j in range(c):
        if eatable_cols[j]:
            if not eatable_rows[i] and cake_grid[i][j] == '.':
                    total_cells += 1
    
    return total_cells

x, y = map(int, input().split())
cake_grid = []
for _ in range(x):
    cake_grid.append(input().strip())

print(max_cake_cells(x, y, cake_grid))




