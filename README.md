# #Gesture Functionality Alpha Rover

A repository of a ROS-NODE for gesture functionality in Alpha Rover.

<img src="https://media.giphy.com/media/NbtOHMoDaSoTB9HlSK/giphy-downsized.gif" width="700" height="400" />


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
    
![Screenshot from 2022-11-24 22-18-48](https://user-images.githubusercontent.com/76453036/203893700-8d5263ad-848b-44e2-9e8a-fafdc23c0d92.png)

Press `Ctrl+Shift+T` to open a new terminal tab, then, from the terminal go to the path where the files are located and run the next instruction for the talker.py

    python3 talker.py

![Screenshot from 2022-11-24 22-28-21](https://user-images.githubusercontent.com/76453036/203894972-0b56ce3c-4e1b-441a-86d3-10e7518279b3.png)

In a another new terminal tab run the listener.py

    python3 listener.py

You will see the commands that the talker.py will be sending

![Screenshot from 2022-11-24 22-39-01](https://user-images.githubusercontent.com/76453036/203896785-ed5de2a5-da75-464b-882a-e7a35b214c0c.png)


## Author
**[Universidad de Ibagué - Ingeniería Electrónica.](https://electronica.unibague.edu.co)**

 - [Kevin S. MONTAÑA](https://github.com/TWBauer)

