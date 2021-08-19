# Validere Assessment

Sourcing and analyzing crude oil data.


## Description

This python script fetches publicly available data from [Crude Monitor](https://www.crudemonitor.ca/), based on the crude oil name, crude oil acronym and start and end dates provided by the user. The characteristic of interest is the crude oil's density. The density data is filtered based on the operation (greater than, lesser than, greater than equal to, etc.) and the limit value provided by the user. The results are then printed for the user.


## Installation Instructions

### Run the following commands on your Mac terminal:

1. #### Install the macOS package manager [Homebrew](https://brew.sh/). 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. #### At the end of that installation, you may be provided with next steps that contain two commands. If prompted, run those commands.
```bash
echo 'eval"$(/opt/homebrew/bin/brew shellenv)"' >> /Users/homefolder/.zprofile
```
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

3. #### Use Homebrew to install Python 3.
```bash
brew install python3
```

4. #### Install the package manager pip to install Python libraries.
```bash
curl -0 https://bootstrap.pypa.io/get-pip.py
```
```bash
sudo python3 get-pip.py
```

5. #### a) Use pip to install the libraries required for the script.
```bash
pip3 install pandas
```
```bash
pip3 install requests
```
5. #### b) Or, you can navigate to the folder with the requirements.txt file and run the following command.
```bash
pip3 install -r requirements.txt
```


## Running The Script

Navigate to the folder on your computer where the crude_monitor.py python file is saved, and run the script with the following command:
```bash
python3 crude_monitor.py
```
