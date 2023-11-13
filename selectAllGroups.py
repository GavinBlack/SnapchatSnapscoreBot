import pyautogui, time, mouse
                
pyautogui.FAILSAFE = True

time.sleep(.5)

def selectGroups():
    value = 0
    ct = 0

    value = int(input("How many snaps: "))

    spot = pyautogui.locateOnScreen('pics/groups.png', confidence=0.89)
    pyautogui.moveTo(spot)
    pyautogui.click(spot)

    spot = pyautogui.locateOnScreen('pics/recents.png', confidence=0.89)
    pyautogui.moveTo(spot)
    pyautogui.click(spot)

    while ct < value:
        spot = pyautogui.locateOnScreen('pics/gaviningroups.png', confidence=0.85)
        pyautogui.moveTo(spot)
        pyautogui.click(spot)

        if ct % 5 == 0 and ct != 0:
            mouse.wheel(-4)  
            time.sleep(.15) 
    
        ct += 1
                  
def main():         
    selectGroups()
    spot = pyautogui.locateOnScreen('pics/send.png', confidence=0.85)
    pyautogui.moveTo(spot)
    pyautogui.click(spot)

main()
