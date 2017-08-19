from sanic import Sanic
import os
from routes import health_check

app = Sanic()
app.add_route(health_check, '/health-check')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000))