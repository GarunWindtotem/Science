import turtle

# Set the window size
turtle.setup(200,900)
wn = turtle.Screen()
wn.title("Falling Ball")

# Create a turtle to draw the ball
ball = turtle.Turtle()

# Set the ball's shape and color
ball.shape("circle")
ball.color("red")

# Set the ball's initial position
ball.penup()
ball.goto(0, 800)

# Set the ball's initial speed
speed = 0

# Set the acceleration due to gravity
gravity = -9.81

# Set the time step
dt = 3

# Move the ball until it hits the ground
while ball.ycor() > 0:
    # Update the ball's speed
    speed += gravity * dt

    # Update the ball's position
    ball.sety(ball.ycor() + speed * dt)

# Stop the program when the ball hits the ground
wn.exitonclick()
