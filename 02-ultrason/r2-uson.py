##
# Commande d'une plateforme robotique 2 roues avec détecteur UltraSon HC-SR04.
#    Tourne sur la droite quand il détecte un objet à moins de 20 cm. Sinon avance en ligne droite.
# 
# Control a 2 wheel robotic plateform with a L293D H Bridge and MicroPython PyBoard
#    Turn right when detecting an object within the 20 cm. Otherwise move forward.
#
#   http://shop.mchobby.be/product.php?id_product=741
#   http://shop.mchobby.be/product.php?id_product=155
#   http://shop.mchobby.be/product.php?id_product=570
#   http://shop.mchobby.be/product.php?id_product=561
# 
# Voir Tutoriel - See our french tutorial
#   http://wiki.mchobby.be/index.php?title=Hack-micropython-Robot2Wheel-HC-SR04
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

from pyb import delay
from r2wheel import Robot2Wheel                                             
from ultrasonic import Ultrasonic

# Broche pour déclencher le senseur
TRIGGER_PIN = pyb.Pin.board.Y5 
# Broche pour attendre le retour d'echo
ECHO_PIN = pyb.Pin.board.Y6

r2 = Robot2Wheel( reverse_mot2 = True ) 
u = Ultrasonic( TRIGGER_PIN, ECHO_PIN )

MIN_DISTANCE = 20 # Minimum distance 

r2.forward()
while True:
    if u.distance_in_cm() < MIN_DISTANCE:
        r2.halt()
        delay(100)
        r2.right()
        delay( 2500 )
        r2.halt()
        delay(100)
    # If nothing in front then move
    if (r2.state == Robot2Wheel.HALTED) and (u.distance_in_cm() > MIN_DISTANCE): 
        r2.forward()
