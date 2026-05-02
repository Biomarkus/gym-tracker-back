from factory import Base, engine
from src.api.app import create_app

app = create_app()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run(host="0.0.0.0", port=8080, debug=True)