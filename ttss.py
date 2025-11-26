from flask import Flask, send_file, jsonify
from gtts import gTTS
import os

app = Flask(__name__)
OUTPUT_FILE = os.path.join(os.getcwd(), "output.mp3")

@app.route("/tts", methods=["GET"])
def tts():
    text = "Hi ahmad"
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(OUTPUT_FILE)
        return send_file(OUTPUT_FILE, mimetype="audio/mpeg", as_attachment=True)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

