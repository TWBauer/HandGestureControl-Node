# #Gesture Functionality Alpha Rover

A repository of a ROS-NODE for gesture functionality in Alpha Rover



# Software requirements
For this ROS-NODE we need to install the following repositories an requirements.

 - ROS Melodic
 - Python3
 - Python libraries
	 - `sudo apt-get install python-pip`
	 - `pip install numpy`
	 - `pip install mediapipe`

## How to install?

Clone this repository

    git clone https://github.com/TWBauer/Funcionalidad-Gestos-rober.git
    
## How to run?

To run this python script follow this steps

go to the folder where you downloaded the repository and extract the file, you will find two python scripts (talker.py and listener.py)

Open the terminal and run ROS using the next instruction.

    roscore
    
Press `Ctrl+Shift+T` to open a new terminal tab, then, from the terminal go to the path where the files are located and run the next instruction for the talker.py

    python3 talker.py

In a another new terminal tab run the listener.py

    python3 listener.py
You will see the commands that the talker.py will be sending



## Author
**[Universidad de Ibagué - Ingeniería Electrónica.](https://electronica.unibague.edu.co)**

 - [Kevin S. MONTAÑA](https://github.com/TWBauer)

