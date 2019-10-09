#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''The board has the following structure:

A1   B1   C1
A2   B2   C2
A3   B3   C3

'''


# In[2]:


import numpy as np


# In[3]:


#Define board postions as matrix indices
pos_index = {'a1': [0,0], 'a2': [1,0], 'a3': [2,0], 'b1': [0,1], 'b2': [1,1], 'b3': [2,1], 'c1': [0,2], 
             'c2': [1,2], 'c3': [2,2]}


# In[7]:


#Define the empty tic tac toe board.
game_positions = np.matrix([['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']])
game_board = np.matrix([[300]*3]*3)
visual_game_board = np.matrix([[None]*3]*3)
player_id = 1
end=False
break_stat=0
count=0

while end == False:
    
    if count==0: 
        print('Welcome to Tic Tac Toe! \nStart entering positions on the game board below to get stated')
        print('If you would like to leave the game at any point type exit into the command prompt')
        print(game_positions)
        count+=1
    
    if player_id == 1: 
        marker=1 
        player_code = 'x'
    else: 
        marker=0
        player_code = 'o'
    
    #Ask the current player to pick a position
    position = input("Player "+ player_code +" Choose a Positon:").lower()
    
    #Testing exit option
    if position == 'exit': break
    
    #Check if the game board position is valid
    try:
        pos_index[position]
    except: 
        print('Not a valid game board position. Choose another value')
        continue
    
    position_pick = game_board[pos_index[position][0], pos_index[position][1]]
    
    if position_pick != 300: 
        print('This position has already been picked. Pick another position')
        continue
    else:
        game_board[pos_index[position][0], pos_index[position][1]] = marker
        visual_game_board[pos_index[position][0], pos_index[position][1]] = player_code

    print('\n')
    print(visual_game_board)
     #####Begin game status checking: #######
    
   
    row1_x = game_board[0].sum() == 3
    
    row1_o = game_board[0].sum() == 0
    
    row2_x = game_board[1].sum() == 3
    row2_o = game_board[1].sum() == 0
    
    row3_x = game_board[2].sum()== 3
    row3_o = game_board[2].sum()== 0
    
    col1_x = game_board[:,0].sum()== 3
    col1_o = game_board[:,0].sum()== 0
    
    col2_x = game_board[:,1].sum()== 3
    col2_o = game_board[:,1].sum()== 0
    
    col3_x = game_board[:,2].sum()== 3
    col3_o = game_board[:,2].sum()== 0
    
    diag1_x = game_board.diagonal().sum()== 3
    diag1_o = game_board.diagonal().sum()== 0
    
    diag2 = []
    
    for r,c in zip(range(0,3), range(2,-1,-1)):
        diag2.append(game_board[r,c])

    diag2_x = sum(diag2)== 3
    diag2_o = sum(diag2)== 0
    
    x_conditions = [row1_x, row2_x, row3_x, col1_x, col2_x, col3_x, diag1_x, diag2_x]
    o_conditions = [row1_o, row2_o, row3_o, col1_o, col2_o, col3_o, diag1_o, diag2_o]
    
    for i in x_conditions:
        if i == True:
            status = '\n Player X has won!'
            message = 'Sorry player O, you suck :('
            break_stat = 1
    
    for i in o_conditions:
        if i == True:
            status = '\n Player O has won!'
            message = 'Sorry player X, you suck :('
            break_stat = 1
    
    if game_board.sum() <= 300: 
        status = '\n This is a tie game. No player has won. Start a new game and try again!'
        message= 'Start a new game and try again!'
        break
        
    
    if break_stat == 1: break 
        
    player_id *= -1
    
    
print(status)
print(message)

# Made a change here

