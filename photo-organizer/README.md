## GitHub
- https://github.com/gabrielfroes/photo-organizer.git

## Install Dev
```
 python3 -m venv env
 source env/bin/activate
 pip install -r requirements.txt
```

## Run Manual
```
 python photo-organizer.py 
```

## Install Linux
```
 sudo cp photo-organizer.py /bin
 sudo cp photomanager /bin
```

## Install Windows

1. To generate *photo-organizer.exe* file to run on Windows.

```
pyinstaller -w -F photo-organizer.py
```
- Generate in dist/
- With icone pyinstaller -w -F -i {icon location} {python file}

## Dependency
- sudo apt install python3-venv

### Installing

A step by step series of examples that tell you how to get a development env running

Install Python 3.x with pip

Install Pillow, a Python Imaging Library

```
pip install Pillow
```

Install PyInstaller, to generate .exe file (for Windows)

```
pip install pyinstaller
```


## Running the tests

To run a test, call the script inside a folder with photos.

```
python photo-organizer.py .
```

**For Windows in Context Menu:**

1. To generate *photo-organizer.exe* file to run on Windows.

```
pyinstaller -w -F photo-organizer.py
```

2. Add the keys on Registry or run *photo-organizer.reg*.
3. Copy .exe file on *C:\Program Files\Photo Organizer*
4. Add *C:\Program Files\Photo Organizer* in the *Path* on Windows Environment Variable.

## Contributing

Feel free to submitting pull requests to us.

## Authors

* **Gabriel Froes** - *Initial work* - [Twitter](https://www.twitter.com/gabrielfroes)
* **Vanessa Weber** - *Initial work* - [Twitter](https://www.twitter.com/nessaweberfroes)

## License

This project is licensed under the [GNU General Public License](https://opensource.org/licenses/GPL-3.0).

## Acknowledgments

* First steps in Python language
* Create simple and useful things
* Build code for [Código Fonte TV](https://www.youtube.com/codigofontetv), our Youtube Channel.
