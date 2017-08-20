import os

from sanic import Sanic
import mongoengine

from sanic_cors import CORS
from routes.health_check import health_check
from routes.call import create_call, search

app = Sanic()
CORS(app)
app.add_route(create_call, '/call', methods=['POST'])
app.add_route(search, '/search', methods=['POST'])
app.add_route(health_check, '/health-check')
mongoengine.connect('blah', host=os.getenv('MONGO_URL'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))