from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from embedchain import App

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = FastAPI()

class YtbPromptRequest(BaseModel):
    youtube_link: str
    prompt: str

class YtbPromptResponse(BaseModel):
    response: str

@app.post("/query/", response_model=YtbPromptResponse)
async def query_youtube_prompt(request_body: YtbPromptRequest):
    ytb_prompt = App()
    try:
        ytb_prompt.add(request_body.youtube_link, data_type='youtube_video')
        response = ytb_prompt.query(request_body.prompt)
        return YtbPromptResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=int(os.environ.get("PORT", 8080)), reload=True)
