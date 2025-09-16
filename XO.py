def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    
    return None

def is_board_full(board):
    return ' ' not in board

def main():
    board = [' '] * 9
    current_player = 'X'
    
    print("XO Game Started!")
    print("Use numbers 1-9 to select cells:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    while True:
        print_board(board)
        try:
            position = int(input(f"Player {current_player}'s turn. Choose a cell (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1-9!")
            continue
            
        if position < 0 or position > 8:
            print("Number must be between 1-9!")
            continue
            
        if board[position] != ' ':
            print("This cell is already taken!")
            continue
            
        board[position] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()