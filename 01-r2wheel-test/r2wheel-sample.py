# SAMPLE AND TEST FOR Robot2Wheel class
#
# Handle a L293D dual H-Brige (pont-H L293D) with MicroPython PyBoard
#   http://shop.mchobby.be/product.php?id_product=155
# See the tutorial (and wiring) on  
#   http://wiki.mchobby.be/index.php?title=Hack-micropython-L293D
#
from pyb import delay
from r2wheel import Robot2Wheel


def test_moving():
    """ Test the two H-Bridges of the L293D """

    robot = Robot2Wheel( reverse_mot2 = True ) # Rerverse commands on motor 2 to move forward proprely
    print( "Move Forward" )
    robot.forward()
    delay( 2000 )
    print( "Move Forward 50%" )
    robot.forward( 50 )
    delay( 2000 )
    print( "Move Forward 70% and 40%" )
    robot.forward( 70, 40 )
    delay( 2000 )
    print( "Halt" )
    robot.halt()

def test_turning():
    """ Test the robot turning/rotating commands """

    robot = Robot2Wheel( reverse_mot2 = True ) # Rerverse commands on motor 2 to move forward proprely
    print( "Rotate RIGHT" )
    robot.turn( Robot2Wheel.RIGHT_ROTATE )
    delay( 2000 )
    robot.halt()
    delay( 2000 )
    print( "Rotate LEFT" )
    robot.turn( Robot2Wheel.LEFT_ROTATE )
    delay( 2000 )
    robot.halt()
    delay( 2000 )
    print( "Rotate RIGHT 60% Speed" )
    robot.turn( Robot2Wheel.RIGHT_ROTATE, speed=60 )
    delay( 2000 )
    print( "Halt" )
    robot.halt()

def test_turning2():
    """ Test the robot turning/rotating commands """

    robot = Robot2Wheel( reverse_mot2 = True ) # Rerverse commands on motor 2 to move forward proprely
    print( "Forward full Speed" )
    robot.forward()
    delay( 2000 )
    print( "Turning on RIGHT delta speed=60%" )
    robot.turn( Robot2Wheel.RIGHT_BEND, speed=80 )
    delay( 4000 )
    print( "Forward full Speed" )
    robot.forward()
    delay( 2000 )
    print( "Turning on LEFT delta speed=60%" )
    robot.turn( Robot2Wheel.LEFT_BEND, speed=80 )
    delay( 4000 )
    print( "Halt" )
    robot.halt()

def test_derivative_fix():
    """ two identical motor never have the exact same gear ratio and speed
       so, to really move forward without derivative (going on right or left)
       you have to slow down the 'fastest' motor to make to robot
       moving forward 

       Derivative value should be < 10%.
       """
    # Force a derivative_fix of +50% to make it obvious... slow down the left
    #    motor to avoids the the robot to bend its path on the right
    robot = Robot2Wheel( reverse_mot2 = True, derivative_fix = 50 )
    print( "Move forward with derivative" )
    robot.forward()
    delay( 3000 )
    print( "Move forward 70% with derivative" )
    robot.forward( speed = 70 )
    delay( 3000 )
    print( "Halt" )
    robot.halt()
    
    # Force a derivative_fix of -50% to make it obvious... slow down the right
    #    motor to avoids the the robot to bend its path on the left
    robot = None
    robot = Robot2Wheel( reverse_mot2 = True, derivative_fix = -50 )
    print( "Move forward with derivative" )
    robot.forward()
    delay( 3000 )
    print( "Move forward 70% with derivative" )
    robot.forward( speed = 70 )
    delay( 3000 )
    print( "Halt" )
    robot.halt()

def test_derivative_fix2():
    """ Do the same than derivative_fix() but for forward move """
    # Force a derivative_fix of +50% to make it obvious... slow down the left
    #    motor to avoids the the robot to bend its path on the right
    robot = Robot2Wheel( reverse_mot2 = True, derivative_fix = 50 )
    print( "Move forward with derivative" )
    robot.forward()
    delay( 3000 )
    print( "Move backward with derivative" )
    robot.backward()
    delay( 3000 )
    print( "Halt" )
    robot.halt()
    

test_moving()
# test_turning()
# test_turning2()
# test_derivative_fix()
# test_derivative_fix2()
