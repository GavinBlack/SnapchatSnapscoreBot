import pyautogui, time, mouse
from pynput import keyboard
from time import perf_counter
from playsound import playsound
                
pyautogui.FAILSAFE = True

time.sleep(.5)

def clickPlusSignAndMultiSnap():
    plus = None
    multiSnap = None
    
    while plus is None:
        plus = pyautogui.locateOnScreen('pics/plusSign.png', confidence=0.8)

    pyautogui.moveTo(plus)
    pyautogui.click(plus)

    while multiSnap is None:
        multiSnap = pyautogui.locateOnScreen('pics/multiSnap.png', confidence=0.8)

    pyautogui.moveTo(multiSnap)
    pyautogui.click(multiSnap)

def forceStopSnapchat():
    snapchat = None
    appInfo = None
    forceStop = None
    forceStopOk = None
    settingsAtTop = None
    clearAll = None
    iInfoButton = None

    #hold the snapchat app
    while snapchat is None:
        snapchat = pyautogui.locateOnScreen('pics/snapchat.png', confidence=0.8)
        
    pyautogui.moveTo(snapchat)
    pyautogui.mouseDown()
    time.sleep(.65)
    pyautogui.mouseUp()

    #click app info
    while appInfo is None and iInfoButton is None:
        appInfo = pyautogui.locateOnScreen('pics/appinfo.png', confidence=0.8)
        iInfoButton = pyautogui.locateOnScreen('pics/iInfoButton.png', confidence=0.8)

    #figure out which one is one the screen
    if appInfo is None:
        pyautogui.moveTo(iInfoButton)
        pyautogui.click(iInfoButton)
    else:
        pyautogui.moveTo(appInfo)
        pyautogui.click(appInfo)

    #click force stop
    while forceStop is None:
        forceStop = pyautogui.locateOnScreen('pics/forcestop.png', confidence=0.8)

    pyautogui.moveTo(forceStop)
    pyautogui.click(forceStop)

    #click force stop ok button
    while forceStopOk is None:
        forceStopOk = pyautogui.locateOnScreen('pics/forcestopok.png', confidence=0.8)

    pyautogui.moveTo(forceStopOk)
    pyautogui.click(forceStopOk)

    #close force stop screen
    bottomOfScreen = pyautogui.locateOnScreen('pics/forcestopbottomofscreen.png', confidence=0.8)

    #get the center coords of the two points
    centerOfBottom = pyautogui.center(bottomOfScreen)
    bottomX, bottomY = centerOfBottom

    #get a point at the top of screen
    top = pyautogui.locateOnScreen('pics/infoattop.png', confidence=0.8)
    centerOfTop = pyautogui.center(top)
    topX, topY = centerOfTop

    #drag the bottom of the screen to the first point (show app tray)
    pyautogui.moveTo(centerOfBottom)
    pyautogui.mouseDown(button='left', x=bottomX, y=bottomY)
    pyautogui.dragTo(topX, topY, .3, button='left')

    #get coords of the app icon in the app tray

    while settingsAtTop is None:
        settingsAtTop = pyautogui.locateOnScreen('pics/settingsicon.png', confidence=0.8)
        
    centerOfSettings = pyautogui.center(settingsAtTop)
    settingsX, settingsY = centerOfSettings

    #drag everything to the right to see the Clear All button
    pyautogui.moveTo(centerOfSettings)
    pyautogui.mouseDown(button='left', x=settingsX, y=settingsY)
    pyautogui.dragTo(2500, settingsY, .5, button='left')

    while clearAll is None:
        clearAll = pyautogui.locateOnScreen('pics/clearAll.png', confidence=0.8)
        
    pyautogui.moveTo(clearAll)
    pyautogui.click(clearAll)

def restartSnapchat(blue=False):
    top = None
    snapLogoAtTop = None
    clearAll = None
    snapchat = None
    chatButton = None

    """
    There's not an easy way to restart the applications, so we have to create a way
    to control the mouse to close everything and then reopen everything in the
    correct way by itself.
    """
    
    #get the values of points of dragging
    if not blue:
        bottomOfScreen = pyautogui.locateOnScreen('pics/bottomOfScreen.png', confidence=0.8)
    else:
        bottomOfScreen = pyautogui.locateOnScreen('pics/blueBottomOfScreen.png', confidence=0.8)
    
    if not blue:
        while top is None:
            top = pyautogui.locateOnScreen('pics/chat.png', confidence=0.8)
    else:
        while top is None:
            top = pyautogui.locateOnScreen('pics/search.png', confidence=0.8)

    #get the center coords of the two points
    centerOfBottom = pyautogui.center(bottomOfScreen)
    bottomX, bottomY = centerOfBottom

    centerOfTop = pyautogui.center(top)
    topX, topY = centerOfTop

    #drag the bottom of the screen to the first point (show app tray)
    pyautogui.moveTo(centerOfBottom)
    pyautogui.mouseDown(button='left', x=bottomX, y=bottomY)
    pyautogui.dragTo(topX, topY, .3, button='left')

    #get coords of the app icon in the app tray
    while snapLogoAtTop is None:
        snapLogoAtTop = pyautogui.locateOnScreen('pics/snapLogoAtTop.png', confidence=0.8)
        
    centerOfSnapLogo = pyautogui.center(snapLogoAtTop)
    snapLogoX, snapLogoY = centerOfSnapLogo

    #drag everything to the right to see the Clear All button
    pyautogui.moveTo(centerOfSnapLogo)
    pyautogui.mouseDown(button='left', x=snapLogoX, y=snapLogoY)
    pyautogui.dragTo(2500, snapLogoY, .5, button='left')

    while clearAll is None:
        clearAll = pyautogui.locateOnScreen('pics/clearAll.png', confidence=0.8)
        
    pyautogui.moveTo(clearAll)
    pyautogui.click(clearAll)

    #hold down on snapchat, goto app info, force stop, go back to home screen
    forceStopSnapchat()

    #take a 5 minute break to possibly prevent more freezing
    print('taking a break')
    time.sleep(300)
    print('done with break')

    #click the snapchat app
    while snapchat is None:
        snapchat = pyautogui.locateOnScreen('pics/snapchat.png', confidence=0.8)
        
    pyautogui.moveTo(snapchat)
    pyautogui.click(snapchat)

    time.sleep(12) # this is needed for everything to load on screen

    #click the chat button
    while chatButton is None:
        chatButton = pyautogui.locateOnScreen('pics/chatbutton.png', confidence=0.8)
        
    pyautogui.moveTo(chatButton)
    pyautogui.click(chatButton)

