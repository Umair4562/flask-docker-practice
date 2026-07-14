from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Connect to Redis using the hostname defined in Docker Compose
redis_host = os.environ.get("REDIS_HOST", "redis")
cache = Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        hits = cache.incr('hits')
    except Exception as e:
        return f"Hello World! (Could not connect to Redis: {e})"
    return f"Hello World! I have been seen {hits} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)