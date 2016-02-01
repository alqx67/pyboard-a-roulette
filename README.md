PyBoard-a-roulette project
==========================

About
-----
Here I'll put some libraries that can be useful for the PyBoard-a-roulette project.

The aim of pyboard-a-roulette is to place wheels on a PyBoard to make it move around. 

Please support us, our free translations and projects (freely available on wiki.mchobby.be) by buying your material on shop.mchobby.be 

You can redistribute it and/or modify the code found in this repository
under the terms of the GNU GPLv3 license detailed above.

Wiki, Wiring, Shop
------------------
Project information, wiring, recommandation are available on our FRENCH wiki
* http://wiki.mchobby.be/index.php?title=MicroPython-Accueil#PyBoard_.C3.A0_roulette

The material list and link to the shop (France & Belgium)
* http://wiki.mchobby.be/index.php?title=Hack-micropython-Robot2Wheel#Mat.C3.A9riel_n.C3.A9cessaire

Installing a library:
---------------------
simply copy the '.py' files listed in the "library" section here under into the root directory of your PYFLASH PyBoard drive.

Once done, you can use the regular python import statement to use the library into your own scripts.

Libraries
----------
All the libraries are stored under the libraries directory which is subdivided depending on the peripherals/sensors you need to handle.

* __r2wheel\hbridge.py__ : Library HBridge for a single H-Bridge (1 motor control) and DualHBridge (2 motors control).
 * Quite good to manage a L293D
 * Both classes contains basic move method (forward, backward, halt) with speed management.
 * DualHBridge already manage path derivation due to the motors not being exactly identicals 
* __r2wheel\r2wheel.py__ : Library Robot2Wheel extending DualHBridge class to control a 2 Wheels robot plateform.
 * Implement turn() method with RIGHT_ROTATE, LEFT_ROTATE, RIGHT_BEND, LEFT_BEND
 * Implement the more convenient right() and left()
 * Can switch forward/backward for each motor (manage from code instead of re-wiring the motor)
 * Can switch right/left motor from code (instead of re-wiring the motors)
* __ultrasonic\ultrasonic.py__ : Library for the HC-SR04 Ultrasonic distance sensor (by Sergio Conde Gómez, GPL V3, see the file header for more details)
Samples
-------
This project will be conducted in several steps depending on request, contribution and implemented ideas.
So I do order the sample folder with numerical prefix (2 digits). This numerical order also show the historical steps of the project. 

* __01-r2wheel-test\__  : Robot-2-wheel wiring AND test scripts. 
 * Sample scripts used to test the assembled "Robot 2 Wheel" and classes HBridge, Robot2Wheel
 * Pictures with functionnalities.  

License: GPL v3
---------------
Copyright 2016 - Meurisse D <info[at]mchobby[dot]com> - http://shop.mchobby.be

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

