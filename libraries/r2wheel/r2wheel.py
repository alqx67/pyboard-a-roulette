# Commande d'une plateforme robotique 2 roues avec un pont-H L293D 
#   et MicroPython PyBoard
#   http://shop.mchobby.be/product.php?id_product=741
#   http://shop.mchobby.be/product.php?id_product=155
#   http://shop.mchobby.be/product.php?id_product=155
# 
# Voir Tutoriel 
#   http://wiki.mchobby.be/index.php?title=Hack-micropython-L293D
#
import pyb
from hbridge import DualHBridge

class Robot2Wheel( DualHBridge ):
    """ Specifics for 2 Wheel Robot. Other  
           
        wired as described in the tutorial 
           http://wiki.mchobby.be/index.php?title=Hack-micropython-L293D """

    MOT1_PINS = ( pyb.Pin.board.X6, pyb.Pin.board.X5 )
    MOT1_PWM = {'pin' : pyb.Pin.board.X3, 'timer' : 2, 'channel' : 3 }   

    MOT2_PINS = ( pyb.Pin.board.X7, pyb.Pin.board.X8 )
    MOT2_PWM = {'pin' : pyb.Pin.board.X4, 'timer' : 5, 'channel' : 4 }  

    (RIGHT_ROTATE, LEFT_ROTATE, RIGHT_BEND, LEFT_BEND ) = ('RP','LP','RB','LB')
    DIRECTIONS =  (RIGHT_ROTATE, LEFT_ROTATE, RIGHT_BEND, LEFT_BEND ) 
    
    def __init__( self, reverse_mot1 = False, reverse_mot2 = False, fix_rotate = False, derivative_fix = 0 ):
        """ Initialize the DualHBridge L293D. Allows you to reverse the 
            spinning commands for the motors when the robot does not 
            move proprely when calling forward() or backward()

          :param reverse_mot1: switch the forward/backward commands for motor 1
          :param reverse_mot2: switch the forward/backward commands for motor 2
          :param fix_rotate: set this True when the robot turn left instead of turning right as requested
          :param derivative_fix: use +3 to speedup right motor when forward() does bend the path to the right. 
                                 use -3 to slow down the right motor when forward() bend the path to the left."""
        mot1 = ( self.MOT1_PINS[1], self.MOT1_PINS[0] ) if reverse_mot1 else self.MOT1_PINS
        mot2 = ( self.MOT2_PINS[1], self.MOT2_PINS[0] )  if reverse_mot2 else self.MOT2_PINS
        if not fix_rotate:
            DualHBridge.__init__( self, mot1, self.MOT1_PWM, mot2, self.MOT2_PWM, derivative_fix )
        else:
            # Robot is apparently rotating the wrong way... this is because
            # motor1 has been wired in place of the motor 2.
            DualHBridge.__init__( self, mot2, self.MOT2_PWM, mot1, self.MOT1_PWM, derivative_fix )

    def turn( self, direction, speed=100 ):
        if not( direction in self.DIRECTIONS ):
            raise ValueError( 'invalid direction' )
        if direction == self.RIGHT_ROTATE:
            self.motor1.forward( speed )
            self.motor2.backward( speed )
        elif direction == self.LEFT_ROTATE: 
            self.motor1.backward( speed )
            self.motor2.forward( speed )
        elif direction == self.RIGHT_BEND:
            self.motor1.forward( 100 )
            self.motor2.forward( 100-speed ) 
        elif direction == self.LEFT_BEND:
            self.motor1.forward( 100-speed )
            self.motor2.forward( 100 )
