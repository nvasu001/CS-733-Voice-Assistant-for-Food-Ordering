# Subway Voice Assistant

### Files from the repo that are used in the colab file.

1. test.csv - _it is the intent annotated test dataset_
2. train.csv - _it is the intent annotated train dataset_
3. valid.csv - _it is the intent annotated validation dataset_
4. base_config.cfg - _it is a configuration file for spaCy NER using __Tok2Vec__ which uses CPU and it is optimized for ACCURACY_
5. dialogue_policy.csv 
6. slot_annotated_utterances.csv - _it is the slot and entity annotation dataset for spaCy NER_
7. requirements.txt - _it has all the dependencies for this python project_

You do not have to upload these files into the ___VoiceAssistantforSubway.ipynb___ colab file. Executing the __!wget__ line will upload them into the colab instance.

### There are 5 modules in the ___VoiceAssistantforSubway.ipynb___ colab file. Namely:

1. ASR
2. Intent Dectection
3. Slot Detection
4. DST
5. TTS
6. Integrated Voice Assistant 

## Integrated Voice Assistant

This module is where one executes the voice assistant. It will record the voice and create and audio.wav file which will be used by the ASR to convert speech into text. Then the utterance text will be passed through the intent detector to find the intent and the slot detector to find the entity and its slot. It will look through the dialog policy and pick the appropriate reponse. The responses will have a placement tag of <ref> which will be replaced by the normalized term (ex: official name of the item from the menu). The response will then be passed through the TTS to give out the voice audio response of the assistant. 

Once you execute the Integrated VA, it will immediately start recording your command and once you stop the recording, it will give a response to your command.

