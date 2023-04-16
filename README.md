# python-cv-ai-intro

Small introduction to python, opencv and ai. See `docs/Readme.md` directory for a guide how to use this repository regarding BOGY 2023.

## Setup

1. Open a command prompt or terminal somewhere and clone this repository with: 

`git clone https://github.com/tml444/python-cv-ai-intro.git`

2. Create conda environment by running the following command:

`conda create -n cvintro python=3.7 -y`

3. Activate the environment with:

`conda activate cvintro`

4. Install dependencies:

`pip install tensorflow opencv-python jupyter mediapipe matplotlib ` (opencv-python and jupyter are necessary for 2 and mediapipe and matplotlib additionally for 3)

5. Open Visual Studio Code and open the directory where you cloned this repository. Start with 1_python_basics and go on with 2.. and 3..

`cd python-cv-ai-intro`  
`code .`  

6. After opening your first script (hello world in 1_python_basics), select the correct conda environment in the bottom right corner, select "cvintro".




## Problem handling

- webcam starts very slow under windows: export env variable -> OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS=0, e.g. directly in script via ``os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]=0``
