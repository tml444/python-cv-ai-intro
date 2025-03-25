_Hint: scroll down for english version_

# Python-cv-ai-Einführung (de)
Kleine Einführung in Python, OpenCV und KI.

## Voraussetzungen
- Visual Studio Code
- Anaconda
- Git

## Einrichtung
1. Öffnen Sie ein Kommandozeilenfenster oder Terminal (Eingabeaufforderung) an einem geeigneten Ort und klonen Sie dieses Repository mit dem Befehl:
`git clone https://github.com/tml444/python-cv-ai-intro.git`
2. Erstellen Sie eine Conda-Umgebung, indem Sie den folgenden Befehl ausführen:
`conda create -n cvintro python=3.10 -y`
3. Aktivieren Sie die Umgebung mit:
`conda activate cvintro`
4. Installieren Sie Abhängigkeiten:
`pip install tensorflow opencv-python jupyter mediapipe matplotlib` (jupyter ist erforderlich für 1, opencv-python zusätzlich für 2 und der Rest zusätzlich für 3)
5. Öffnen Sie Visual Studio Code und öffnen Sie das Verzeichnis, in dem Sie dieses Repository geklont haben:
`cd python-cv-ai-intro`  
`code .`  
6. Nachdem Sie Ihr erstes Skript geöffnet haben (python_basics.ipynb in 1_python_basics), wählen Sie im oberen rechten Bereich den korrekten Kernel aus, wählen Sie "Anderen Kernel auswählen --> Python-Umgebung --> cvintro".
7. Beginnen Sie mit der Bearbeitung von 1_python_basics und gehen Sie dann weiter zu 2. und 3..

## Teachable Machine: Ausprobieren einer KI
Versuchen Sie den folgenden Link aus: https://teachablemachine.withgoogle.com/train 

## Problemlösung
- Die Webcam startet unter Windows sehr langsam: Exportieren Sie die Umgebungsvariable -> OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS=0, z.B. direkt im Skript über ``os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]=0``

# Python-cv-ai-intro (en)
Small introduction to python, opencv and ai.

## Prerequisites
-	Visual Studio Code
-	Anaconda
-	Git

## Setup
1. Open a command prompt or terminal somewhere and clone this repository with: 
`git clone https://github.com/tml444/python-cv-ai-intro.git`
2. Create conda environment by running the following command:
`conda create -n cvintro python=3.10 -y`
3. Activate the environment with:
`conda activate cvintro`
4. Install dependencies:
`pip install tensorflow opencv-python jupyter mediapipe matplotlib` (jupyter is necessary for 1, opencv-python additionally for 2 and the rest additionally for 3)
5. Open Visual Studio Code and open the directory where you cloned this repository: 
`cd python-cv-ai-intro`  
`code .`  
6. After opening your first script (python_basics.ipynb in 1_python_basics), select the correct kernel in the top right corner, select "Select different kernel --> python environment --> cvintro".
7. Start with 1_python_basics and go on with 2. and 3..


## Teachable machine: Playing with AI
Try out the following link: https://teachablemachine.withgoogle.com/train 

## Problem handling
- webcam starts very slow under windows: export env variable -> OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS=0, e.g. directly in script via ``os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]=0``