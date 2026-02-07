# medium-4-archive-export/app.py
from flask import Flask, request, send_file
import zipfile, os

app = Flask(__name__)

BASE = "/tmp/files"
os.makedirs(BASE, exist_ok=True)

with open("/tmp/flag.txt","w") as f:
    f.write("CTF{medium_archive_file}")

@app.route("/health")
def health():
    return "ok"

@app.route("/export", methods=["POST"])
def export():
    name = request.json.get("name")
    zip_path = "/tmp/out.zip"

    with zipfile.ZipFile(zip_path,"w") as z:
        # BUG: path directly used
        z.write(name, arcname=name)

    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
