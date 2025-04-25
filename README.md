# Road To Waffle House
Ever wanted to know the distance to the nearest Waffle House with ease? Now you can!

## Description

This project will locate the nearest Waffle House and tell you how far away you are from it.  This program takes users inputted address and returns distance, and travel time to wherever the nearest Waffle House is in relation to that address. 

One of the options will be implementing a gui.  The other option will not be using a gui and will run right out of the command prompt.  We will explain this more in detail in a little bit.


## About This README
This README has 2 sets of instructions.  The first set of instructions is if the user is planning on using a gui to run the program.  The second set of instructions is if the user is not planning on using a gui to run the program.  The deployment for the first set of instructions will be on the main branch.  The deployment for the second set of instructions will be on the return CLI branch. Follow the proper set of instructions based on this criteria.
************************************************************************


# Instructions For Using The GUI (Main Branch)

### Installing
1. Create a new folder from your home: 

Go to your home directory, and then mkdir "FOLDER_NAME_HERE"


2. Create and activate a virtual environment.

    python3 -m venv "VE_NAME_HERE"
    source NAME_HERE/bin/activate


3. Once activating the virtual environment, use this pip install:

    pip install road-to-waffle-house==0.1.13 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple

### Executing Program
Once this package has been installed, simply type 'road-to-waffle-house' into the command prompt line, and the API will automatically be activated.  Any wrong inputs will be told to the user, and they will be prompted to try again.

When entering an address, the inputs should follow one of the following:
* Full Mailing Address:  900 Oakwood St, Ypsilanti, MI 48197
* Coordinates: 42.251026, -83.627448
* City, State:  Ann Arbor, MI

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

## End Of Deployment Step

************************************************************************
# INSTRUCTIONS FOR WHEN NOT USING A GUI (returnCLI branch)
************************************************************************

### Installing
1. Create a new folder from your home: 

Go to your home directory, and then mkdir "FOLDER_NAME_HERE"


2. Create and activate a virtual environment.

    python3 -m venv "VE_NAME_HERE"
    source NAME_HERE/bin/activate


3. Once activating the virtual environment, use this pip install:

    pip install road-to-waffle-house==0.1.12 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple

### Executing Program
Once this package has been installed, simply type 'road-to-waffle-house' into the command prompt line, and the API will automatically be activated.  Any wrong inputs will be told to the user, and they will be prompted to try again.  

When entering an address, the inputs should follow one of the following:
* Full Mailing Address:  900 Oakwood St, Ypsilanti, MI 48197
* Coordinates: 42.251026, -83.627448
* City, State:  Ann Arbor, MI

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

## End Of Deployment Step

### Authors
 * Joe Briggs
 * Bear Kennedy
 * Justin Miles
 * Ryan Retan


pip install road-to-waffle-house --no-deps -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple 

It runs out of a gui.
