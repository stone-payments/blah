from sanic.response import json
from models.call import Call
import mongoengine

async def add_call(request):
    return_data = {"messages" : [], "success": False, "data": {}}
    call = Call()
    try:
        call.save()
        return_data['success'] = True
    except mongoengine.errors.ValidationError as e:
        for key in e.errors:
            return_data['messages'].append('{} - {}'.format(key, e.errors.get(key)))
       
    return json(return_data)