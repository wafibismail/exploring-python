from pygame.locals import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *

pygame.init()

# project settings
screen_width = 500
screen_height = 400
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformations in Python')
cube = Cube(GL_LINE_LOOP)
mesh = LoadMesh("teapot.obj", GL_LINE_LOOP)
eye = [0, 0, 0]

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glTranslated(0.5, -0.5, -5)  # With this, the cube is moved; not the camera
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def init_camera():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_camera()
    glPushMatrix()
    mesh.draw()
    glPopMatrix()


done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        eye[2] += 1
    elif keys[pygame.K_UP]:
        eye[2] -= 1
    elif keys[pygame.K_LEFT]:
        eye[0] -= 1
    elif keys[pygame.K_RIGHT]:
        eye[0] += 1

    display()
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()