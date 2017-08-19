import os

from sanic import Sanic
import mongoengine

from routes.health_check import health_check
from routes.call import create_call

app = Sanic()
app.add_route(create_call, '/call', methods=['POST'])
app.add_route(health_check, '/health-check')
mongoengine.connect('blah', host=os.getenv('MONGO_URL'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))