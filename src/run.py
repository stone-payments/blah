from sanic import Sanic
from sanic.response import json
import os

app = Sanic()

@app.route("/")
async def health_check(request):
    return json({
        "message": "Help, I'm alive. My heart keeps beating like a hammer."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))