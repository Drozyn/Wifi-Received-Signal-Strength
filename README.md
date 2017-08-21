# Wifi-Received-Signal-Strength
This script allows to measure received signal strength of avalaible wifi transmitters in the area. User can also determine x,y coordinates of position, where measure was made.

Author enabled also do a iterative measurement (user must determine how much measure iterations has to be done). Every measurement is saved in .txt file with such data as:
ID of measurement position
position coordinates (x,y)
iteration number
transmitter's MAC
transmiter's RSS

Language: Python
Language used in script: Polish (descriptions)

Received data can be used in further analysis.

Script uses:
PyQt4 (QtCore, QtGUi)
win32wifi
