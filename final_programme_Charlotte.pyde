import random
def setup():
    global player1, player2, diceVal, current_position1, current_position2, boardImage, player1Image, player2Image, help1Image, help2Image
    global current_position1, current_position2, startbutton, helpbutton, game_mode, sandlbanner, snake1Image, ladder1Image
    global startButton, helpButton, player_1, player_2, player_1_turn, player_2_turn, player_1_score, player_2_score
    global dice_1, dice_2, alphabet, dice_bounds, diceImage, player1Image, player2Image
    global rows, cols, boardList, board_info, nextButton, previousButton, scoreList
    global ball_y, ball_incr, splitball_x1, splitball_x2, splitball_x3, splitball_y, up
    
    size( 1000, 1100 )
    player_1 = ''
    player_2 = ''
    diceVal = 0
    board_info = []

    player_1_turn = True
    player_2_turn = False
    player_1_score = 0
    player_2_score = 0
    
    dice_1 = 0
    scoreList = [player_1_score, player_2_score]
    dice_bounds = [[0, 850, 200, 200], [800, 850, 200, 200]]
    
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwxyz1234567890'
    
    #load image#
    boardImage = loadImage("board.PNG")
    player1Image = loadImage("player1.png")
    player2Image = loadImage("player2.png")
    sandlbanner = loadImage("sandlbanner.png")
    snake1Image = loadImage("snake_1.png")
    ladder1Image = loadImage("ladder_1.png")
    diceImage = loadImage("dice.png")
    help1Image = loadImage("help1.png")
    help2Image = loadImage("help2.png")
 
    diceImage.resize(1200, 200)
    
    current_position1 = 0
    current_position2 = 0
    
    rows = 5
    cols = 6
    sizeX = 160
    sizeY = 175
    
    ball_y = 600
    ball_incr = 15
    splitball_x1 = 475
    splitball_x2 = 475
    splitball_x3 = 475
    splitball_y = 1200
    up = True
    
    # ladder start --> ls
    # ladder end --> le
    # snake tail --> st
    # snake head --> sh
    
    boardList = ['st27', '', 'ls3', 'st17', 'ls5', '', 
                  'st19', 'le5', 'st21', '', 'ls11', '', 
                 '', '', '', '', 'sh17', '', 
                 'sh19', 'ls20', 'sh21', 'le3', '', '',
                 '', 'le11', 'sh27', '', 'le20', '' ]
            
    startButton = [200, 800, 200, 100]
    helpButton = [700, 800, 200, 100]
    nextButton = [700, 900, 200, 100]
    previousButton = [200, 900, 200, 100]
    
    game_mode = 'start'
    
    load_board(board_info, rows, cols, sizeX, sizeY)
 
def load_board(board_info, rows, cols, sizeX, sizeY):
    for i in range (rows):
        temp = []
        for j in range(cols):
            x = j * sizeX
            y = 850 - (i * sizeY)
            temp.append([x,y])
        
        if i % 2 !=0:
            temp.reverse()    
        board_info.append(temp)
    print(board_info)        
 
    return board_info
    
    
def mousePressed():
    global game_mode, player_1_score, player_2_score, player_1_turn, player_2_turn, dice_1, dice_2, diceVal
    if game_mode == 'start':
        if (mouseX >= startButton[0] and mouseX <= (startButton[0]+startButton[2]) and mouseY >= startButton[1] and mouseY <= (startButton[1]+startButton[3])):
                game_mode = 'game'
                player_1_turn = True
                player_2_turn = False
        if (mouseX >= helpButton[0] and mouseX <= (helpButton[0]+helpButton[2]) and mouseY >= helpButton[1] and mouseY <= (helpButton[1]+helpButton[3])):
                game_mode = 'help'
                
    if game_mode == "help":
        image(help1Image, 0, 300, 1000, 300)
        if (mouseX >= nextButton[0] and mouseX <= (nextButton[0]+helpButton[2]) and mouseY >= nextButton[1] and mouseY <= (nextButton[1]+nextButton[3])):
            game_mode = "next"
            
    if game_mode == "next":        
        if (mouseX >= previousButton[0] and mouseX <= (previousButton[0]+previousButton[2]) and mouseY >= previousButton[1] and mouseY <= (previousButton[1]+previousButton[3])):
            game_mode = "start"
    
    if game_mode == 'game':
        if (dice_bounds[0][0] <= mouseX <= dice_bounds[0][2]) and (dice_bounds[0][1] <= mouseY <= dice_bounds[0][1] + dice_bounds[0][3]):
            diceVal = random. randint(1, 6)
            if player_1_turn == True:
                player_1_score += diceVal
                player_1_turn = False
                player_2_turn = True
                
                keyMove()
                
            else:
                player_2_score += diceVal
                player_2_turn = False
                player_1_turn = True   
                
                keyMove()
                
                
def keyMove():
    image(player1Image, board_info[player_1_col][player_1_row][0]+80,board_info[(player_1_col)][player_1_row][1]-100,45,85)
    image(player2Image, board_info[player_2_col][player_2_row][0]+90,board_info[(player_2_col)][player_2_row][1]-90,45,85)
    delay(650)
    boardList_process()
    image(player1Image, board_info[player_1_col][player_1_row][0]+80,board_info[(player_1_col)][player_1_row][1]-100,45,85)
    image(player2Image, board_info[player_2_col][player_2_row][0]+90,board_info[(player_2_col)][player_2_row][1]-90,45,85)            
            
    
