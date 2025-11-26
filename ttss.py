from flask import Flask, send_file, jsonify
import asyncio
import edge_tts
import os

app = Flask(__name__)
OUTPUT_FILE = os.path.join(os.getcwd(), "output.mp3")

async def text_to_speech(text, voice="en-US-JennyNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(OUTPUT_FILE)

@app.route("/tts", methods=["GET"])
def tts():
    text = "Hi Haaamooodi"
    voice = "en-US-JennyNeural"

    try:
        asyncio.run(text_to_speech(text, voice))
        return send_file(OUTPUT_FILE, mimetype="audio/mpeg", as_attachment=True)

    except Exception as e:
        print("🔥 ERROR OCCURRED:", e)
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

