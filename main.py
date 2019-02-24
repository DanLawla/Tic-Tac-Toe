def print_board():
  print (board[0],'|',board[1],'|', board[2])
  print('--------')
  print (board[3],'|',board[4],'|',  board[5])
  print('--------')
  print (board[6],'|',board[7],'|',board[8])
  
def play_tic_tac_toe():
      num_turns = 1
      print_board()
      while num_turns <10:
        if check_winner()==True:
          break 
        if num_turns%2==1:
          print ('PLAYER 1 TURN:')
          x = int(input('Enter position'))
          while board[x]=='X' or board[x]=='O':
            print('Incorrect position')
            print ('PLAYER 1 TURN:')
            x = int(input('Enter position'))
          board[x]='X'
          num_turns+=1
        print_board()
        if check_winner()==True:
          break 
        if num_turns==10:
          print ('GAME IS A DRAW')
          break
        if num_turns%2==0:
          print ('PLAYER 2 TURN:')
          x = int(input('Enter position'))
          while board[x]=='X' or board[x]=='O':
            print('Incorrect position')
            print ('PLAYER 2 TURN:')
            x = int(input('Enter position'))
          board[x]='O'
          num_turns+=1
        print_board()
    
def check_winner():
  win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for x in win_combinations: 
    if board[x[0]] == board[x[1]] == board[x[2]] == 'X' :
      print('Player 1 Wins!')
      return True
    if board[x[0]]== board[x[1]] == board[x[2]] == 'O' :
      print('Player 2 Wins!')
      return True
      
board=[0,1,2,3,4,5,6,7,8]
play_tic_tac_toe()
