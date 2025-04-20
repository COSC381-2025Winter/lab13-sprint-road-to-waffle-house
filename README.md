1. Since our program has a GUI, it will not run on the ec2 instances.
2. When prompted to type address follow the style of this example (900 Oakwood St MI)

For deployment:
1. Files were sorting appropriately according to the layout given in class.
2. Proper pyproject.toml, README, LICENSE, and test folders were also implemented correctly.
3. We installed build tools: python3 -m pip install --upgrade build twine
4.  Then the package was built: python3 -m build
5.  Test package was then uploaded  python3 -m twine upload --repository testpypi dist/road_to_waffle_house-*.  Package is in fact in the appropriate test.pypi place.
6.  The main was set up to automatically start the gui.