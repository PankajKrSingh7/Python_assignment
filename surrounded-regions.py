board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(f"Original Matrix: {board}")
'''
m = int(input("Number of rows:"))
n = int(input("Number of columns:"))

lst=[]

for i in range(m):
    data = []
    print("Enter",i," row data")
    for j in range(n):
        s = input()
        data.append(s)
        
    lst.append(data)
'''
m = len(board)
n = len(board[0])

def dfs(board,r,c):
    if(r<=0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c]=='X'):
        return
    board[r][c] ='#'
    dfs(board,r+1,c)
    dfs(board,r-1,c)
    dfs(board,r,c+1)
    dfs(board,r,c-1)


for r in range(m):
    for c in range(n):
        if(board[r][c] == 'O' and (r in [0,m-1] or c in [0,n-1])):
            dfs(board,r,c)

for r in range(m):
    for c in range(n):
        if(board[r][c] == 'O'):
            board[r][c] = 'X'
            
for r in range(m):
    for c in range(n):
        if(board[r][c] == '#'):
            board[r][c] = 'O'

print(f"Matrix After Capture: {board}")            
