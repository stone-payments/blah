from sanic.response import json
from models.call import Call
from services.call import add_call
import mongoengine

async def create_call(request):
    return_data = {"messages" : [], "success": False, "data": {}}
    if not request.json:
        return json(return_data, status=400)
    call_details = request.json
    return_data['data'] = add_call(call_details['file_uri'], call_details['metadata'])
    return_data['success'] = True
    return json(return_data)