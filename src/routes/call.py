from sanic.response import json

async def add_call(request):
    return json({
        "success": True
    })
