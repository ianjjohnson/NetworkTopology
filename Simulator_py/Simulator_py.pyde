#A host is created using a dictionary, so we can add/remove attributes as we please

#Build a default host at position x, y. Modify this function to add more params to the host structure
def buildDefaultHostAtXY(x, y):
    return {'x': x, 'y': y, 'showInterference': False}


#Randomly generate some hosts for the network
def randomlyGenerateHosts(num):
    hosts = []
    for i in range(num):
        hosts.append(buildDefaultHostAtXY(random(1600), random(800)))
    return hosts

hosts = randomlyGenerateHosts(50)

#The 'showInterference' flag on the AP is used to override the showInterference flag for all other hosts to generate an overall interference map

AP = buildDefaultHostAtXY(800, 450)
   
#Processing setup -- use this only for setting up processing stuff, not other python stuff   
def setup():
    print "Setup" 
    ellipseMode(CENTER)
    size(1600,900)
    background(255)     

#Draw loop - should ideally be used only for drawing stuff, not our algorithms
def draw():
    
    background(255);
    
    for host in hosts:
        stroke(0)
        fill(0)
        x = host['x']
        y = host['y']
        ellipse(x, y, 10,10)
        line(x, y, 800, 450)
        if(host['showInterference'] or AP['showInterference']):
            noStroke()
            fill(0, 20)
            distToAP = sqrt((x-800)**2 + (y-450)**2)
            ellipse(x, y, 2*distToAP, 2*distToAP)
        
    noStroke() 
    fill(0,0,255)
    ellipse(800, 450, 50, 50)
    
#Called when the mouse is pressed -- I know, profound.
def mousePressed():
    
    clickedOnHost = False
    
    for host in hosts:
        x = host['x']
        y = host['y']
        
        
        #If we clicked on this host
        if(abs(x - mouseX) < 10 and abs(y - mouseY) < 10):
            
            #print it and flip its showInterference attribute
            print host
            host['showInterference'] = not host['showInterference']
            clickedOnHost = True
            break
        
    if(not clickedOnHost):
        hosts.append(buildDefaultHostAtXY(mouseX, mouseY))
        
    #If we clicked the AP, flip its showInterference attribute
    if(abs(mouseX - 800) <= 50 and abs(mouseY- 450) <= 50):
        AP['showInterference'] = not AP['showInterference']