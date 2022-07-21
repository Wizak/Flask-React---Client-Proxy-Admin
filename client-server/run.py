from app import create_app


if __name__ == '__main__':
    server_app = create_app()
    server_app.run()
