function LedsDown() {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
}

function MoveRight() {
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, speed)
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.RightMotor)
}

function LedsNone() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
}

function LedsUp() {
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
}

function LedsRight() {
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        `)
}

function LedsLeft() {
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
}

function MoveLeft() {
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, speed)
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.LeftMotor)
}

function MoveBackward() {
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Backward, speed)
}

function Stop() {
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
}

function MoveForward() {
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, speed)
}

let move_left = false
let move_right = false
let y_box_position = 0
let x_box_position = 0
let speed = 0
let screen_width = 320
let screen_hight = 240
let width_center = screen_width / 2
let hight_center = screen_hight / 2
let free_gap = 30
speed = 60
maqueenPlusV2.I2CInit()
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_COLOR_RECOGNITION)
basic.forever(function on_forever() {
    
    let move_backward = 0
    let move_forward = 0
    huskylens.request()
    x_box_position = huskylens.readeBox(1, Content1.xCenter)
    y_box_position = huskylens.readeBox(1, Content1.yCenter)
    if (x_box_position > width_center + free_gap) {
        move_right = true
    } else if (width_center - free_gap > x_box_position && x_box_position > -1) {
        move_left = true
    }
    
    //  elif y_box_position > hight_center + free_gap:
    //  move_forward = True
    //  elif hight_center - free_gap > y_box_position > -1:
    //  move_backward = True
    if (move_right) {
        //  LedsRight()
        MoveRight()
    } else if (move_left) {
        //  LedsLeft()
        MoveLeft()
    } else if (move_forward) {
        //  LedsUp()
        MoveForward()
    } else if (move_backward) {
        //  LedsDown()
        MoveBackward()
    } else {
        LedsNone()
        Stop()
    }
    
})
