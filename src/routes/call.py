from sanic.response import json
from models.call import Call
from services.call import add_call
import mongoengine

async def create_call(request):
    return_data = {"messages" : [], "success": False, "data": {}}
    if not request.json:
        return json(return_data, status=400)
    call_details = request.json
    
    data = add_call(call_details['file_uri'], call_details['metadata'])
    return_data['data'] = {
        'id': str(data.get('id')), 
        'analysis': [], 
        'file_hash': data.get('file_hash')
    }
    for analysis in data.get('analysis'):
         return_data['data']['analysis'].append({
            'id': str(analysis.get('id')), 
            'result': {
                'magnitude': analysis.get('result').get('magnitude'), 
                'score': analysis.get('result').get('score')
            }, 
            'provider': analysis.get('provider')
        })
    return_data['success'] = True
    return json(return_data)