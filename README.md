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
```!pip install -r requirements.txt```

You do not have to upload these files into the ___VoiceAssistantforSubway.ipynb___ colab file. Executing the __!wget__ line will upload them into the colab instance.


## Integrated VA

This module is where one executes the voice assistant. It will record the voice and create and audio.wav file which will be used by the ASR to convert speech into text. Then the utterance text will be passed through the intent detector to find the intent and the slot detector to find the entity and its slot. It will look through the dialog policy and pick the appropriate reponse. The responses will have a placement tag of <ref> which will be replaced by the normalized term (ex: official name of the item from the menu). The response will then be passed through the TTS to give out the voice audio response of the assistant. 

Once you execute the Integrated VA, it will immediately start recording your command and once you stop the recording, it will give a response to your command.
    
## NLU
    
The NLU in a TOD is used to extract the user's goal from the utterance. 

### ASR
    
For the ASR we have used the GoogleColabAudio _[5]_ to set up the mic which saves the audio recording in ```audio.wav``` as colab runs in a remote server and does not have access to the built in microphone of the local machine. We have also used the Speech to Text _[6]_ as the ASR along with the recorder.

The output of the ASR is ```user_input``` which is a string type.

### Intent Detector

The intent detector in a TOD extracts the command/action context from the user's utterance based off which a response can be chosen.

There are 6 intents:
    1. Select (used in the prototype)
    2. Deselect (used in the prototype)
    3. Greetings (used in the prototype)
    4. Agree
    5. Disagree
    6. Instead
    
The ```sentences``` variable stores the utterances from ```user_input``` in the NLU and ```text``` stores the ```sentences``` as string type.
The predicted intent is stored in ```classes[label]``` which is the output of the Intent Detector module.

## References
1. https://colab.research.google.com/github/PradipNichite/Youtube-Tutorials/blob/main/Spacy_Custom_NER_Youtube.ipynb#scrollTo=enIOTr8y6hf9 (SPACY NER)
2. https://github.com/amrrs/custom-ner-with-spacy3/blob/main/Custom_NER_with_Spacy3.ipynb (SPACY NER)
3. https://spacy.io/usage/training#config-overrides (SPACT NER base_config.cfg)
4. https://tecoholic.github.io/ner-annotator/ (NER ANNOTATOR)
5. https://pypi.org/project/GoogleAudio/ (COLAB AUDIO RECORDING SETUP)
6. https://www.researchgate.net/publication/358429149_Speech_to_text_in_python Sundiman, Didi. (2022). Speech to text in python. (ASR)
7. https://github.com/mammothtraining/Super-Simple-Text-to-Speech-with-Python-and-Google-Colab/blob/main/01%20Convert%20text%20to%20speech%20with%20gTTS.ipynb (TTS)
8. https://www.youtube.com/watch?v=ngYRYMoIGu8&ab_channel=MammothInteractive (TTS)
9. https://github.com/curiousily/Deep-Learning-For-Hackers/blob/master/18.intent-recognition-with-BERT.ipynb (INTENT DETECTOR)
10.https://curiousily.com/posts/intent-recognition-with-bert-using-keras-and-tensorflow-2/(INTENT DETECTOR)
