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

## How it works?

  
![](https://lh4.googleusercontent.com/OXmzbjzN3GmnzSyU8LtxILopqn1GsYUA6R9bNLQYeQ0E-8_5yF33C5-k1oWG08TAsXgJ3M0LSmTb15DmitDhOsGE7jY6ZQdrSM8iTxPRLftT-G7RAT2kEouflGfJEP96b3bYqDpiClT-MFqiuT1g_-vmx7yYd9e_5OsZERnc4SmHfGlSCzcg0RektzW7SA)

![](https://lh4.googleusercontent.com/df8FzYbuKpys5w0np7jtsRqC4_OQEBeYh4IbWfp56gG0HIDLK9NVauoLBq9hWlz7qvO3MRqcVxy6hshDAAK2eSoO6GbMBXEduGZKVyJH1-m_sH-IzNWQ0gDHF0pmp32f7YsX_41AyFBoFVBgFM8175wW-eEB512uw2elXmPtVbLTryorvnaE8JdoSlWo0w)



  

In the Figure we can see that when the 5 fingers up gesture is performed, we will get a response from our listener, obtaining the Twist message where all values are at 0 indicating the action "Stop".

  

![](https://lh6.googleusercontent.com/owru_8dZ5K0RvoA9LL-UkXri17GdbdRoZmkXclRdXtYefAIDLN7awpbkw2ARMYmGJOMo4BWqsbMNgtDIFK0xNwBldvGux9bBh9H3tGm5D0ARYAyuyy4THPtM-9MUBrZSwdlqe7Cr7zryumikr83BmBWKxYeMkqZ3HnGJPMM4jRxDfRUO8HolIVaIimKcIg)

![](https://lh5.googleusercontent.com/pmzDtT9aoe_Kdu42JNsjNftf85j6volqNSUshOhbdJ8lkpIU8dYRoFQnMvfVhhOUaXoUzWX8X42qbeIQDMGUCHJIs7RjJpqtyjc1eppbVjB74hxBtflLpGoxwpf57iU8_V2OBHUvXeVTizhgxNBw9hPOpeW4BVeJuwedeQL37JtweW4Yta33nXV6dspEOw)



  

As in the previous figure, we now have the 4-finger gesture where we will obtain the Twist message showing that the variable X = 1 and Z = 0, indicating the action "Advance".

  

![](https://lh3.googleusercontent.com/Qw1pqrYXbyR0x_ctYunLah02s188Fh_KtCMtucjdwrUICDn74kPmpasjgdKl9rne5hUqZd4BGiHnZZbWJmAOVNSPiZYFRUIBsEUFopM6xmXmBNAR4GdTmORQUd8eh7PXadlGhiOtf_d1UzyX3Y8izMlMvyAo7d6a7DEnq-IwY14QExaHFnmDvM8Ppgz8lg)

![](https://lh4.googleusercontent.com/k7r5f1LnVsfIBhpitaWg_INVx7ePGaMrswlzsL-Rojswvwj8eadlXxhkvOU_FfwTLqSn89v9Gl0y4oyeWYQT-T6HTnzX3TpiQ0Gmci5FJfcL3YeNQfHGz8VOkpeN5AN9vkUyA33OGQKfloIB219ROQ26uJUlzjsfPVfo8YeeEeRcEUaa23aj6lGVUlLLBA)



  

As shown in the figure, the Twist message shows the variable X = -1 and Z = 0, indicating the action "Go back".

  

![](https://lh5.googleusercontent.com/va_DED9XgG1VMG_qJTNvzKZk4vcRXgeWn1VzRAwT36UHCilyY59hCU_NtlzGf53M3CrdLuUBDxlV_0p_hscQjXh2RM6dXq7kHsqr5rrliLVOerXiAwDgouOrSfOso0gQXxglor62jd78doaJ4H7swcd6cxIfJJClvhaPz3-Dq2aiFtZ-ucPxqmVAy5OmHA)

![](https://lh4.googleusercontent.com/B70PCynLxMS940BedVJ2rPzeXb5ARebyJv3kn4R6fNULa_tBxTF2D_s41_nJnbv44A4-hini1AHqraw-0IvQyH-Me8V0I5QQarG-hActL7t3FLv47M_DmsjW3KpKzVlNdzCF219xbHFcytZxvOwlkyqm_3-_ARYw9FZGOa_k1NRZshE6DSKPv39ZhcqvMg)



  

The figure shows the Twist message with variable X = 0 and variable Z = 1 indicating the action "Turn Left".

  

![](https://lh5.googleusercontent.com/fQwxSihz-MXX-G1GE4DOJDSD1o_7JazlnBuY5qDBVyC2kpoN36GsrtFTQ8uillbpKjhwjlD5JTKxGmNbaE1LnJPEer6fcEJyElL-dk1fQHZt_LQ7ZUW4O_t8JFUH-x5VGsIdA3hUuHlih0gd5xX-V95HwgvKqfHYcR0BQ7lH0mMUzz39hcL4PYebdo9edA)

![](https://lh4.googleusercontent.com/He98aodjzQGR_eOmEQx6qbluBtJdKyhLiOye9gTLTQxDjKjwKZSRwoLYW3BbpLhMGnXJoqVlWzj-j9MDdxgZ4JzfSXp_2E9E4-4kcJvoxZRfaoTQLiW6Je1jNedfFWkiXPirKqrNli-KUV9n9j5D_UvzoDi56nde_dAkEJV9hs17ksUqOoFZ8EM7hOaN_Q)



  

Seeing the Figure where we obtain a Twist type message showing the variable X = 0 and Z = -1, indicating the action "Turn right".

This code works as a ros node and has a 'Twist' output to be read by the roboclaw node, if you want to test the code without the need to connect through ROS, use the following instruction.

    python3 pruebamano.py

## Author
**[Universidad de Ibagué - Ingeniería Electrónica.](https://electronica.unibague.edu.co)**

 - [Kevin S. MONTAÑA](https://github.com/TWBauer)

