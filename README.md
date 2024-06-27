# Image-Based Assistant for the Visually Impaired

This repository contains two Python scripts designed to assist visually impaired individuals by using image recognition and text-to-speech technology. \
- The first script allows users to upload an image and receive a descriptive scenario based on detected labels. 
- The second script uses a webcam to capture images, detects labels, and provides descriptive scenarios, all while incorporating voice output to communicate with the user in real-time.

## Features
- Image Label Detection: Uses AWS Rekognition to detect labels from images.
- Natural Language Processing: Uses OpenAI's GPT-3.5 to generate compassionate and descriptive scenarios from detected labels.
- Text-to-Speech: Uses pyttsx3 and Google Text-to-Speech (gTTS) for voice output.
- Webcam Integration: Captures images using a webcam, processes them, and provides real-time descriptions.
  
## Prerequisites
- Python 3.6 or higher
- AWS Account with Rekognition service enabled
- OpenAI API Key
- Required Python packages (listed in requirements.txt)

## Installation
1. Clone this repository:
   ```python
   git clone https://github.com/theSamyak/image-assistant.git
   cd image-assistant
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your AWS and OpenAI credentials:
  ```python
  aws_access_key = 'YOUR_AWS_ACCESS_KEY'
  aws_secret_key = 'YOUR_AWS_SECRET_KEY'
  openai.api_key = 'YOUR_OPENAI_API_KEY'
  ```
Replace the placeholders in the script with your actual AWS and OpenAI keys.


## Script 1: Image Upload and Description
Run the script: 

```bash
python image_upload.py
```

This script allows users to upload an image, detects labels using AWS Rekognition, and generates a descriptive scenario using OpenAI's GPT-3.5 model. The response is then read aloud using pyttsx3.

## Script 2: Webcam Capture and Real-Time Description
Run the script:

```bash
python webcam_capture.py
```

This script captures images from the webcam, processes them to detect labels, and generates descriptive scenarios. The descriptive text is converted to speech using gTTS and played using the pygame mixer module, providing real-time voice output.


## Voice Settings Customization
In image_upload.py, the pyttsx3 engine is initialized with customized voice settings for naturalness and emphasis. You can adjust the rate, volume, and voice according to your preferences:

```python
# Initialize pyttsx3 engine with customized voice settings
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Choose the voice you prefer
selected_voice = voices[1]  # Adjust this index value as needed

# Set the selected voice
engine.setProperty('voice', selected_voice.id)

# Adjust rate and volume for naturalness and emphasis
engine.setProperty('rate', 150)  # Adjust the rate value as needed
engine.setProperty('volume', 1.0)  # Adjust the volume level (0.0 to 1.0)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements
- AWS Rekognition for image label detection.
- OpenAI for the GPT-3.5 model.
- pyttsx3 for text-to-speech conversion.
- gTTS for Google Text-to-Speech.
- pygame for playing audio files.
