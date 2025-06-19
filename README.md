# Snorlax No More <img alt="discord icon" src="https://img.icons8.com/?size=100&id=LOWwEDik1xs8&format=png&color=000000" width="25"/>

<img align="left" alt="transparent image of Orange Unit Style Snorlax" src="https://res.cloudinary.com/dsns0avdz/image/upload/v1749435757/143-orangeunite_lbf1wg.png"> </img>

> It's time to get fit! 🏋️

**Snorlax No More** is a discord bot created as a submission to the [June 2025 Codédex Monthly Challenge](https://www.codedex.io/community/monthly-challenge/4QHMd8GadBZtZbq6W1wD). It's functions include the following:

- Generate a random no-equipment exercise from the excercisedb library if certain keywords are triggered (No command necessary! Snorlax is always listening 👀)
- Saves youtube videos into an csv file and return them in a randomized order on command
- Uses Gemini to recommend ways to improve your health and wellness according to information you share with Snorlax in a questionaire
- Utilizes Gemini to provide quick tips and tricks to beat procrastination, low motivation, lack of discipline concerns

<sub>This project was previously developed in a [private repository](https://github.com/maescha/snorlaxnomore) with over 60 commits (started June 8 2025), now recreated for public access.</sub>

## APIs used

- Discord API
- [Exercisedb API](https://exercisedb-api.vercel.app/)
- [Giphy API](https://developers.giphy.com/docs/api/#quick-start-guide)
- Gemini API

## LLM used

- gemini-2.0-flash

## Set Up

1. Run the following in terminal `py -m pip install discord.py python-dotenv google-genai`

2. Clone this repository

3. Create an environmental/**.env** file in the main directory

- inside the .env, add the following tokens

```
DISCORDBOTTOKEN=
GIPHYAPIKEY=
GEMINIKEY=
```

**How to get Discord Bot Token**

1. Add bot to your [Discord Applications](https://discord.com/developers/applications/) directory
2. Once bot is added, navigate to Bot Settings and click 'Bot'
3. Once on the 'Bot' page, click 'Reset Token' to generate a new Bot Token. Paste the generated token into the .env file

**How to get Giphy API Key**

1. Follow the instructions outlined on the [Giphy API Quick Start Guide](https://developers.giphy.com/docs/api/#quick-start-guide), create or sign into your account and create an API key **NOT** a SDK key

- your unique API key can also be found on the [Giphy Developers dashboard](https://developers.giphy.com/dashboard/) once you sign in
  > - **Note that** API Keys start as beta keys, which are rate limited (100 searches/API calls per hour)

**How to get Gemini API Key**

1. Head over to [Google AI Studio](https://aistudio.google.com/apikey) to get a free Gemini API key
   > - **Note that** Gemini API "free tier" is offered through the API service with lower rate limits for testing purposes. Google AI Studio usage is completely free in all available countries.
   > - [Click here to learn more about Gemini Developer pricing](https://ai.google.dev/gemini-api/docs/pricing)

## How to Run

1. Once all needed files are added, type the following in the terminal:
   `py bot.py` or `python3 bot.py`

   > You will know that you are successfully logged into your Discord server as the bot if you see the following message in your terminal:

   `Logged on as Snorlax No More#0512!`

## Commands & Screenshots

## Future Improvements

- [ ] add logging functionality for excercised minutes
- [ ] add Snorlax leveling in accordance to what is logged
