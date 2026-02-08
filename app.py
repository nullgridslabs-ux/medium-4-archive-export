# medium-4-archive-export/app.py
from flask import Flask, request, send_file
import zipfile, os

app = Flask(__name__)

BASE = "/tmp/files"
os.makedirs(BASE, exist_ok=True)

with open("/tmp/flag.txt","w") as f:
    f.write("CTF{medium_archive_file}")

@app.route("/")
def index():
    return """
<h2>Archive Export Service</h2>
<ul>
<li>POST /export</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/export", methods=["POST"])
def export():
    name = request.json.get("name")
    zip_path = "/tmp/out.zip"

    with zipfile.ZipFile(zip_path,"w") as z:
        z.write(name, arcname=name)

    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
