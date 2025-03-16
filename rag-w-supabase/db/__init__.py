from supabase.client import Client, create_client
from config import supabase_url, supabase_key

supabase: Client = create_client(supabase_url, supabase_key)