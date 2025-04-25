This project will locate the nearest Waffle House and tell you how far away you are from it.  This program takes users inputted address and returns distance, and travel time to wherever the nearest Waffle House is in relation to that address. 

One of the options will be implementing a gui.  The other option will not be using a gui and will run right out of the command prompt.  We will explain this more in detail in a little bit.


#################################################################################
IMPORTANT: This README has 2 sets of instructions.  The first set of instructions is if the user is planning on using a gui to run the program.  The second set of instructions is if the user is not planning on using a gui to run the program.  The deployment for the first set of instructions will be on the main branch.  The deployment for the second set of instructions will be on the return CLI branch. Follow the proper set of instructions based on this criteria.
#################################################################################


###########################
INSTRUCTIONS FOR WHEN USING A GUI (main branch):
###########################

**TO RUN**
1. Create a new folder from your home: 

    Go to ~, and then mkdir "NAME_HERE"

2. Create and activate a virtual environment.

    python3 -m venv "NAME_HERE"
    source NAME_HERE/bin/activate

3. There are packages that need to be installed that are outside the scope of the project and more to do with having correct packages to run a GUI.  Run the following commands:

     pip install setuptools --upgrade

     pip install --upgrade pip wheel

     pip install pygame requests

     pip install -i https://test.pypi.org/simple/ road-to-waffle-house --extra-index-url https://pypi.org/simple
    
    -- WE NEED TO DISCUSS! This is what I had to use, which ones should we include? --

     pip install --upgrade setuptools wheel pip --index-url https://pypi.org/simple

     pip install road-to-waffle-house --no-deps -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple 

4. At this point, the gui should open.  You will be prompted through the steps.  When typing in your location:

You can type in addresses, like this: 
 900 Oakwood St MI

 You can also type in the name of a city or town as your location, like:
 Ann Arbor


**QUICK NOTE**

Since our program uses tkinter to display gui, our program wil not run on an ec2 instance and a normal pc will be needed.  To satisfy the tkinter module: winget install: 

    "Python 3.x" --source winget

**THE DEPLOYMENT STEPS FOR THIS PROJECT:**
1. Files were sorting appropriately according to the layout given in class.
2. Proper pyproject.toml, README, LICENSE, and test folders were also implemented correctly.
3. We installed build tools: 

    python3 -m pip install --upgrade build twine

4.  Then the package was built: 

    python3 -m build

5.  Test package was then uploaded  

    python3 -m twine upload --repository testpypi dist/*  

Package is in fact in the appropriate test.pypi place.

6.  The main was set up to automatically start the gui.

7. You will need to install other packages to satisfy the requirements of our road-to-waffle-house package.  That has been explained above.


8.  After those pip installs are completed (which are outside the scope of our project, but are necessary for it to run) This is the pip install for our lab: 

pip install road-to-waffle-house --no-deps -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple

## DEPLOYMENT STEPS COMPLETED.  HOW TO USE THE GUI IS DESCRIBED ABOVE ##





###########################
INSTRUCTIONS FOR WHEN NOT USING A GUI (returnCLI branch):
###########################


**TO RUN**
1. Create a new folder from your home: 

    Go to ~, and then mkdir "FOLDER_NAME_HERE"


2. Create and activate a virtual environment.

    python3 -m venv "VE_NAME_HERE"
    source NAME_HERE/bin/activate


3. Once activating the virtual environment, use this pip install:

    pip install road-to-waffle-house==0.1.12 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple


4. Once this package has been installed, simply type 'road-to-waffle-house' into the command prompt line, and the API will automatically be activated.  Any wrong inputs will be told to the user and they will be prompted to try again.  

You can type in addresses, like this: 
 900 Oakwood St MI

 You can also type in the name of a city or town as your location, like:
 Ann Arbor



**THE DEPLOYMENT STEPS FOR THIS PROJECT:**
1. Files were sorting appropriately according to the layout given in class.
2. Proper pyproject.toml, README, LICENSE, and test folders were also implemented correctly.
3. We installed build tools: 

    python3 -m pip install --upgrade build twine

4.  Then the package was built: 

    python3 -m build

5.  Test package was then uploaded  

    python3 -m twine upload --repository testpypi dist/*  

Package is in fact in the appropriate test.pypi place.


6.  After those pip installs are completed (which are outside the scope of our project, but are necessary for it to run) This is the pip install for our lab: 

pip install road-to-waffle-house==0.1.12 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple

## DEPLOYMENT STEPS COMPLETED. ##