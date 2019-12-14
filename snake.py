#A more difficlut game mode or the snake game which includes snake food and posion, if the snake eats the poison then it loses a body part and loses score. what makes this game more difficult is the user does not know what the food and poison is.
#The game also speeds up as the snake gets longer
#Enjoy!



from tkinter import *
import random


def storefood():
        global food, foodX, foodY
        food = canvas.create_oval(0,0, 15,15, fill = "blue")

        foodX = random.randint(0, width-snakeSize)
        foodY = random.randint(0, height-snakeSize)
        canvas.move(food, foodX, foodY)


        
def growSnake():
        lastElement = len(snake) - 1
        lastPos = canvas.coords(snake[lastElement])
        snake.append(canvas.create_rectangle(0,0,snakeSize,snakeSize, fill = "#FDF3F3"))
        
        if (direction == "left"):
            canvas.coords(snake[lastElement+1], lastPos[0]+snakeSize, lastPos[1],
                          lastPos[2]+snakeSize, lastPos[3])
        elif (direction == "right"):
            canvas.coords(snake[lastElement+1], lastPos[0]-snakeSize, lastPos[1],
                          lastPos[2]-snakeSize, lastPos[3])
        elif (direction == "up"):
            canvas.coords(snake[lastElement+1], lastPos[0], lastPos[1]+snakeSize,
                          lastPos[2], lastPos[3]+snakeSize)
        elif (direction == "down"):
            canvas.coords(snake[lastElement+1], lastPos[0], lastPos[1]-snakeSize,
                          lastPos[2], lastPos[3]-snakeSize)

        global score

        score += 5
        txt = "score:" + str(score)


        canvas.itemconfigure(scoreText, text = txt)

def shrinkSnake():
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.remove(snake[lastElement])

    
    global score
    score -= 5
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)

    if score < 0:
            gameOver = True 
            score = 0 
            txt = "score:" + str(score)
            canvas.itemconfigure(scoreText, text=txt)
            canvas.create_text(width/2, height/2, fill = "white",
                                   font = "Times 20 italic bold", text = "Game Over!")
            sys.exit()
            

def moveFood():
        global food, foodX, foodY
        canvas.move(food, (foodX*(-1)), (foodY*(-1)))
        foodX = random.randint(0,width-snakeSize)
        foodY = random.randint(0,height-snakeSize)
        canvas.move(food, foodX, foodY)

def movePoison():
    global poison, poisonX, poisonY
    canvas.move(poison, (poisonX*(-1)), (poisonY*(-1)))
    poisonX = random.randint(0,width-snakeSize)
    poisonY = random.randint(0,height-snakeSize)
    canvas.move(poison, poisonX, poisonY)

def placePoison():
    global poison, poisonX, poisonY
    poison = canvas.create_oval(0,0, snakeSize, snakeSize,fill="blue" )
    poisonX = random.randint(0,width-snakeSize)
    poisonY = random.randint(0,height-snakeSize)
    canvas.move(poison, poisonX, poisonY)

        
def collision(a,b):
        if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
            return True
        return False

        
def moveSnake():
        canvas.pack()
        
        position=[]
        position.append(canvas.coords(snake[0]))

        if position [0][0] < 0:
            canvas.coords(snake[0], width, position[0][1], width-snakeSize, position[0][3])
        elif position [0][2]>width:
            canvas.coords(snake[0], 0-snakeSize, position[0][1],0, position[0][3])
        elif position[0][3] > height:
            canvas.coords(snake[0], position[0][0], 0 - snakeSize, position[0][2],0)
        elif position[0][1] < 0 :
            canvas.coords(snake[0], position[0][0], height, position[0][2], height-snakeSize)

        position.clear()
        position.append(canvas.coords(snake[0]))
        

        if direction == "left":
            canvas.move(snake[0], -snakeSize,0)
        elif direction == "right":
            canvas.move(snake[0], snakeSize,0)
        elif direction == "up":
            canvas.move(snake[0],0,-snakeSize)
        elif direction == "down":
            canvas.move(snake[0],0,snakeSize)

        
        headPos = canvas.coords(snake[0])
        foodPos = canvas.coords(food)
        poisonPos = canvas.coords(poison)



        if collision(headPos, foodPos):
                moveFood()
                growSnake()
                movePoison()

        elif collision(headPos, poisonPos):
                movePoison()
                shrinkSnake()
                moveFood()
        for i in range(1, len(snake)):
            if collision(headPos, canvas.coords(snake[i])):
                gameOver = True
                canvas.create_text(width/2, height/2, fill = "white",
                                   font = "Times 20 italic bold", text = "Game Over!")

        
        for i in range(1,len(snake)):
            position.append(canvas.coords(snake[i]))

        for i in range(len(snake)-1):
            canvas.coords(snake[i+1], position[i][0], position[i][1], position[i][2],
                          position[i][3])

        

    
                
                
                

        if 'gameOver' not in locals() and len(snake) < 3:
            window.after(50, moveSnake)

        if 'gameOver' not in locals() and len(snake) >= 3 and len(snake) < 6:
                window.after(30, moveSnake)
        if 'gameOver' not in locals() and len(snake) >= 6:
                window.after(20, moveSnake)
        
 


        
        
def pause(event):
        global direction
        direction = ""
        
def leftKey(event):
        global direction
        direction = "left"

def rightKey(event):
        global direction
        direction = "right"

def upKey(event):
        global direction
        direction = "up"

def downKey(event):
        global direction
        direction = "down"
        
def setWindowDimensions(w,h):
        window = Tk()
        window.title("snake game")

        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()

        x = (ws/2) - (w/2) #calculates the centre of the screen
        y = (hs/2) - (h/2)

        window.geometry('%dx%d+%d+%d' % (w,h,x,y))

       
        
        return window 


width = 600
height = 600
window = setWindowDimensions(width, height)
canvas = Canvas(window, bg = "black", width = width, height= height)
canvas2 = Canvas(window, bg = "blue", width = width, height= height)
snake = []
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize, snakeSize, snakeSize*2,snakeSize*2,
                                         fill = "white"))
score = 0
txt = "score: " + str(score)
scoreText = canvas.create_text(width/2, 10, fill = "white", font = "Times 20 italic bold",
                                   text = txt)
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.focus_set()

direction = "up"

position = []

storefood()
placePoison()
moveSnake()


window.mainloop()















