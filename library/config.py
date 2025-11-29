from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DP_NAME=os.getenv('DP_NAME')
    DP_HOST=os.getenv('DP_HOST')
    DP_PORT=os.getenv('DP_PORT')
    DP_PASS=os.getenv('DP_PASS')
    DP_USER=os.getenv('DP_USER')
    