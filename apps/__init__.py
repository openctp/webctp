import fastapi
from .td_app import app as _td_app
from .md_app import app as _md_app

td_app = fastapi.FastAPI()
td_app.mount("/td", _td_app)

md_app = fastapi.FastAPI()
md_app.mount("/md", _md_app)

dev_app = fastapi.FastAPI()
dev_app.mount("/td", _td_app)
dev_app.mount("/md", _md_app)
