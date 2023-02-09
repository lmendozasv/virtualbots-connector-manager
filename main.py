import os
from datetime import datetime
from flask import app, Flask
from ChatLogger import ChatLogger
from db.declarative_base import Base, engine, Session
session = Session()
app = Flask(__name__)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    dt = datetime.now()
    registro = ChatLogger(caller="SERVICE-STARTED", dt_created=dt)
    session.add(registro)
    session.commit()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
