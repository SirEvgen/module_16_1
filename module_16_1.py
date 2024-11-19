from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> str:
    return ("Главная страница")

@app.get("/user/admin") #/user/admin
async def admin() -> str:
    return ("Вы вошли как администратор")

@app.get("/id") # /id?user_id=123
async def id_paginator(user_id: int) -> str:
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user/{username}/{age}") # /user/alex/33
async def welcome_page(username: str, age: int) -> str:
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")

