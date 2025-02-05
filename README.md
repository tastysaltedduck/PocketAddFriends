Relearning how to code, one script at a time!

The script is nothing special. Start at the "Friends Tab" in PTCGP and run the python script through VSCode.

It is not fast. To reduce the possibility of being flagged for botting, the script goes about as fast as a human could do it.

**USE AT YOUR OWN RISK**

# Requirements:

[VSCode](https://code.visualstudio.com/)

[Python 3](https://www.python.org/downloads/windows/)

[MuMu](https://www.mumuplayer.com/)

Grab the game's apk from here:

[APK Mirror](https://www.apkmirror.com/)

# How to run it

  1. After installing VSCode, Python, and Mumu, download the APK and drag it into the MuMu window.
  2. Install the game to MuMu, open the game, and sync your Google or Nintendo account.
  3. Once MuMu is setup, download the repo as a zip or clone the repo. You can do this by clicking the green "Code" button in the top right of the repo.
  4. Open the PocketAddFriends.py in VSCode.
  5. Open ids.txt and add the list of IDs to add. Look at example.txt as an example. Remember to remove your own!
  6. Press Ctrl + ` or go to the top and click on "View" and then "Terminal"
  7. In the terminal, you want to run the following commands one by one
       - pip install pyautogui
       - pip install pynput
       - pip install opencv-python
  8. Open PTCGP and go the "Friends" tab
  9. In VSCode, there is a small play button in the top-right. Click it to run the script.
  10. There will be failures! You have to retake the screenshots.
        - Be careful not to take a screenshot near where the red dot shows up. Look at the images in the repo as examples. Some look like they are cutoff, but that's on purpose.
        - I used [Greenshot](https://getgreenshot.org/)
        - Make sure the new screenshots are "Clickable" at the center. The script always clicks at the center of the found image.

# IMPORTANT! THINGS TO DO BEFORE RUNNING!:

- YOU WILL NEED TO RETAKE THE SCREENSHOTS. This is because of monitors having different DPI and Scaling settings.

- Copy and Paste a list of friend codes. Look at the example.txt. Also remember to remove your own!

# Notes

- The script needs to maintain focus on the emulator, you can run it and leave it for about 10 mins

# Thanks to:

[pyautogui](https://github.com/asweigart/pyautogui)
