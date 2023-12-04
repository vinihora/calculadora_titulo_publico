from supabase import create_client, Client

url: str = "https://geghwzramcdyqmnziwwf.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdlZ2h3enJhbWNkeXFtbnppd3dmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA4NDg1NDksImV4cCI6MjAxNjQyNDU0OX0.S_SmrTeOIEJgkdGVpNVcQpF6O9hZ61pdaDXiTk_x-wo"
supabase: Client = create_client(url, key)
user = supabase.auth.sign_in_with_password({ "email": "vinidahora08@gmail.com.com", "password": "tera@capital" })