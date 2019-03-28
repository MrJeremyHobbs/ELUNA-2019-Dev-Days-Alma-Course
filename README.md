# ELUNA 2019 Dev Days+ Alma Course

## Setup and Requirements
### Python
Python 3.6.2 (https://www.python.org/downloads/release/python-362/)

Though there is a newer version, I recommend using this for now. It works with all the modules we will be using and is compatible with PyInstaller, a popular module to create your own executable files. It’s also the version I will be using during the demo.

You will also need to install the following modules: requests and xmltodict.

You can install these using pip by typing “pip3 install requests” and “pip3 install xmltodict” into your command line.

You can test your installation by running this file: https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course/blob/master/0%20-%20setup%20and%20tests/TEST.py

Easy installation guide: https://tutorial.djangogirls.org/en/python_installation/
More technical guide: https://docs.python-guide.org/starting/installation/

## Code Editor
Plain-text editor of your choice. 
Windows users: I recommend Notepad++.
Mac users, I recommend: SublimeText (evaluation version is fine).

For some other options and an explanation of why using a plain-text editor is important: https://tutorial.djangogirls.org/en/code_editor/

## API Key
You will need to create an API key for your institution that has the following permissions:

-BIBS (PRODUCTION read)
-CONFIGURATION (PRODUCTION read/write)

Keep a copy of this key in a secure location and have it ready for the workshop.

For security reasons, I recommend you delete this key after the workshop and create a new key afterwards.

For more info on API keys in Alma: https://developers.exlibrisgroup.com/alma/apis/

## Create a Set
You will need to create an itemized physical items set in Alma and have the "set id" on hand for the workshop (see below).

![Alt text](https://github.com/MrJeremyHobbs/ELUNA-2019-Dev-Days-Alma-Course/blob/master/images/screenshot.png?raw=true "Screenshot")
 
## BYOB (Bring Your Own Barcodes)
You will need at least 10 barcode numbers to actual items in your collection that you can place in the program and add to the set you created. Make sure these are items that have active records in the system (not old withdrawn books). 

You don’t have to have the actual books in hand, just the numbers in a text file. 

Nothing will happen to these records except being added to a set in Alma, so no need to worry about harming any data.

## Last Thoughts
If you need any help with these steps, please reach out to Jeremy Hobbs (jthobbs@calpoly.edu) or the other members of this workshop team.

Though there will be people on hand to help with technical issues should they arise, our goal is to have all these ducks in a row so we can get straight to coding.
