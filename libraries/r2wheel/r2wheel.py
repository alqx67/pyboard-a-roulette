##
# Commande d'une plateforme robotique 2 roues avec un pont-H L293D et MicroPython PyBoard
# Control a 2 wheel robotic plateform with a L293D H Bridge and MicroPython PyBoard
#
#   http://shop.mchobby.be/product.php?id_product=741
#   http://shop.mchobby.be/product.php?id_product=155
#   http://shop.mchobby.be/product.php?id_product=570
# 
# Voir Tutoriel - See our french tutorial
#   http://wiki.mchobby.be/index.php?title=Hack-micropython-Robot2Wheel
#
# Copyright 2016 - Dominique Meurisse for MC Hobby SPRL <info (at) mchobby (dot) be>
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##
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

    (HALTED,MOVE_FORWARD,MOVE_BACKWARD) = ('H', 'MF', 'MB') 
    STATES = (HALTED,MOVE_FORWARD,MOVE_BACKWARD) + DIRECTIONS

    _state = None # Current state of the robot.
    
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
        self._state = Robot2Wheel.HALTED
	
    @property 
    def state( self ):
        return self._state

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
        self._state = direction

    def right( self, speed=100 ):
        self.turn( Robot2Wheel.RIGHT_ROTATE, speed )

    def left( self, speed=100 ):
        self.turn( Robot2Wheel.LEFT_ROTATE, speed )

    def halt( self ):
        super( Robot2Wheel, self ).halt()
        self._state = Robot2Wheel.HALTED

    def forward( self, speed = 100, speed_2 = None ):
        super( Robot2Wheel, self ).forward( speed, speed_2 )
        self._state = Robot2Wheel.MOVE_FORWARD

    def backward( self, speed = 100, speed_2 = None ):
        super( Robot2Wheel, self ).backward( speed, speed_2 )
        self._state = Robot2Wheel.MOVE_BACKWARD
