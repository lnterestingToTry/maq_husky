def LedsDown():
    basic.show_leds("""
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        """)
def MoveRight():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR)
def LedsNone():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
def LedsUp():
    basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        """)
def LedsRight():
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
def LedsLeft():
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
def MoveLeft():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR)
def MoveBackward():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.BACKWARD,
        speed)
def Stop():
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
def MoveForward():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)
move_left = False
move_right = False
y_box_position = 0
x_box_position = 0
speed = 0
screen_width = 320
screen_hight = 240
width_center = screen_width / 2
hight_center = screen_hight / 2
free_gap = 30
speed = 60
maqueenPlusV2.i2c_init()
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_COLOR_RECOGNITION)

def on_forever():
    global x_box_position, y_box_position, move_right, move_left
    move_backward = 0
    move_forward = 0
    huskylens.request()
    x_box_position = huskylens.reade_box(1, Content1.X_CENTER)
    y_box_position = huskylens.reade_box(1, Content1.Y_CENTER)
    if x_box_position > width_center + free_gap:
        move_right = True
    elif width_center - free_gap > x_box_position and x_box_position > -1:
        move_left = True
    # elif y_box_position > hight_center + free_gap:
    # move_forward = True
    # elif hight_center - free_gap > y_box_position > -1:
    # move_backward = True
    if move_right:
        # LedsRight()
        MoveRight()
    elif move_left:
        # LedsLeft()
        MoveLeft()
    elif move_forward:
        # LedsUp()
        MoveForward()
    elif move_backward:
        # LedsDown()
        MoveBackward()
    else:
        LedsNone()
        Stop()
basic.forever(on_forever)
