import os
from supabase import create_client,Client
from dotenv import load_dotenv

load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb: Client=create_client(url,key)

def up(pid,s):
    res=sb.table("products").update({"stock":s}).eq("product_id",pid).execute()
    return res
if __name__ == "__main__":
    pid = int(input("Enter product_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = up(pid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 