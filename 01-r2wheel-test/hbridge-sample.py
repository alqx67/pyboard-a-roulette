# SAMPLE AND TEST FOR HBridge class
#
# Handle a single L293D H-Brige with MicroPython PyBoard
#   http://shop.mchobby.be/product.php?id_product=155
# See tutorial 
#   http://wiki.mchobby.be/index.php?title=Hack-micropython-L293D
#
from pyb import delay, Timer
from hbridge import HBridge
        
# Pont-H broches de commande Input 1 et Input 2
MOT1_PINS = ( pyb.Pin.board.X6, pyb.Pin.board.X5 )
# Commande PWM pont-H
MOT1_PWM = {'pin' : pyb.Pin.board.X3, 'timer' : 2, 'channel' : 3 }   

# Pont-H broches de commande Input 3 et Input 4
MOT2_PINS = ( pyb.Pin.board.X7, pyb.Pin.board.X8 )
# Commande PWM pont-H
MOT2_PWM = {'pin' : pyb.Pin.board.X4, 'timer' : 5, 'channel' : 4 }        

def test_bridge_simple():
    """ Simply test the HBridge without speed control. 
        For this sample the ENABLE PIN of L293D must be high!!! """
    h1 = HBridge( MOT1_PINS )
    print( "Forward" )
    h1.forward()
    delay( 3000 )
    print( "Halt" )
    h1.halt()
    delay( 3000 )
    print( "Backward" )
    h1.backward()
    delay( 3000 )
    print( "Halt" )
    h1.halt()
    print( "end." )

def test_bridge_speed():
    """ Test the HBridge WITH speed control """
    h1 = HBridge( MOT1_PINS, MOT1_PWM )
    print( "Forward full speed" )
    h1.forward()
    delay( 3000 ) 
    print( "Forward half speed 50%" )
    h1.forward( 50 )
    delay( 3000 )
    print( "Forward 30% speed" )
    h1.forward( 30 )
    delay( 3000 )
    for the_speed in range( 10, 70, 10 ):
        print( "Backward at speed %i" % (100-the_speed) )
        h1.backward( 100-the_speed )
        delay( 1500 )
    h1.halt()

def test_two_bridges():
    """ Test the two H-Bridges of the L293D """
    h1 = HBridge( MOT1_PINS, MOT1_PWM )
    h2 = HBridge( MOT2_PINS, MOT2_PWM )
    # move the 2 motors forwards
    h1.forward( 70 )
    h2.forward( 70 )
    delay( 3000 )
    # Stop the 2 motors
    h1.halt()
    h2.halt()

def test_bridge2_simple():
    """ Test the two H-Bridges of the L293D """
    h2 = HBridge( MOT2_PINS, MOT2_PWM )
    print( "Forward full speed" )
    h2.forward()
    delay( 3000 )
    print( "Halt" )
    h2.halt()


# test_bridge_simple()
test_bridge2_simple()
test_bridge_speed()  
test_two_bridges()
