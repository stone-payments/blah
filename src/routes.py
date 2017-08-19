from sanic.response import json

async def health_check(request):
    return json({
        "message": "Help, I'm alive. My heart keeps beating like a hammer."
    })
