from pyrogram import Client, filters

# Configuration - replace with your own values
api_id = ""
api_hash = ""
bot_token = ""

# Initialize the bot
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a handler for photo and video messages
@app.on_message(filters.photo | filters.video)
def thanks(client, message):
    message.reply_text("Thanks!")

# Run the bot
app.run()
