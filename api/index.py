from app.asgi import app

# Vercel serverless function
def handler(request):
    return app(request.scope, request.receive, request.send)
