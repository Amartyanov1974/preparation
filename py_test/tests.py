from django.contrib.auth.models import User
import pytest

from simple_db.models import Thing


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user(username='user2', email='user2@mail.com')
    User.objects.create_user(username='user', email='user@mail.com')
    assert User.objects.all().first().username == 'user2'
    assert User.objects.count() == 2


@pytest.mark.django_db
def test_thing_create():
    Thing.objects.create(name='One_Thing', amount=3)
    Thing.objects.create(name='Two_Thing', amount=2)

    assert Thing.objects.count() == 2
    assert Thing.objects.get(name='One_Thing').amount == 3


@pytest.mark.django_db
def test2_thing_create():
    with pytest.raises(TypeError):
        Thing.objects.create(name='One_Thing', amounts=3)


@pytest.mark.django_db
def test3_thing_create():
    with pytest.raises(TypeError) as excinfo:
        Thing.objects.create(name='One_Thing', amounts=3)
        assert "amounts" in str(excinfo.value)


@pytest.mark.parametrize('numer, result', [(1, 1), (2, 4), (3, 9)])
def test_quad(numer, result):
    assert numer*numer == result
