# Subway Voice Assistant

### Files from the repo that are used

1. test.csv
2. train.csv
3. valid.csv
4. base_config.cfg
5. dialogue_policy.csv
6. slot_annotated_utterances.csv

You do not have to upload these files into the ___VoiceAssistantforSubway.ipynb___ colab file. Executing the __!wget__ code will upload them into the colab instance.

There are 5 modules in the ___VoiceAssistantforSubway.ipynb___ colab file. Namely:

1. ASR
2. Intent Dectection
3. Slot Detection
4. DST
5. TTS
6. Integrated Voice Assistant 

## Integrated Voice Assistant

This module is where one executes the voice assistant. It will record the voice and create and audio.wav file which will be used by the ASR to convert speech into text. Then the utterance text will be passed through the intent detector to find the intent and the slot detector to find the entity and its slot. It will look through the dialog policy and pick the appropriate reponse. The responses will have a placement tag of <ref> which will be replaced by the normalized term (ex: official name of the item from the menu). The response will then be passed through the TTS to give out the voice audio response of the assistant. 

Once you execute the Integrated VA, it will immediately start recording your command and once you stop the recording, it will give a response to your command.

