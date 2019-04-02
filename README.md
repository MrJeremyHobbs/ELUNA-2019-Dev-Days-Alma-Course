# ELUNA 2019 Dev Days+ Alma Course

## Setup and Requirements
### Python
Python 3.6.2 (https://www.python.org/downloads/release/python-362/)

Though there is a newer version, I recommend using this for now. It works with all the modules we will be using and is compatible with PyInstaller, a popular module to create your own executable files. It’s also the version I will be using during the demo.

Mac users: Installation is simple. Just download and install.

Windows users: Installation is a bit more complicated. I’ve created a short installation guide here: https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course/blob/master/INSTALLATION.md

### Modules
You will need to install the following modules: requests and xmltodict.

You can install these using pip by typing “pip3 install requests” and “pip3 install xmltodict” into your command line.

### Test Your Installation
I’ve created a GitHub page for this course at https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course

Click the green “Clone or Download” button to download the repository to your local machine. 

Unzip the file.

On your local machine, navigate to the “setup and tests” folder and then choose either “mac” or “pc”, based on your setup.

Run the TEST.py file either by opening the file on the desktop or by running the program from the command line by typing “python TEST.py” or “python3 TEST.py” into your command prompt.

You’ll know that you have succeeded when you see the following:
 
![Alt text](https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course/blob/master/images/congratulations.png?raw=true "Screenshot") 

### Code Editor
Install a plain-text editor of your choice. Here are my recommendations:

For Windows users:  Notepad++

For Mac users: TextWrangler (evaluation version is fine, but you’ll get pop-ups)

For some other options and an explanation of why using a plain-text editor is important: https://tutorial.djangogirls.org/en/code_editor/

### Watch your tabs!
Python gets unhappy if you try to mix tabs and spaces in your code. 

If you are a tabs person (like I am), the easiest thing to do is set your code editor to 4 spaces per tab. Instead of inserting a literal tab into your code, it will insert 4 spaces instead.

Notepad++ directions: https://notepad-plus-plus.org/community/topic/16129/how-do-i-tell-notepad-to-use-spaces-to-auto-indent-instead-of-tabs

TextWrangler directions: https://stackoverflow.com/questions/5750361/auto-convert-tab-to-4-spaces-in-textwrangler

### API Key
You will need to create an API key for your institution that has the following permissions:

BIBS (PRODUCTION read)

CONFIGURATION (PRODUCTION read/write)

Keep a copy of this key in a secure location and have it ready for the workshop.

For security reasons, I recommend you delete this key after the workshop and create a new key afterwards.

For more info on API keys in Alma: https://developers.exlibrisgroup.com/alma/apis/

### Create a Set
You will need to create an itemized physical items set in Alma and have the "set id" on hand for the workshop (see below).
 
![Alt text](https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course/blob/master/images/screenshot.png?raw=true "Screenshot") 
 
### BYOB (Bring Your Own Barcodes)
You will need at least 10 barcode numbers to actual items in your collection that you can place in the program and add to the set you created. Make sure these are items that have active records in the system (not old withdrawn books). 
You don’t have to have the actual books in hand, just the numbers in a text file. 
Nothing will happen to these records except being added to a set in Alma, so no need to worry about harming any data.

### Last Thoughts
If you need any help with these steps, please reach out to Jeremy Hobbs (jthobbs@calpoly.edu) or the other members of this workshop team.
Though there will be people on hand to help with technical issues should they arise, our goal is to have all these ducks in a row so we can get straight to coding.