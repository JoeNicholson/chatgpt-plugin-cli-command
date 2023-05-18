import json
import logging
import quart
import quart_cors
from quart import request
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load settings
with open("settings.json") as f:
    settings = json.load(f)
cwd = settings.get("working_directory", ".")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/command")
async def command():
    data = await request.get_json()
    command = data.get("command", "")
    logging.info(f"Received command: {command}")

    try:
        my_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd)
        stdout, stderr = my_process.communicate()
        if my_process.returncode != 0:
            return quart.Response(response=stderr.decode("utf-8"), status=500)
        else:
            return quart.Response(response=stdout.decode("utf-8"), status=200)
    except Exception as e:
        logging.error(f"Error executing command: {e}")
        return quart.Response(response=str(e), status=500)

 
@app.get("/logo.png")
async def plugin_logo():
    filename = "logo.png"
    return await quart.send_file(filename, mimetype="image/png")

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers["Host"]
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers["Host"]
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5004)

if __name__ == "__main__":
    main()
