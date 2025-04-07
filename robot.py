from motor import Motor

class Robot:
    def __init__(self, name: str, color: str):

        self.speed = None
        self.name = name
        self.color = color
        self.left_motor = Motor()
        self.right_motor = Motor()
        
    def drive_forward (self, speed: float)->None:
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

    def reverse(self)->None:
        self.left_motor.reverse()
        self.right_motor.reverse()

    def turn_left(self)->None:
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(1)
    def turn_right(self)->None:
        self.right_motor.set_speed(0)
        self.left_motor.set_speed(1)


        
