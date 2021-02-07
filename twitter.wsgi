
from app import create_app

activate_this = '/home/ubuntu/Missing-Relations/venv/bin/activate'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

application = create_app()
