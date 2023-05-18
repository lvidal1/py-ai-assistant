from flask import Blueprint

home_router = Blueprint('home', __name__)

@home_router.route('/')
def hello():

  er = "Lol"
  return f"""Hi, my causa! {er}"""