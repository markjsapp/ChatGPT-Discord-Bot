# Discord Chatbot with GPT-3

This is a Python-based chatbot for Discord that uses the OpenAI GPT-3 API to answer user/chat's questions. The bot is hosted on Heroku and is integrated with Integromat to send and receive messages.

# Prerequisites

To use this bot, you will need:
    A Discord account and a server to which you have administrative access.
    An OpenAI GPT-3 API key and credentials.
    A Discord developer account, created bot, and API credentials
    A Heroku account and Heroku CLI installed on your machine.
    An Integromat account to set up the webhook integration.

## Setup
    Clone this repository to your local machine.
    Create a new Discord bot application and add it to your server.
    Copy the bot token and add it to the config.ini file.
    Install the required Python packages (discord.py and requests) using pip.
    Create a new Heroku app and deploy the bot code using Git.
    Add the Heroku app URL to the config.ini file.
    Create a new scenario in Integromat and set up the webhook to send requests to the Heroku app.
    In the scenario, use the JSON module to parse the response from the GPT-3 API and extract the answer.
    Use another module to send the answer back to the Discord chat as a message.

## Usage

To use the bot, simply type your question into the Discord chat (with the command !ask) and the bot will respond with an answer. You can customize the bot's responses by modifying the GPT-3 API parameters and prompts.

## Creator
Mark S. & ChatGPT

## License

This project is licensed under the MIT License.