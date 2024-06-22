# Image-Based Assistant for the Visually Impaired

This repository contains two Python scripts designed to assist visually impaired individuals by using image recognition and text-to-speech technology. The first script allows users to upload an image and receive a descriptive scenario based on detected labels. The second script uses a webcam to capture images, detects labels, and provides descriptive scenarios, all while incorporating voice output to communicate with the user in real-time.

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
git clone https://github.com/your_username/image-assistant.git
cd image-assistant
```
