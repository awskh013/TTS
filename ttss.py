from flask import Flask, send_file, jsonify, request
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        text = data["text"]

        # Unique filename for each request
        output_file = os.path.join(os.getcwd(), f"{uuid.uuid4()}.mp3")

        tts = gTTS(text=text, lang='en')
        tts.save(output_file)

        return send_file(
            output_file,
            mimetype="audio/mpeg",
            as_attachment=True,
            download_name="speech.mp3"
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
