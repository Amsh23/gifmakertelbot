# 📌 Telegram GIF Maker Bot


## About This Project This project was created as part of my personal AI experiments. It combines my own ideas with code and content generated using tools like ChatGPT. The main purpose is to explore and test how AI can assist in development and creativity. *Note: This is an AI-assisted project made for learning and experimentation.*

A simple and efficient Telegram bot that allows users to convert their images into animated GIFs. Just send images to the bot, and it will generate a smooth GIF from them!

## 🚀 Features
- 📷 **Image to GIF**: Send multiple images, and the bot will create an animated GIF.
- ⏳ **Custom Timing**: GIFs are created with a smooth transition (500ms per frame).
- 🏗 **Auto Cleanup**: Uploaded images and generated GIFs are deleted after processing.
- 🌐 **Error Handling**: Handles network timeouts and unexpected errors gracefully.

## 🛠 Setup & Installation

### 1️⃣ Prerequisites
- Python 3.8+
- A Telegram bot token (Get it from [@BotFather](https://t.me/BotFather))
- Install dependencies:
  ```sh
  pip install python-telegram-bot==20.0.1 python-dotenv pillow
  ```

### 2️⃣ Configuration
- Create a `.env` file and add your bot token:
  ```
  TELEGRAM_BOT_TOKEN=your_bot_token_here
  ```

### 3️⃣ Run the Bot
```sh
python bot.py
```

## 📝 Usage
1. Start the bot with `/start`
2. Send at least **two images**
3. Run `/makegif` to generate a GIF
4. The bot will send back an animated GIF!

## 🛡 Error Handling
- **Timeouts:** If a network timeout occurs, the bot will notify the user.
- **File Errors:** If images cannot be processed, an error message is sent.
- **Minimum Image Requirement:** At least two images must be sent before making a GIF.

## 📜 License
This project is open-source under the **MIT License**.

## 📬 Contact
For suggestions or contributions, feel free to open an issue or fork the project on GitHub!

---

## 🤖 AI-Powered Development
This Telegram bot was created entirely with the help of **ChatGPT**. All code was generated using AI assistance.

## 🔥 Keep the Bot Running Forever!
If anyone is interested, we can work together to keep this bot running **permanently** on a server. Contributions and ideas are welcome!

## 🌱 Contributing
Want to help improve this bot? Follow these steps:

1. **Fork the Repository**: Click on the `Fork` button in GitHub.
2. **Clone Your Fork**:
   ```sh
   git clone https://github.com/your-username/telegram-gif-bot.git
   cd telegram-gif-bot
   ```
3. **Create a New Branch**:
   ```sh
   git checkout -b feature-branch
   ```
4. **Make Changes and Commit**:
   ```sh
   git add .
   git commit -m "Added a new feature"
   ```
5. **Push Changes**:
   ```sh
   git push origin feature-branch
   ```
6. **Create a Pull Request**: Go to the original repository and submit a Pull Request.

Looking forward to collaborating! 🚀

