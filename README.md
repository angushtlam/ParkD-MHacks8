# ParkD-MHacks8

# Why Virtual Environments
Virtual environments are important in Python development because it makes sure the same program will function the same way on different computers.

## How to make it
1. `cd` to the project directory.
2. Install `virtualenv` by typing `pip install virtualenv` in the Terminal
3. Type `virtualenv -p python3 venv` to create your virtual environment.
4. Activate the `virtualenv` by typing `source venv/bin/activate`. You should see a `(venv)` at the beginning of command lines now.
5. Type `pip install -r requirements.txt` to install the libraries used by the program.
6. Now, run `server.py` to start the server by typing `python server.py`
