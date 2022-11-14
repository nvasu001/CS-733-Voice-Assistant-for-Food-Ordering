# CS-733-Voice-Assistant-for-Food-Ordering
NLP project

//to do this we need python version 3.8
virtualenv --python=python3.8 .venv
source .venv/bin/activate
which python
python3 -m pip install requests
python3 -m pip install --upgrade pip
pip3 install speechrecognition
pip3 install pyttsx3
pip3 install pyaudio
python -m pip install pyaudio
If these step doesn't work for pyaudio {
    pip3 install pyaudio
    python -m pip install pyaudio
}
else{
    brew install portaudio
    brew link --overwrite portaudio
    pip install pyaudio
}

Install Tensorflow:
sudo easy_install --upgrade six
Follow these for macos{
https://www.youtube.com/watch?v=6W8pjnW65Q8
'/Users/saitheja/Downloads/tensorflow_macos/install_venv.sh' -p
.venv
}
else{
pip3 install tensorflow
}
pip3 install neuralintents

https://www.youtube.com/watch?v=F62wb_jfUUw
https://data-flair.training/blogs/install-tensorflow/
https://github.com/apple/tensorflow_macos/releases
https://www.youtube.com/watch?v=6W8pjnW65Q8


pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl