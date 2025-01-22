from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randint
import uvicorn

app = FastAPI()

# Директория для шаблонов
templates = Jinja2Templates(directory="./")


@app.get("/", response_class=HTMLResponse)
def play_game(request: Request, guess: int = None):
    mystery_number = randint(1, 100)
    print(mystery_number)

    message = "Попробуйте угадать число от 1 до 100!"
    if guess is not None:
        if guess == mystery_number:
            message = f"🎉 Вы угадали! Загаданное число: {mystery_number}. Начинаем новую игру!"
            mystery_number = randint(1, 100)  # Сброс игры
        elif guess < mystery_number:
            message = "Число слишком маленькое. Попробуйте еще раз."
        else:
            message = "Число слишком большое. Попробуйте еще раз."

    return templates.TemplateResponse("index.html", {"request": request, "message": message})



def run_fastapi():
    port = 8000
    uvicorn.run(app, host="0.0.0.0", port=port)

run_fastapi()