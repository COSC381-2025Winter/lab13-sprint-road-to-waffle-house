This project will locate the nearest Waffle House and tell you how far away you are from it.  This program takes users inputted address and returns distance, and travel time to wherever the nearest Waffle House is in relation to that address, whilst implementing a gui.  When prompted to type address follow the style of this example (900 Oakwood St MI)

**TO RUN**

For either platform, please setup the virtual environment and download all packages from requirements.txt
   
If using powershell:
1. ```$env:PYTHONPATH = "src"```
2. ```python -m road_to_waffle_house.main```
   
If using bash
1. ``` export PYTHONPATH="/home/ubuntu/road_to_wafflehouse"```
2. ``` python -m src.road_to_waffle_house.main```

**QUICK NOTE**

Since our program uses tkinter to display gui, our program wil not run on an ec2 instance and a normal pc will be needed.

**For deployment:**
1. Files were sorting appropriately according to the layout given in class.
2. Proper pyproject.toml, README, LICENSE, and test folders were also implemented correctly.
3. We installed build tools: python3 -m pip install --upgrade build twine
4.  Then the package was built: python3 -m build
5.  Test package was then uploaded  python3 -m twine upload --repository testpypi dist/road_to_waffle_house-*.  Package is in fact in the appropriate test.pypi place.
6.  The main was set up to automatically start the gui.
