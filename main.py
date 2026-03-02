from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel # 추가! JSON 데이터를 깔끔하게 받아줄 틀이야.

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 프론트엔드에서 날아올 JSON 데이터의 구조(뼈대)를 파이썬 클래스로 정의해!
class ScoreData(BaseModel):
    player_name: str
    chicken_count: int

@app.get("/")
async def show_game_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 폼 데이터(Form)를 받던 코드에서 JSON(ScoreData)을 받는 코드로 변경!
@app.post("/submit-score")
async def submit_score(data: ScoreData): 
    # data.player_name, data.chicken_count 로 아주 편하게 꺼내 쓸 수 있어.
    
    # 여기서 DB 저장 작업이 일어나겠지?
    message = f"[{data.player_name}]님이 무려 {data.chicken_count}점을 달성했습니다! (AJAX 통신 성공!)"
    
    # 템플릿(HTML)을 리턴하는 게 아니라, 그냥 파이썬 딕셔너리를 리턴하면
    # FastAPI가 알아서 예쁜 JSON으로 변환해서 프론트엔드(fetch)로 보내줘!
    return {"status": "success", "result_message": message}