This project will locate the nearest Waffle House and tell you how far away you are from it.  This program takes users inputted address and returns distance, and travel time to wherever the nearest Waffle House is in relation to that address, whilst implementing a gui.  When prompted to type address follow the style of this example (900 Oakwood St MI)

**TO RUN**
1. Create a new folder
2. Create and activate a virtual environment.
3. Run the following commands

`pip install setuptools --upgrade`

`pip install --upgrade pip wheel`

`pip install -i https://test.pypi.org/simple/ road-to-waffle-house --extra-index-url https://pypi.org/simple`


**QUICK NOTE**

Since our program uses tkinter to display gui, our program wil not run on an ec2 instance and a normal pc will be needed.

**For deployment:**
1. Files were sorting appropriately according to the layout given in class.
2. Proper pyproject.toml, README, LICENSE, and test folders were also implemented correctly.
3. We installed build tools: 

python3 -m pip install --upgrade build twine

4.  Then the package was built: 

python3 -m build

5.  Test package was then uploaded  

python3 -m twine upload --repository testpypi dist/road_to_waffle_house-*.  

Package is in fact in the appropriate test.pypi place.

6.  The main was set up to automatically start the gui.

7. You will need to install other packages to satisfy the requirements of our road-to-waffle-house package.  Install these first:

To satisfy the tkinter module: winget install "Python 3.x" --source winget

To satisfy the needed steuptool requirements: pip install --upgrade setuptools wheel pip --index-url https://pypi.org/simple

To satisfy the pygame requirments: pip install pygame requests

8.  After those pip installs are completed (which are outside the scope of our project, but are necessary for it to run) This is the pip install for our lab: 

pip install road-to-waffle-house --no-deps -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple 

###############

git clone -b returnCLI  --single-branch  git@github.com:COSC381-2025Winter/lab13-sprint-road-to-waffle-house.git

Make a virtual environment
python3 -m venv .venv
source .venv/bin/activate

Install the requirements.txt
pip install -r requirements.txt

To run program: 
python3 -m src.road_to_waffle_house.distance_matrix 
inside of the "lab13-sprint-road-to-waffle-house" directory
