import json


async def app(scope, receive, send):
    if scope["type"] != "http":
        return

    path = scope["path"]
    method = scope["method"]

    if method == "GET" and path == "/":
        data = {
            "message": "Welcome to Raw ASGI App",
            "framework": "No framework used",
            "week": "Week 07"
        }
        status = 200

    elif method == "GET" and path == "/about":
        data = {
            "topic": "Python Web Fundamentals",
            "server": "Uvicorn",
            "protocol": "ASGI"
        }
        status = 200

    elif method == "GET" and path == "/health":
        data = {
            "status": "healthy",
            "server": "running"
        }
        status = 200

    else:
        data = {
            "error": "Route not found"
        }
        status = 404

    body = json.dumps(data).encode("utf-8")

    await send({
        "type": "http.response.start",
        "status": status,
        "headers": [
            (b"content-type", b"application/json")
        ]
    })

    await send({
        "type": "http.response.body",
        "body": body
    })