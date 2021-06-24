# Azure Cognitive Services for Text to Speech

- [Dependencies](#Dependencies)
- [Installation](#installation)
- [Configuration](#configuration)

A simple Python script to leverage Azure Cognitive Services for [Text to Speech](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech)

# Dependencies

- [Python 3.8](https://www.python.org/)
- [Github account](https://github.com/join)
- [Azure Subscription](https://azure.microsoft.com/en-ca/free/)

# Installation

- Deploy [Cognitive Services](https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne) into your Azure Subscription
    - Note **Keys and Endpoint** -> **Key 1**
    - Note **Overview** -> **Location**

# Configuration

- Clone this Github repository
``` git clone https://github.com/jasonvriends/azure-tts.git ```<br/>

- Create a Python virtual environment<br/>
``` python3 -m venv .venv ```

- Source the Python virtual environment<br/>
``` source .venv/bin/activate ```

- Install the required Python packages<br/>
``` pip install -r requirements.txt ```

- Rename .env.template to .env<br/>
``` cp .env.template .env ```

- Replace the following variables with yours<br/>
```
KEY="{KEY1 from Deploying Cognitive Services}"
REGION="{Location from Deploying Cognitive Services}"
```

- Update the text within tts.xml<br/>

- Run the script<br/>
``` python3 main.py ```