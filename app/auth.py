from fastapi import Request, HTTPException
async def require_api_key(request: Request):
    config = request.app.state.config
    api_key = request.headers.get("X-API-Key")
    if api_key != config.api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")