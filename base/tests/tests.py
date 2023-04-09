import pytest
from django.urls import reverse
from django.test import TestCase

@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:index'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
