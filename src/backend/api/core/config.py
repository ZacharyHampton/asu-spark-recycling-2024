import os
from databases import DatabaseURL
from dotenv import load_dotenv

load_dotenv()


if not (MONGODB_URL := os.getenv("MONGODB_URL")):
    raise RuntimeError("MONGODB_URL is not set")
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)
