from flask import Flask, request
import random
import string
import threading
from time import sleep


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Strict',
)


class Website:
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
        self.access_code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        threading.Thread(target=self.generate_access_code).start()
        self.register_routes()

    def generate_access_code(self):
        while True:
            for cell in range(0, len(self.access_code)):
                self.access_code[cell] = ""
                for _ in range(0, 20):
                    self.access_code[cell] += random.choice(
                        string.ascii_letters + "1234567890")
            sleep(4)

    def register_routes(self):
        @self.app.route('/', methods=['POST', 'GET'])
        def index():
            if request.method == 'POST':
                return 'Incorrect method!'
            return 'Concatenate all the codes to get the final access code. Find the codes in /1, /2, /3 ... /9, /10. Submit the final access code to /flag with parameter "flag". You have to be quick though! The codes change every four seconds.'


        @self.app.route('/<string:num>', methods=['POST', 'GET'])
        def num(num):
            if request.method == 'POST':
                return 'Incorrect method!'
            try:
                num = int(num) - 1
            except:
                return 'Not a number!'

            if 0 <= num and num <= 9:
                return self.access_code[num]
            return 'Nothing here!'


        @self.app.route('/flag', methods=['POST', 'GET'])
        def flag():
            if request.method == 'GET':
                return 'Incorrect method!'

            if not request.args.__contains__('flag'):
                return 'flag parameter not in arguments'

            flag_sum = ""
            for cell in self.access_code:
                flag_sum += cell

            if request.args.get('flag') == flag_sum:
                return "ODUCTF{27de9783395536a64b89ae29fcb695da}"

            return "Incorrect value"
        
http = Website().app