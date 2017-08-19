from sanic.response import json
from models.call import Call
from services.call import add_call
import mongoengine

async def create_call(request):
    call_details = request.json
    return_data = {"messages" : [], "success": False, "data": {}}

    return_data['data'] = add_call(call_details['file_uri'], call_details['metadata'])
    return_data['success'] = True
    print(return_data)
    return json(return_data)