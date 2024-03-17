# FastAPI YouTube Generate Prompt

This repository contains a FastAPI application designed to process YouTube video links and user prompts, utilizing the embedchain library to generate relevant responses. 

![App Screenshot](https://github.com/fitriadyaa/youtube-prompt-api/blob/main/Screenshot%202024-03-17%20at%2022.28.16.png?raw=true)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- FastAPI
- Uvicorn (for running the app)
- An OpenAI API Key set as an environment variable

## Installation

Clone the repository to your local machine:


```bash
git clone https://github.com/fitriadyaa/youtube-prompt-api.git
cd youtube-prompt-api
```

Next, install the required dependencies:

```bash
pip install fastapi uvicorn embedchain
```

## Usage
To run the application, set your OpenAI API key as an environment variable and start the Uvicorn server:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
uvicorn main:app --reload
```
The application will be available at http://127.0.0.1:8000. Use the /query/ endpoint to submit YouTube links and prompts as POST requests.

## Support Me ☕

If you find MyGithubUser helpful or just want to support my work, you can buy me a coffee! ☕

<a href="https://www.buymeacoffee.com/fitriadyaa" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
[![Support Me on Saweria](https://img.shields.io/badge/Support%20Me%20on-Saweria-brightgreen)](https://saweria.co/fitriadyaa)
