import os

from sanic import Sanic
import mongoengine

from routes.health_check import health_check
from routes.call import create_call, search
from routes.twilio import rec_message

app = Sanic()
app.add_route(create_call, '/call', methods=['POST'])
app.add_route(search, '/search', methods=['POST'])
app.add_route(health_check, '/health-check')
app.add_route(rec_message, '/twilio', methods=['POST'])
mongoengine.connect('blah', host=os.getenv('MONGODB_URI'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))