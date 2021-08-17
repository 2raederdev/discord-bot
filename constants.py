import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

DISCORD_BOT_TOKEN= os.getenv('DISCORD_BOT_TOKEN')