board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(f"Original Matrix: {board}")

# we can also take the matrix as user input 
'''
m = int(input("Number of rows:"))
n = int(input("Number of columns:"))

bord=[]

for i in range(m):
    data = []
    print("Enter",i," row data")
    for j in range(n):
        s = input()
        data.append(s)
        
    board.append(data)
'''
# m and n are row and columns of board respectively
m = len(board)
n = len(board[0])

# DFS algorithm to move on the Board and make changes 
def dfs(board,r,c):
    if(r<=0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]=='X'):
        return
    board[r][c] ='#'
    dfs(board,r+1,c)
    dfs(board,r-1,c)
    dfs(board,r,c+1)
    dfs(board,r,c-1)

# Running DFS on boundry 'O' and changing them to '#' since it is not surrounded by 'X'
for r in range(m):
    for c in range(n):
        if(board[r][c] == 'O' and (r in [0,m-1] or c in [0,n-1])):
            dfs(board,r,c)

# Now all remaining 'O' are surrounded by 'X' so we change them to 'X'
for r in range(m):
    for c in range(n):
        if(board[r][c] == 'O'):
            board[r][c] = 'X'

# Here converting '#' back to 'O'           
for r in range(m):
    for c in range(n):
        if(board[r][c] == '#'):
            board[r][c] = 'O'

print(f"Matrix After Capture: {board}")            
