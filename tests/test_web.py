import pytest
from flask import url_for

from web import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_app(client):
    response = client.get(url_for('api.index'))
    assert response.status_code == 200
    texto = 'hello flask'
    assert texto
    assert 'fail' not in texto
