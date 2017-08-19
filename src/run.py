import os

from sanic import Sanic
from routes.health_check import health_check
from routes.call import add_call

app = Sanic()
app.add_route(add_call, '/call', methods=['POST'])
app.add_route(health_check, '/health-check')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))