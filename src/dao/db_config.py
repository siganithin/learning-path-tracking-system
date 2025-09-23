import os
from dotenv import load_dotenv
from supabase import create_client

# Load .env from project root
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase URL or Key not found. Check your .env file!")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
