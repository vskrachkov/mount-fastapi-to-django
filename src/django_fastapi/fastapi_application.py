from fastapi import FastAPI

application = FastAPI()


@application.get('/')
def index():
    return 'hello'
