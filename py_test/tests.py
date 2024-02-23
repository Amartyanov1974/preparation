from django.contrib.auth.models import User
import pytest

from django.core.exceptions import ObjectDoesNotExist
from simple_db.models import Thing


@pytest.mark.django_db
def test_create_user():
    User.objects.create_user(username='user2', email='user2@mail.com')
    User.objects.create_user(username='user', email='user@mail.com')
    assert User.objects.all().first().username == 'user2'
    assert User.objects.count() == 2


@pytest.mark.django_db
def test_create_thing():
    Thing.objects.create(name='One_Thing', amount=3)
    Thing.objects.create(name='Two_Thing', amount=2)

    assert Thing.objects.count() == 2
    assert Thing.objects.get(name='One_Thing').amount == 3


@pytest.mark.django_db
def test_get_thing():
    # Раскоменторовать, чтобы вызвать ошибку
    # thing = Thing.objects.create(name='One_Thing', amount=3)
    with pytest.raises(ObjectDoesNotExist):
        thing = Thing.objects.get(name='One_Thing')


@pytest.mark.parametrize('numer, result', [(1, 1), (2, 4), (3, 9)])
def test_quad(numer, result):
    assert numer*numer == result
