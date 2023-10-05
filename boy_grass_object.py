from pico2d import *
import random
# Game object class here
class Grass: # 클래스 이름은 대문자로 시작하는 명사...
    def __init__(self): # 괄호 끝내고 밑으로 내려갈때 쉬프트키 누르고 엔터
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):
        pass
class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x +=5
    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,self.y)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Ball:
    def __init__(self):
        self.choice = random.randint(0,1)
        self.x,self.y = random.randint(50,700),599
        self.image = 0
        self.size = 0
        self.speed = random.randint(100,1000)
        self.stop = False
        if self.choice == 0:
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41
    def update(self):
        if self.stop:
            return
        if self.y  - self.size <= 55:
           self.y = 55 + self.size /2
           self.stop = True
           return
        self.y -= self.speed * 0.02
    def draw(self):
        self.image.draw(self.x,self.y)

def reset_world():
    global running
    global grass
    global team
    global world
    global ball

    running = True
    world=[]
    grass = Grass() # 클래스를 이용해 객체를 찍어냄.
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team
    ball = [Ball() for _ in range(20)]
    world += ball

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def update_world():
    for o in world:
        o.update()
    pass

open_canvas()
# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.02)

# finalization code

close_canvas()
