import xbox


#####################
## Variable Setups ##
#####################

# instantiate drum controller
drum = xbox.Joystick()

# Position of Pads and Buttons in Array
y_cymbal = 0
b_cymbal = 1
g_cymbal = 2

r_drum = 3
y_drum = 4
b_drum = 5
g_drum = 6

rt_pedal = 7
lt_pedal = 8

# variables to hold current hits and output notes.
hits = []
triggers_to_send = []
number_of_inputs = 9
cymbal = "None"
bouncing_cymbal = False
bouncing_drum = False
# set all lists members to False
for pad in range(number_of_inputs):
    hits.append(False)
    triggers_to_send.append(False)
    
#TODO: Add face buttons, d pad, start, back

#########################
## Necessary Functions ##
#########################
def ResetOutputs():
    for pad in range(number_of_inputs):
        triggers_to_send[pad] = False 

# Checks to see if the cymbals have stopped bouncing.
def CheckYellowCymbal():
    global bouncing_cymbal
    if (drum.Y() and drum.rightBumper() and drum.dpadUp() and drum.leftY() != 0):
        return True
    else:
        bouncing_cymbal = False
        return False

def CheckBlueCymbal():
    global bouncing_cymbal
    if (drum.X() and drum.rightBumper() and drum.dpadDown() and drum.rightX() != 0):
        return True
    else:
        bouncing_cymbal = False
        return False

def CheckGreenCymbal():
    global bouncing_cymbal
    if (drum.A() and drum.rightBumper() and drum.rightY() != 0):
        return True
    else:
        bouncing_cymbal = False
        return False

def CheckRedDrum():
    global bouncing_drum
    if (drum.B() and drum.rightThumbstick() and drum.leftX() != 0):
        return True
    else:
        bouncing_drum = False
        return False

def CheckYellowDrum():
    global bouncing_drum
    if (drum.Y() and drum.rightThumbstick() and drum.leftY() != 0):
        return True
    else:
        bouncing_drum = False
        return False

def CheckBlueDrum():
    global bouncing_drum
    if (drum.X() and drum.rightThumbstick() and drum.rightX() != 0):
        return True
    else:
        bouncing_drum = False
        return False

def CheckGreenDrum():
    global bouncing_drum
    if (drum.A() and drum.rightThumbstick() and drum.rightY() != 0):
        return True
    else:
        bouncing_drum = False
        return False

# Hits
def YellowCymbalHit():
    global bouncing_cymbal, cymbal
    hits[y_cymbal] = True
    triggers_to_send[y_cymbal] = True
    cymbal = "Yellow"
    print("Yellow Cymbal")
    bouncing_cymbal = True

def BlueCymbalHit():
    global bouncing_cymbal, cymbal
    hits[b_cymbal] = True
    triggers_to_send[b_cymbal] = True
    cymbal = "Blue"
    print("Blue Cymbal")
    bouncing_cymbal = True


def GreenCymbalHit():
    global bouncing_cymbal, cymbal
    hits[g_cymbal] = True
    triggers_to_send[g_cymbal] = True
    cymbal = "Green"
    print("Green Cymbal")
    bouncing_cymbal = True


def RedDrumHit():
    global bouncing_drum
    hits[r_drum] = True
    triggers_to_send[r_drum] = True
    print("Red Drum")
    bouncing_drum = True


def YellowDrumHit():
    global bouncing_drum
    hits[y_drum] = True
    triggers_to_send[y_drum] = True
    print("Yellow Drum")
    bouncing_drum = True


def BlueDrumHit():
    global bouncing_drum
    hits[b_drum] = True
    triggers_to_send[b_drum] = True
    print("Blue Drum")
    bouncing_drum = True

def GreenDrumHit():
    global bouncing_drum
    hits[g_drum] = True
    triggers_to_send[g_drum] = True
    print("Green Drum")
    bouncing_drum = True

def ObjectHit(color, object, cymbal):
    global bouncing_drum, bouncing_cymbal, hits, triggers_to_send
    hits[object] = True
    triggers_to_send[object] = True
    if cymbal:
        print(str(color) + " Cymbal")
        bouncing_cymbal = True
    else:
        print(str(color) + " Drum")
        bouncing_drum = True

## Main Program ##
    
print("Starting Program")
while True:
    # has a cymbal or drum been played?
    cymbal_played = drum.rightBumper()
    drum_played = drum.rightThumbstick()
    
    # Cymbals played, no drums
    if cymbal_played and not drum_played and not bouncing_cymbal and not bouncing_drum:
        if drum.Y() and hits[y_cymbal] is False:
            YellowCymbalHit()
        if drum.X() and hits[b_cymbal] is False:
            BlueCymbalHit()
        if drum.A() and hits[g_cymbal] is False:
            GreenCymbalHit()
    
    # Drums played, no cymbals
    elif drum_played and not cymbal_played and not bouncing_drum and not bouncing_cymbal:
        if drum.B() and hits[r_drum] is False:
            RedDrumHit()
        if drum.Y() and hits[y_drum] is False:
            YellowDrumHit()
        if drum.X() and hits[b_drum] is False:
            BlueDrumHit()
        if drum.A() and hits[g_drum] is False:
            GreenDrumHit()
    
    # A Cymbal and Drum were played together
    elif cymbal_played and drum_played and not bouncing_cymbal and not bouncing_drum:
        # determine which cymbal was played
        print("Both Played")
        if drum.dpadUp() and hits[y_cymbal] is False:
            YellowCymbalHit()
        elif drum.dpadDown() and hits[b_cymbal] is False:
            BlueCymbalHit()   
        elif hits[g_cymbal] is False:
            GreenCymbalHit()
            
        # determine which drum was played
        # this is basically process of elimation based on inputs
        # if you don't see inputs of a color of the cymbal, the
        # drum has to be the same color as the cymbal
        if cymbal is "Yellow":
            if drum.B() and hits[r_drum] is False:
                RedDrumHit()
            elif drum.X() and hits[b_drum] is False:
                BlueDrumHit()
            elif drum.A() and hits[g_drum] is False:
                GreenDrumHit()
            elif hits[y_drum] is False:
                YellowDrumHit()
               
        elif cymbal is "Blue":
            if drum.B() and hits[r_drum] is False:
                RedDrumHit()
            elif drum.Y() and hits[y_drum] is False:
                YellowDrumHit()
            elif drum.A() and hits[g_drum] is False:
                GreenDrumHit()
            elif hits[b_drum] is False:
                BlueDrumHit()
                
        elif cymbal is "Green":
            if drum.B() and hits[r_drum] is False:
                RedDrumHit()
            elif drum.X() and hits[b_drum] is False:
                BlueDrumHit()
            elif drum.Y() and hits[y_drum] is False:
                YellowDrumHit()
            elif hits[g_drum] is False:
                GreenDrumHit()
        
    # Account for pad bounce to prevent multiple hits
    
    for hit in range(number_of_inputs):
        if hits[hit] is True:
            if hit is y_cymbal:
                hits[hit] = CheckYellowCymbal()
            if hit is b_cymbal:
                hits[hit] = CheckBlueCymbal()
            if hit is g_cymbal:
                hits[hit] = CheckGreenCymbal()
            if hit is r_drum:
                hits[hit] = CheckRedDrum() 
            if hit is y_drum:
                hits[hit] = CheckYellowDrum()
            if hit is b_drum:
                hits[hit] = CheckBlueDrum()
            if hit is g_drum:
                hits[hit] = CheckGreenDrum()
            


    #send outputs to pico for midi processing
    #ResetOutputs()