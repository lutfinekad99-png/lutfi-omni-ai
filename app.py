from flask import Flask, render_template_string, request
import requests, re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    vids = []
    if request.method == "POST":
        q = request.form.get("q")
        # FILTER YOUTUBE AGRESIF - LOGIKA LUTFI.LN
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(f"https://www.youtube.com/results?search_query={q}", headers=headers)
        vids = re.findall(r"watch\?v=(\S{11})", res.text)
        vids = list(dict.fromkeys(vids))[:6]
    
    return render_template_string(HTML_CODE, vids=vids)

HTML_CODE = """
<!DOCTYPE html>
<html style="background:#000; color:#0f0; font-family:monospace;">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L-INV OMNI v17.5</title>
</head>
<body style="padding:20px; text-align:center;">
    <h2 style="color:#fff; text-shadow:0 0 10px #0f0;">LUTFI.LN COGNITIVE SYSTEM</h2>
    
    <form method="POST">
        <input name="q" placeholder="Filter Video YouTube..." style="width:75%; padding:12px; background:#111; color:#0f0; border:1px solid #0f0;">
        <button style="padding:12px; background:#0f0; color:#000; border:none; font-weight:bold;">EKSTRAKSI</button>
    </form>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:15px; margin-top:20px;">
        {% for id in vids %}
        <iframe width="100%" height="200" src="https://www.youtube.com/embed/{{id}}" frameborder="0" allowfullscreen></iframe>
        {% endfor %}
    </div>

    <div style="margin-top:40px; border:2px dashed #0f0; padding:20px; background: rgba(0,255,0,0.05);">
        <h3 style="color:#fff;">UPLOAD & INTERAKSI AI</h3>
        <input type="file" style="margin-bottom:10px;"><br>
        <button style="background:#fff; color:#000; padding:10px 20px; border:none; font-weight:bold;">PUBLIKASIKAN VIDEO SAYA</button>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
