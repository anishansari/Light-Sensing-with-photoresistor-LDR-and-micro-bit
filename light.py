from microbit import *
while True:   
    input = pin2.read_analog()    
   output= int(input / 50)    
    display.show(str(output))
