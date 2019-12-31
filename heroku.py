import os

os.system("git init")
os.system("git remote add origin https://github.com/erenmetesar/NiceGrill.git")
os.system("git config branch.master.remote origin && git config branch.master.merge refs/heads/master")
try:
    os.remove("Procfile")
    os.remove("runtime.txt")
    os.remove("requirements.txt")
except Exception:
    pass
os.system("git pull")
os.system("pip install -r https://raw.githubusercontent.com/erenmetesar/NiceGrill/master/requirements.txt")
with open("config.py", "w+") as config:
    config.write(
        "API_ID = " + os.environ.get("API_ID", "1234") + "\nAPI_HASH = "
        + repr(os.environ.get("API_HASH", "'1234'")) + "\nSESSION = " + repr(os.environ.get("SESSION", "0"))
        + "\nMONGO_URI = " + repr(os.environ.get("MONGO_URI", "0")))
import nicegrill