from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_main_page() -> str:
    return ("Главная страница")

@app.get("/user/admin") #/user/admin
async def get_admin_page() -> str:
    return ("Вы вошли как администратор")

@app.get("/id") # /id?user_id=123
async def get_user_number(user_id: int) -> str:
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user") # /user?username=alex&age=33
async def get_user_info(username: str, age: int) -> str:
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")

