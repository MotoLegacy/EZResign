# EZResign
Python script to easily resign PlayStation 3 .PKGs and their respective .RAP files for use with PS3Han, using [PS3Xploit/PS3xploit-resigner 2.0.0](https://github.com/PS3Xploit/PS3xploit-resigner).

## Prerequisites:
* Python 3.X (to run EZResign)
* Python 2.7 (to run PS3xploit-resigner)
* WINE (for Linux users.. UNTESTED!)
* Your console's idps.hex and act.dat placed in EZResign's bin folder

## Usage
1. Place all .PKGs and .RAPs in the same directory as EZResign.py
2. Run EZResign.py
3. After the scipt has completed, put ALL files located in the output folder on the root of your USB stick
4. Install the .PKGs with your PS3's Package Manager

## To-Do
* Script clean-up
* Update PS3xploit-resigner (for native Linux binary)
* Edit PS3xploit-resigner to work with Python 3.X

## Special Thanks
* esc0rtd3w, bguerville, Habib, and other members of the PS3xploit Team
* stbrenner for [SilentCMD](https://github.com/stbrenner/SilentCMD)
