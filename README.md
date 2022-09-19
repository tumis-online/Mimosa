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
`git clone https://gitlab.ub.uni-bielefeld.de/mas-projects/smart-home-voice-assistant`



### Research ([Link](./research.md))

- Speech Assistance for people with Impairments
- Multimodal Speech Recognition
- Open Source Voice Assistance



### Hardware ([Link](./hardware.md))

- intel NUC Model D54250WYKH (2014)
- FRITZ!Box 3490
- Phillips Hue Light Bulbs and Hue Bridge control center



### User Stories

**Scene 1**  
*Kitchen*, *Lights kitchen* workspace bright, other lights dimmed. Music playing (e.g. Jazz) in background. Different recipes will be presented.

**Scene 2**  
Dinner in *dining room*, lamp bright, other *lights* dimmed or off, calm music (e.g. Piano).

**Scene 3**  
*Living Room* TV, dim lights next to the TV and switch off others. Start TV. Music off.  

-----
**Use Case 1**  
User wants to create *Scene 1*. 

**Use Case 2**  
User wants to change music in *Scene 2*.

**Use Case 3**  
User wants to add a *new light*.

**Use Case 4**  
User wants to add a new scene (*Scene 3*).

**Use Case 5**  
User wants to know the *current time*.

**Use Case 6**  
User wants to *hear music* [title].



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