def draw():
    global game_mode, player_1, player_2, diceVal, player_1_score, player_2_score, player_1_col, player_2_col, player_1_row, player_2_row, scoreList
    
    background(0)
    
    if player_1_score>=29 or player_2_score >= 29:
        game_mode = 'end'   
         
    if game_mode == 'start':
        
        textSize(36)
        text("player 1 name: ", 100, 950)
        text(player_1, 500,950)
        
        text("player 2 name: ", 100, 1050)
        text(player_2, 500, 1050)
        
        fill(255)
        rect(200, 800, 200, 100)
        fill(255, 0, 0)
        textSize(45)
        text("Start", 250, 870)
        
        fill(255)
        rect(700, 800, 200, 100)
        fill(0, 0, 255)
        textSize(45)
        text("Help", 750, 870)
        
        image(sandlbanner, 375, 75, 225, 600)
        image(snake1Image, 0, 75, 300, 600)
        image(ladder1Image, 650, 75, 450, 600)
        
    if game_mode == "help":
        fill(255)
        rect(700, 900, 200, 100)
        fill(0, 0, 255)
        textSize(45)
        text("Next", 750, 970)
        image(help1Image, 0, 300, 1000, 300)
    
    if game_mode == "next":
        image(help2Image, 0, 250, 1000, 500)
        fill(255)
        rect(200, 900, 300, 100)
        fill(255, 0, 0)
        textSize(45)
        text("Previous", 250, 970)

        
    if game_mode == 'game':
        image(boardImage, 0, 0, 1000, 850)
        
        #diceImage#
        diceImage.resize(1200, 200)
        image(diceImage.get(0, 0, 200, 200), 0, 850) 
   
        #chess#
        player_1_row = player_1_score %(5 +1)
        player_1_col = player_1_score //6 
        player_2_row = player_2_score % (5 +1) 
        player_2_col = player_2_score //6
       
        #dice#
        diceFace = diceImage.get((diceVal - 1) * 200, 0, 200, 200)
        image(diceFace, 0, 850)
        
         #name and score text#
        scoreList = [player_1_score, player_2_score]
        scoreList = bubbleSort_opt (scoreList)
        if scoreList[-1] == player_1_score:
            fill(255)
            textSize(36)
            text(player_1 + " is bigger.", 450, 1000)
            
        else:
            fill(255)
            textSize(36)
            text(player_2 + " is bigger.", 450, 1050)
            
           
        
        fill(255)
        textSize(36)
        text(player_1 + ': ' + str(player_1_score+1), 700, 950)
        text(player_2 + ': ' + str(player_2_score+1), 700, 1050)   
        keyMove()
    
    if game_mode == 'end':
        fire_works()
        
     
def keyPressed():
    global player_1_score, player_2_score, player_2_turn, player_1_turn, player_1, player_2
    global dice_1, dice_2, game_mode
    
    if game_mode == 'start' and player_1_turn:
        try:
            if key in alphabet:
                player_1 += key
            if key == ENTER:
                player_1_turn = False
                player_2_turn = True
                
        except TypeError: 
            pass           
 
    
    if game_mode == 'start' and player_2_turn:
        try:    
            if key in alphabet:
                player_2 += key
                
            if key == ENTER and player_2 != '' :
                player_1_turn = True
                player_2_turn = False
                game_mode = 'game'
                
        except TypeError:
            pass        
    
    if game_mode == 'game':
        print("Game starts")
        
        
def boardList_process():
    global player_1_score, player_2_score
    
    if player_1_turn:
        p1 = boardList[player_1_score]
        snake_ladder = p1[:2]
        num = p1[2:]
        
        if snake_ladder == 'ls':
            player_1_score = boardList.index('le' + num)
            print(p1, boardList.index('le' + num))
            
        if snake_ladder == 'sh':
            player_1_score = boardList.index('st' + num)
    
    if player_2_turn:
        p2 = boardList[player_2_score]
        snake_ladder = p2[:2]
        num = p2[2:]
        
        if snake_ladder == 'ls':
            player_2_score = boardList.index('le' + num)
            print(p2, boardList.index('le' + num))
        if snake_ladder == 'sh':
            player_2_score = boardList.index('st' + num)
            print(p2, boardList.index('st' + num))
            
    return player_1_score, player_2_score
        
        
    
 
def fire_works():
    global ball_y, ball_incr, splitball_x1, splitball_x2, splitball_x3, splitball_y, up
    
    background(0)
    fill(255)
    textSize(36)
        
    if player_1_score > player_2_score:
        text(player_1 +" wins", 300, 500)
    else:
        text(player_2 + " wins", 300, 500)
        
    base_x = 450
    base_y = 800
    
    
    if ball_y <=0:
        ball_incr = -ball_incr
    
    if ball_y >= 1200:
        up = False
    
    if up:
        ball_y -= ball_incr
        rect(base_x, 600, 50,200)
        ellipse(base_x + 25, ball_y, 45,45)
        
    else:
        splitball_x1 += 10
        splitball_x3 -= 10
        splitball_y -= 15
        ellipse (splitball_x1, splitball_y, 15, 15)
        ellipse (splitball_x2, splitball_y, 15, 15)
        ellipse (splitball_x3, splitball_y, 15, 15)
        
def bubbleSort_opt (lista):
  switch  = False
  for j in range (1, len(lista)):
    switch  = True
    limit = len(lista)- j
    for i in range (limit):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            switch  = False
    if switch:
        break
 
  return lista
