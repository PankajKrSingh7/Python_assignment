
def capturing_using_recursion(r,c,rows,cols): 
        if (r<0 or r==rows or c<0 or c==cols or board[r][c]!="O"):
            return 
        board[r][c]="#"
        capturing_using_recursion(r+1,c,rows,cols)
        capturing_using_recursion(r-1,c,rows,cols)
        capturing_using_recursion(r,c+1,rows,cols)
        capturing_using_recursion(r,c-1,rows,cols)

def solve(board):
        rows=len(board) 
        cols=len(board[0])

        #(DFS)capture unsurrounded region(0->#) starting from boundry Os 
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r==0 or r==rows-1 or c==0 or c==cols-1):
                    capturing_using_recursion(r,c,rows,cols)

        #capture remaining  surrounded region(0->X)
        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if board[r][c]=="O":
                    board[r][c]="X" 

        #uncapture unsurrounded region from # to O(#->0)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="#":
                    board[r][c]="O"



# Driver code
if __name__ == '__main__':
 
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(f"Original Matrix: {board}")
 
    (board)

    print(f"Matrix After Capture: {board}") 
 
    
