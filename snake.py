from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle('square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self):
        # will start counting from the last segment and go down to the first one
        # the we take the coordinations of the next segment and go there, this way the segments will always follow the next segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_segment_xcor = self.segments[seg_num - 1].xcor()
            next_segment_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(next_segment_xcor, next_segment_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
