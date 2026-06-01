# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def teleport():
    agent.teleport_to_player()

def move_foward(step):
    agent.move(FORWARD, step)

def move_back(step):
    agent.move(BACK, step)

def move_up(step):
    agent.move(UP, step)

def move_down(step):
    agent.move(DOWN, step)


def turn_left():
    agent.turn(LEFT)


def turn_right():
    agent.turn(RIGHT)



player.on_chat("come", teleport)
player.on_chat("fw", move_foward)
player.on_chat("bk", move_back)
player.on_chat("up", move_up)
player.on_chat("down", move_down)
player.on_chat("tl", turn_left)
player.on_chat("tr", turn_right)


def move_from_gold():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD,4)


    
player.on_chat("q1", move_from_gold)

def move_from_dimond():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
player.on_chat("w1", move_from_dimond)

def move_from_top():
    agent.move(FORWARD, 2)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("e1", move_from_top)

def combine_obs():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD,4) 
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 2)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("r1", combine_obs)

