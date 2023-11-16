# Done in terminal

# Virtual   Environment
# A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

# To create a virtual environment in Python, you can use the venv module that comes with Python. Here's an example of how to create a virtual environment and activate it:

# Create a virtual environment
# python -m venv myenv

# Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate

# Deactivate the virtual environment
# deactivate

# Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat

# if using powershell
# myenv\Scripts\activate.ps1

# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.


# The "requirements.txt" file
# In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:

# Output the list of installed packages and their versions 
# pip freeze 

# Output the list of installed packages and their versions to a file (new file will be created and list will be in it)
# pip freeze > requirements.txt

# To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:

# Install the packages listed in the requirements.txt file
# pip install -r requirements.txt


# Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.


# jo python hmare computer me login h wo global version h hmare computer ka on my computer

# viertual environment me hm virtual python install kr skte hai jo global se alag rhega
# we can add as many python installation as we want and can add whatever/whichever package(of any version) to each of them 
# if we want we can create 10 diffferent virtual env and add 10 different version of same package to them



