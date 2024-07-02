
# Discord DM Bot

🚀 **Discord DM Bot** is a powerful and easy-to-use bot that allows you to send direct messages (DMs) to any specified user from your terminal. With robust error handling and secure token management, this bot is perfect for integrating simple DM functionality into your Discord workflow.

![DM Bot](https://github.com/YooSiddhartha41210/Discord-DM-Bot/assets/banner.png) <!-- Placeholder for image -->

## 🌟 Features

- **Send DMs from Terminal**: Send messages to any Discord user directly from your terminal.
- **Exception Handling**: Robust error handling ensures you know exactly what went wrong if something fails.
- **Secure**: Bot token is securely loaded from an environment variable.

## ⚙️ Setup

### Prerequisites

- ![Python](https://img.shields.io/badge/Python-3.8+-blue)
- ![discord.py](https://img.shields.io/badge/discord.py-1.7.3+-blue)
- ![python-dotenv](https://img.shields.io/badge/python--dotenv-0.19.2+-blue)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YooSiddhartha41210/Discord-DM-Bot.git
   cd Discord-DM-Bot
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Dependencies**:
   ```bash
   pip install discord.py python-dotenv
   ```

4. **Create a `.env` File** in the project root and add your bot token:
   ```env
   DISCORD_BOT_TOKEN=your_actual_bot_token_here
   ```

## 🚀 Usage

1. **Run the Bot**:
   ```bash
   python bot.py
   ```

2. **Interact with the Bot**:
   - Enter your username.
   - Confirm you are not a bot by typing `1`.
   - Enter the recipient's user ID.
   - Start typing messages to be sent to the specified user.

### Example Terminal Interaction

```
    ┌──────────────────────────────┐
    │                              │
    │         DM Bot Online        │
    │                              │
    └──────────────────────────────┘

    Made by yoosid41210 😎

Enter your username: sid
Type '1' to confirm you are not a bot: 1
Enter recipient user ID: 1246520830989434903
sid: Hello there!
sid: How are you?
```

## 📋 Error Handling

- If the bot fails to send a message, it will print an appropriate error message in the terminal.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you have suggestions for improvements or want to contribute new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Thanks to the `discord.py` community for their excellent library and support.
- Special thanks to all contributors and users who have helped improve this project.

---

Made with ❤️ by yoosid41210
```

