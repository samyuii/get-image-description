import boto3
import openai
import pyttsx3

aws_access_key = 'AKIAQJssdUH7ASYGEB'
aws_secret_key = 'd7K6RNF0ATu+1lwJYoawcutVR4h'
openai.api_key = 'sk-5FLnU0a4ORqB7oxFJq0qtKFPRBNsBxAoyEubs'

def detect_labels(image_path):
    client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = client.detect_labels(Image={'Bytes': image_bytes})

    label_names = [label['Name'] for label in response['Labels']]
    return label_names

def generate_response(prompt):
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo-0301",
              messages=[{"role": "system", "content": 'You are a helpful assistant who is accompaning a blind person'},
                        {"role": "user", "content": prompt}
              ])

    return response.choices[0].message['content'].strip()

def main():
    # Initialize pyttsx3 engine with customized voice settings
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Choose the voice you prefer
    # You can change the index value to select a different voice
    selected_voice = voices[1]  # Adjust this index value as needed

    # Set the selected voice
    engine.setProperty('voice', selected_voice.id)

    # Adjust rate and volume for naturalness and emphasis
    engine.setProperty('rate', 150)  # Adjust the rate value as needed
    engine.setProperty('volume', 1.0)  # Adjust the volume level (0.0 to 1.0)

    while True:
        image_path = input("Enter the path to the image: ")
        
        if image_path.lower() == 'exit':
            print("Exiting the program.")
            break
        
        labels = detect_labels(image_path)
        prompt = "Image labels: " + ", ".join(labels) + "\n"
        user_prompt = "i have given you some keywords and from them you have to describe a scenario out of them keep the tone and manner in a way like you are describibg a scenario to a blind person. with compassionate keep the description short and easy and also talk like you with that person " + "\n"
        prompt += user_prompt
        
        response_text = generate_response(prompt)
        print("ChatGPT:", response_text)
        
        # Speak the response aloud with customized voice settings
        engine.say(response_text)
        engine.runAndWait()

if _name_ == "_main_":
    main()
