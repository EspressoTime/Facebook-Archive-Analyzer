# Facebook-Archive-Analyzer
Reads downloaded Facebook archive to analyze attributes.

## Setup
1. When logged into Facebook click the arrow in the top right and select Settings.  
2. Click Download a copy of your Facebook data below your General Account Settings.  
3. Click Start My Archive.  

Detailed instructions here: https://www.facebook.com/help/302796099745838

Facebook will email a download link to a zip file. 

Extract friends.htm to the same folder as this Python file.

### Prerequisites 

```
sudo pip3 install numpy
sudo pip3 install matplotlib	
sudo apt-get install python3-tk
```

## How to run

`python3 oh_friendCountByYear.py`

## Result

![Example graph](https://github.com/EspressoTime/Facebook-Archive-Analyzer/blob/master/example.png?raw=true)