def printResults(playSound=True):
    ct = 0
    end = perf_counter()
    
    print("Total elapsed time:", convert(round(end-start,2)))
    print("Total score:", totalScore)
    
    if playSound:
        while ct < 15: #wake me up/alarm when not working
            ct += 1
            playsound('sounds/beep.mp3')
        
    exit()

def checkIfNotClosed(): #make sure the phone didn't get disconnected
    spot = None
    global totalScore

    while spot is None:
        spot = pyautogui.locateOnScreen('pics/pixel6pro.png', confidence=0.85)
        if spot is None: #if phone disconnected
            printResults()
            
def clickCamera():
    spot = None
    send = None
    ct = 0
    
    while spot is None:
        ct += 1
        if ct == 35:
            checkIfNotClosed()

            #check if the send button is still on screen and snapchat is froze at that step
            send = pyautogui.locateOnScreen('pics/send.png', confidence=0.85)
            if send is not None:
                print('restarting snapchat..')
                restartSnapchat(True)
                clickPlusSignAndMultiSnap()
                return
            
        spot = pyautogui.locateOnScreen('pics/camera.png', confidence=0.80)
        
    pyautogui.moveTo(spot)
    pyautogui.click(spot)
    
def getThe8Pictures():
    spot = None
    okay = None
    ct = 0

    while spot is None:
        ct += 1
        if ct == 100:
            checkIfNotClosed()
            
        spot = pyautogui.locateOnScreen('pics/capture.png', confidence=0.85)
        
    pyautogui.moveTo(spot)

    while okay is None:
        mouse.click()
        time.sleep(.091)
        okay = pyautogui.locateOnScreen('pics/okay.png', confidence=0.85)
    time.sleep(.3)

def clickOkay():
    spot = None
    ct =0
    
    while spot is None:
        ct += 1
        if ct == 50:
            checkIfNotClosed()
            
        spot = pyautogui.locateOnScreen('pics/okay.png', confidence=0.85)
        
    pyautogui.moveTo(spot)
    pyautogui.click(spot)

def clickNext():
    spot = None
    ct = 0

    while spot is None:
        ct += 1
        if ct == 50:
            checkIfNotClosed()
            
        spot = pyautogui.locateOnScreen('pics/next.png', confidence=0.85)
        
    pyautogui.moveTo(spot)
    pyautogui.click(spot)
    time.sleep(2)

def clickLastSnap():
    spot = None
    ct = 0

    while spot is None:
        ct += 1
        if ct == 90:
            checkIfNotClosed()
        spot = pyautogui.locateOnScreen('pics/lastsnap.png', confidence=0.85)
        
    pyautogui.moveTo(spot)
    pyautogui.click(spot)

def clickSend():
    spot = None
    lastSnap = None
    ct = 0

    while spot is None:
        ct += 1

        """
        Sometimes snapchat is slower and we have to double check
        that we clicked the Last Snap button again, because sometimes
        it sees it, but doesn't click it and the program goes idle.
        """
        
        if ct == 60:
            checkIfNotClosed()
            lastSnap = pyautogui.locateOnScreen('pics/lastsnap.png', confidence=0.85)
            
            if lastSnap is not None: #see if last snap button is still on screen
                pyautogui.moveTo(lastSnap)
                pyautogui.click(lastSnap)
                
        spot = pyautogui.locateOnScreen('pics/send.png', confidence=0.85)
        
    pyautogui.moveTo(spot)
    pyautogui.click(spot)
    time.sleep(2.5)

def waitTillAllSent():
    spot = 1 #placeholder value

    while spot is not None: #while the 'sending' is still on screen, not all has been sent.
        spot = pyautogui.locateOnScreen('pics/sending.png', confidence=0.85)
            
def convert(seconds): #converts seconds to h,m,s
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def on_press(key):
    global on
    if key == keyboard.Key.esc:
        print("doesn't work rn")  # WIP
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k == 'x': #stop program
        on = False
        print("exiting after current iteration...")
    if k == 't':
        end = perf_counter()
        print("Total elapsed time:", convert(round(end-start)))
    if k == 's':
        print("Total approx. scored gained:", totalScore)
        
def main():
    #Initializing variables
    ct = 0
    totalTime = 0
    grandTotalTime = 0
    scorePerIteration = 600
    iterationTime = 0
    global totalScore

    while on: 
        clickCamera()            
        getThe8Pictures()
        clickOkay()
        clickNext()
        clickLastSnap()
        clickSend()
        waitTillAllSent()
        
        end = perf_counter()
        iterationTime = round(end-start)
        totalTime += iterationTime
        grandTotalTime += totalTime
        
        ct += 1
        totalScore += scorePerIteration

        #temportary for new account, can remove if too slow
        time.sleep(3.5)

    printResults(False)

#global variables 
start = perf_counter()
totalScore = 0
on = True

#keyboard listener waits for keypresses whenever
listener = keyboard.Listener(on_press=on_press)
listener.start()

main()
