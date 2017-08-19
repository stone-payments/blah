from sanic.response import json

async def health_check(request):
    return json({
        "message": "Help, I'm alive. My S2 keeps beating like a hammer"
    })
