from flask import Flask, request


class Main():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.jinja_env.trim_blocks = True
        self.app.jinja_env.lstrip_blocks = True
        self.app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
        self.app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
        self.app.config["SESSION_PERMANENT"] = False
        self.app.config["SESSION_TYPE"] = "filesystem"
        self.app.config.update(
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_HTTPONLY=True,
            SESSION_COOKIE_SAMESITE="Strict",
        )
        self.register_routes()

    def register_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def index():
            if "SuperSecretArgument" not in request.args:
                return "SuperSecretArgument not found"
            if request.args.get("SuperSecretArgument") != "SuperAmazing@rgumentV@lu3":
                return "SuperSecretArgument is not SuperAmazing@rgumentV@lu3"
            if request.user_agent.string != "L33tBrow$er":
                return "Please use the L33tBrow$er"
            if "L33tBrowser" not in request.headers:
                return "Using fake L33tBrow$ser! L33tBrowser not in headers"
            if "admin" not in request.cookies and not request.cookies.get("admin"):
                return "You are not an admin"
            if request.headers.get("L33tBrowser") != "ODU_CTF{6e6f742074686520666c6167}":
                return "Using fake L33tBrow$ser! L33tBrowser header is not ODU_CTF{6e6f742074686520666c6167}"
            return "ODUCTF{s1ckBr0wserBR0}"


http = Main().app
