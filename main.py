import json
import quart
import quart_cors
from quart import request
import subprocess


app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/command")
async def command():
    data = await request.get_json()
    print(data)
    command = data.get('command', '')
    # Print the command to the console
    print(command)
    # Run the command
    my_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Get the output
    stdout, stderr = my_process.communicate()
    # Return the output
    return quart.Response(response=stdout.decode("utf-8"), status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5004)

if __name__ == "__main__":
    main()