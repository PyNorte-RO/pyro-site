from web import create_app


if __name__ == '__main__':
    app = create_app()

    app.config.update(
        TESTING=True,
        SECRET_KEY=b'insira_uma_key_aqui',
        DEBUG=True
    )

    app.run(host='0.0.0.0', port=5000)
