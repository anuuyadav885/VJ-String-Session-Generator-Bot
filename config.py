from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "24509126"))
API_HASH = environ.get("API_HASH", "2c1e3e02b9e1b0a3f9c7955d5d55a1d5")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7692624621:AAHnW_JShY4EghKpvorRD6xsA-LQgW6ypcg")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6127347210")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "https://t.me/+fK5x8NgiYKQ0ZThl")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://codaga9286:JgH1nbOW5JSXUO4U@cluster0.if4xdya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
