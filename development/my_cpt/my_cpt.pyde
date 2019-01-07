# Trying to add gravity.
# Not working as expected

keys_pressed = [False for key_code in range(256)]
GRAVITY = 0.5

def setup():
    global player_position
    size(640, 480)
    player_position = PVector(width/2, height/2)


def draw():
    if keys_pressed[ord('A')]:  # left
        player_position.x += -3
    elif keys_pressed[ord('D')]:  # right
        player_position.x += 3
            
    if keys_pressed[ord('W')]:  # up
        player_position.y += -3
    if keys_pressed[ord('S')]:  # down
        player_position.y += 3
    
    player_position.y += GRAVITY
        
    background(0)
    fill(255)
    ellipse(player_position.x, player_position.y, 20, 20)
        

def keyPressed():
    keys_pressed[keyCode] = True

def keyReleased():
    keys_pressed[keyCode] = False
