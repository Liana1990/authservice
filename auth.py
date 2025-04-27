import random
import new_python
from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException

users_auth_router = APIRouter(tags=["User Auth"])# nshanakum e app-i poxaren sa enq grelu
from schema import UserSignUpSchema, UserLogin,ChangePassword
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

@users_auth_router.get("/send-forgot-code/{email}") # ays api ov mardun moracac passwordi mail enq anum
def send_forgot_password_code(email:str):
    code=random.randint(1000,9999) #cuyc e talis, vor cragri emailov uxarkac cod@ ppatahakan e @ntrvum ev p                  etq e parunaki 4 nish
    main.cursor.execute ( """INSERT INTO code (code, email) VALUES (%s,%s)
    """, (code, email))# minchev code userin uxarkel@ databasayum sarqum enq nor tale code anunov ev code pahum enq insert enq anum dra mej@
    main.conn.commit()# ete chanenq chi pahpanvi
    new_python.send_email(f"{email}",
               "your code",
               f"{code}") #kanchecinq new_python.py i meji f_n vor mail ani
# hima kuxarki cir koxmic atahakan code, vorovhetev import enq arel randem
@users_auth_router.post("/change-password")
def change_password(password_change_data:ChangePassword):
    password=password_change_data.new_password
    email=password_change_data.email
    hashed_password = pwd_context.hash(password)
    user_input_code = password_change_data.code  # you must add this field to your model!
    # 1. Get the correct code from database
    main.cursor.execute("""SELECT code FROM code WHERE email = %s ORDER BY id DESC LIMIT 1""", (email,))
    result = main.cursor.fetchone()

    if not result:
        raise HTTPException(status_code=400, detail="No verification code found for this email.")

    correct_code = str(result['code'])  # or result[0] depending on how your cursor returns

    # 2. Compare user's input code with correct code
    if user_input_code != correct_code:
        raise HTTPException(status_code=400, detail="Incorrect verification code.")

    # 3. If the code matches, update the password
    hashed_password = pwd_context.hash(password)
    main.cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed_password, email))
    main.conn.commit()

    return {"message": "Password updated successfully."}
    # main.cursor.execute("UPDATE users SET password =%s WHERE email =%s", (hashed_password, email))
    # main.conn.commit()
    # return "ok"

#web password dnel email-ic, todo gtnel sxal@,uxxel

#to do parol@ poxeluc petq e useri tvac code_@ lini nuyn cod@ inch menq enq iran tvel