from sanic.response import json
from models.call import Call
from services.call import add_call, get_analysis_for_call
import mongoengine
import json as t

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

async def search(request):
    return_data = {"messages" : [], "success": True, "data": {}}
    metadata = request.json
    if metadata is None:
        calls = Call.objects()
    else:
        calls = Call.objects(metadata=metadata)
    return_data['data'] = []
    for call in calls:
        r = call.to_json()
        r['analysis'] = []
        analysis = get_analysis_for_call(call)
        for al in analysis:
            r['analysis'].append(al.to_json())
        return_data['data'].append(r)
    return json(return_data, status=200)
