# *Mimosa* - Multi-Modal Smart Home Assistance
### Extension of Multi-modality in Smart Home Assistance Systems for People with Impairments
*Currently under development*

## *Mimosa* Backend
This repository serves as the backend for a corresponding Graphical User Interface (GUI).  
It offers an API to send audio files to in order to perform an action 
according to the corresponding intent of the command given in the audio.  

The projects modules ship in various Docker Containers occupying the following ports:  


## *Mimosa* GUI
To add a GUI to the backend build in this project, 
install the [Mimosa GUI](https://github.com/tdilger/Mimosa-GUI).

For detailed information about the project build process, please visit:

[Overleaf Project [Read-Only]](https://www.overleaf.com/read/bcfpfmccrrvq)  
[Overview PDF (ger)](tdilger-ma-ueberblick-02.pdf)

## Installation
To install the *Mimosa* smart Home Assistance, follow the steps below.  

**Git**  
```
git clone https://gitlab.ub.uni-bielefeld.de/mas-projects/smart-home-voice-assistant
cd smart-home-voice-assistant
bash ./install.sh
```

## Development
If you're a developer, you are encouraged to use the Makefile in the root directory.  
List all options by typing `make`.  
You can build docker images and run and stop containers of the different modules separately.  
Additionally, tests can be run and the code can be lint-checked. 
The documentation can be build and deployed as well.

### Research ([Link](./research.md))

- Speech Assistance for people with Impairments
- Multimodal Speech Recognition
- Open Source Voice Assistance


### Hardware ([Link](./hardware.md))

- intel NUC Model D54250WYKH (2014)
- FRITZ!Box 3490
- Phillips Hue Light Bulbs and Hue Bridge control center


### User Stories ([Link](./user-stories.md))

### Hypothesis

The time it takes to perform the tasks in the different use cases will be less given multi-modal input.

The user will be more satisfied working with a multi-modal speech assistance than without.

## Contributing

You are warmly invited to participate enhancing this project.
If you want to contribute:

1. Create an issue describing the feature 
2. Clone the repository
3. Create an individual branch for your extension or fixup
4. Submit a pull request describing your changes onto the development branch.

## Build on
The *Mimosa* Smart Home Assistance is build on various frameworks and tools:  
- [Base Cube One](https://basecubeone.org/): Smart Home framework based on OpenHAB and 
used to communicate with *Smart Devices* of different manufacturers.  
- [RASA Open Source](https://rasa.com/docs/rasa/): Machine learning framework used for 
NLU conversation automation.
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo): Conversational AI toolkit used for *ASR* and *STT*.

### License

This project is licensed under the Apache License, Version 2.0. [License](LICENSE).  
Copyright 2022 by Tim Dilger.
