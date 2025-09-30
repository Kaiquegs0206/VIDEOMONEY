import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from app.asgi import app

# Vercel serverless function
def handler(request):
    return app(request.scope, request.receive, request.send)
