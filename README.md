# Birdfeed

## Initial setup

```
# if not insalled yet run
$ sudo apt install -y python3-picamera2 --no-install-recommends
# create a virtual environment with ssystem packages. else picamera2 is not available
# it's recommended to install picamera2 via apt, and not with pip.
$ python3 -m venv --system-site-packages env
# activate environment
$ source ./venv/bin/activate
# install dependencies
$ pip install -r requirements.txt
# initialize pre-commits
$ pre-commit install
```
## Usage

```
# activate virtual environment
$ source ./venv/bin/activate
```
