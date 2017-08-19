from sanic.response import json
from models.call import Call
from services.call import add_call
import mongoengine

async def create_call(request):
    return_data = {"messages" : [], "success": False, "data": {}}
    if not request.json:
        return_data['messages'].append('Please provide request body.')
        return json(return_data, status=400)
    call_details = request.json
    if not call_details.get('file_uri'):
        return_data['messages'].append('Please provide file_uri.')
        return json(return_data, status=400)

    call, analysis, messages = add_call(call_details['file_uri'], call_details.get('metadata'))
    return_data['messages'] = messages
    if call is not None:
        return_data['data'] = call.to_json()
        return_data['data']['analysis'] = []
        for al in analysis:
            return_data['data']['analysis'].append(al.to_json())
        return_data['success'] = True
        return json(return_data, status=201)
    return json(return_data, status=400)