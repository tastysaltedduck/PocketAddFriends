import pyautogui
import time
import os
from pynput.keyboard import Controller, Key
#pip install pyautogui
#pip install pynput
#pip install opencv-python

os.chdir('B:\Work\Scripts\PocketAddFriends')
keyboard = Controller()
timeDelay = 1
time.sleep(timeDelay)

friendButtonPoint = pyautogui.locateCenterOnScreen('friendButton.png', confidence=0.8)
friendButtonX, friendButtonY = friendButtonPoint
pyautogui.click(friendButtonX, friendButtonY)
time.sleep(timeDelay)

xButtonPoint = pyautogui.locateCenterOnScreen('xButton.png', confidence=0.8)
xButtonX, xButtonY = xButtonPoint

addFriendButtonPoint = pyautogui.locateCenterOnScreen('addFriendButton.png', confidence=0.8)
addFriendButtonX, addFriendButtonY = addFriendButtonPoint
pyautogui.click(addFriendButtonX, addFriendButtonY)
time.sleep(timeDelay)

friendIDTextBoxPoint = pyautogui.locateCenterOnScreen('friendIDTextBox.png', confidence=0.8)
friendIDTextBoxX, friendIDTextBoxY = friendIDTextBoxPoint

#Start Loop
with open('ids.txt') as file:
    while line := file.readline():
        pyautogui.click(friendIDTextBoxX, friendIDTextBoxY)
        time.sleep(timeDelay)
        
        # Press backspace key 16 times to delete a long number
        # No idea why, but the emulator doesn't allow holding a key through pyautogui
        for _ in range(16):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            time.sleep(0.1)  # Small delay between key presses

        time.sleep(timeDelay)
        pyautogui.write(line.rstrip(), interval=0.25)

        friendSearchPoint = pyautogui.locateCenterOnScreen('friendSearch.png', confidence=0.8)
        friendSearchX, friendSearchY = friendSearchPoint
        pyautogui.click(friendSearchX, friendSearchY)
        time.sleep(timeDelay)

        #Already added friend
        try:
            alreadyAddedPoint = pyautogui.locateCenterOnScreen('alreadyAdded.png', confidence=0.8)
            pyautogui.click(xButtonX, xButtonY)
            time.sleep(timeDelay)
            continue
        except:
            pass
        
        #Sent request
        try:
            alreadySentPoint = pyautogui.locateCenterOnScreen('alreadySent.png', confidence=0.8)
            pyautogui.click(xButtonX, xButtonY)
            time.sleep(timeDelay)
            continue
        except:
            pass

        #Send friend request
        try:
            sendFriendRequestPoint = pyautogui.locateCenterOnScreen('sendFriendRequest.png', confidence=0.8)
            sendFriendRequestX, sendFriendRequestY = sendFriendRequestPoint
            pyautogui.click(sendFriendRequestX, sendFriendRequestY)
            #The prompt to send a friend request is a little slow, so we need to wait longer that the timeDelay here
            time.sleep(3)
            try:
                if pyautogui.locateCenterOnScreen('sendFriendRequest.png', confidence=0.8) is not None:
                    print("Friend List Full: " + line.rstrip())
            except: pass
            pyautogui.click(xButtonX, xButtonY)
            time.sleep(timeDelay)
            continue
        except:
            pass
        
        #Friend Not Found
        try:
            friendNotFoundPoint = pyautogui.locateCenterOnScreen('friendNotFound.png', confidence=0.8)
            print("Friend Not Found: " + line.rstrip())
            friendNotFoundX, friendNotFoundY = friendNotFoundPoint
            pyautogui.click(friendNotFoundX, friendNotFoundY)
            time.sleep(timeDelay)
            continue
        except:
            pass
        

