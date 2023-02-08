from fastapi_login import LoginManager

SECRET_KEY = "7136c046c7752a8455eaeb38a9c6bc5aef26055863b50897cdd8faae170baa89"
login_manager = LoginManager(SECRET_KEY, token_url="/user/login", use_cookie=True, use_header=False)