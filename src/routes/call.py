from sanic.response import json
from models.call import Call
from services.call import add_call
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
    begin_date = request.json.get('begin-date')
    end_date = request.json.get('end-date')
    operator = request.json.get('operator')
    search_data = request.json.get('search-data')
    print('{} {} {} {}'.format(begin_date, end_date, operator, search_data))
    print('{$text: {$search: "' + str(search_data) + '"}}')
    t = dict()
    t['$test'] = {'$search' : search_data}
    print(t)
    calls = Call.objects(__raw__=t)
    print(calls)
    return json(calls.to_json())
