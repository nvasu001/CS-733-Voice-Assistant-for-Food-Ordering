# Subway Voice Assistant

It is a Voice Assistant that will aid one to make an order on Subway food ordering website. It is a Task Oriented Dialogue System that do the task assigned to it and in this case it will be ordering food from subway. 

This project is still at the Prototype stage.

## Table of Contents
- [File from the repo to be used along with the code](#File-from-the-repo-to-be-used-along-with-the-code)
- [Natural Language Understanding (NLU)](#NLU)
    - [Automatic Speech Recognition (ASR)](#ASR)
    - [Intent Detector](#Intent-Detector)
    - [Slot Detector](#Slot-Detector)
- [Dialogue Management (DM)](#DM)
    - [Dialogue Policy (DP)](#DP)
    - [Dialogue State Tracking (DS)](#DS)
- [Natural Language Generation (NLG)](#NLG)
- [Integrated Voice Assistant](#Integrated-VA)


## File from the repo to be used along with the code

1. Dataset containing files (train.csv,test.csv,valid.csv) required to train the __Bert model__ for the intent Detection 
2. base_config.cfg - _it is a configuration file for spaCy NER using __Tok2Vec__ which uses CPU and it is optimized for ACCURACY_
3. dialogue_policy.csv 
4. slot_annotated_utterances.csv - _it is the slot and entity annotation dataset for spaCy NER_
5. requirements.txt - _it has all the dependencies for this python project_

You do not have to upload these files into the ___VoiceAssistantforSubway.ipynb___ colab file. Executing the __!wget__ line will upload them into the colab instance.


## Integrated VA

This module is where one executes the voice assistant. It will record the voice and create and audio.wav file which will be used by the ASR to convert speech into text. Then the utterance text will be passed through the intent detector to find the intent and the slot detector to find the entity and its slot. It will look through the dialog policy and pick the appropriate reponse. The responses will have a placement tag of <ref> which will be replaced by the normalized term (ex: official name of the item from the menu). The response will then be passed through the TTS to give out the voice audio response of the assistant. 

Once you execute the Integrated VA, it will immediately start recording your command and once you stop the recording, it will give a response to your command.

