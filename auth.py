from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException

users_auth_router = APIRouter(tags=["User Auth"])# nshanakum e app-i poxaren sa enq grelu
from schema import UserSignUpSchema, UserLogin
from security import pwd_context
import main
@users_auth_router.post("/api/sign-up")
def sign_up (user_signup_data: UserSignUpSchema):
    name = user_signup_data.name
    email = user_signup_data.email
    password = user_signup_data.password

    hashed_password = pwd_context.hash(password)

    main.cursor.execute("""INSERT INTO users (name, email, password) VALUES (%s, %s, %s)""",
                        (name, email, hashed_password))

    main.conn.commit()

    return "OK"

@users_auth_router.post("/api/login")
def login (logindata: UserLogin):
    email=logindata.email
    password=logindata.password
    main.cursor.execute("""select * From users where email=%s""", (email,))
    user=main.cursor.fetchone()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not pwd_context.verify(password,dict(user)["password"]):
        raise HTTPException (status_code=status.HTTP_403_FORBIDDEN)
    return "ok"
