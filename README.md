# Network Debugging Scripts

In order to use it more conviniently, clone the repo and then create a single executable file for the particular script using PyInstaller.

After cloning this repo, change the directory into the folder of the script you want to create single executable of. 

Install PyInstaller:

```bash
pip install pyinstaller
```

Run the below code to make the executable:

```bash
pyinstaller --onefile main.py
```

Once pyinstaller is done with creating the executables, cd into the ```dist``` folder and you'll see the executable. Now simply run it.

For windows guys, it'll be ```main.exe``` which can be simply run by double clicking it.

For UNIX based system users, it'll be ```main``` which can be run by following command:

```bash
./main
```

The infinite loop script will create a log file having all the details of ping at time intervals, which can be chosen by the user. 