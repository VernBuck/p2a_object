# Animation (Tie fighter) by Vernon Buck

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    # Tie Fighter wing A
    fill (0,0,0)
    rotateY(-time)
    pushMatrix()
    translate (30, 0, 0)
    scale(1,3,1)
    rotate(PI/8)
    rotateY(3)
    box(20)
    popMatrix()
    
    # Tie Fighter wing B
    fill (0,0,0)
    pushMatrix()
    translate (-30, 0, 0)
    scale(1,3,1)
    rotate(PI/8)
    box(20)
    popMatrix()
    
    # Tie fighter cockpit
    fill (128, 128, 128)
    pushMatrix()
    #translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(15)
    popMatrix()
    
    # Tie fighter screen
    fill (0, 0, 0)
    pushMatrix()
    #translate (0, 8 * sin(4 * time), 0)  # move up and down
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    translate (3.5, 3.5, 10)
    sphere(6)
    popMatrix()
    
    # Tie fighter cannon Laser A
    fill (255, 126, 0)
    pushMatrix()
    translate (-5, 10, 10)
    rotateZ (8)
    rotateX (10)
    scale (.8, .8, .8)
    rotate(PI/3)
    cylinder()
    popMatrix()
    
    # Tie fighter cannon Laser B
    fill (255, 126, 0)
    pushMatrix()
    translate (7, 10, 10)
    rotateZ (8)
    rotateX (10)
    scale (.8, .8, .8)
    rotate(PI/3)
    cylinder()
    popMatrix()
    
    # Tie fighter Wing connector A
    fill (128, 126, 128)
    pushMatrix()
    translate (20, -3, 0)
    rotateY (30)
    rotateZ (-10)
    scale (6, 7, 8)
    cylinder()
    popMatrix()
    
    # Tie fighter Wing connector B
    fill (128, 126, 128)
    pushMatrix()
    translate (-20, -3, 0)
    rotateY (30)
    rotateZ (-10)
    scale (6, 7, 8)
    cylinder()
    popMatrix()
    
    # red box
    #fill (255, 0, 0)
    #pushMatrix()
    #translate (-30, 0, 0)
    #rotateX (time)
    #box(20)
    #popMatrix()

    # green sphere
    #fill (0, 250, 0)
    #pushMatrix()
    #translate (0, 8 * sin(4 * time), 0)  # move up and down
    #sphereDetail(60)  # this controls how many polygons are used to make a sphere
    #sphere(10)
    #popMatrix()

    # blue cylinder
    #fill (0, 0, 255)
    #pushMatrix()
    #translate (30, 0, 0)
    #rotateX (-time)
    #scale (10, 10, 10)
    #cylinder()
    #popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2