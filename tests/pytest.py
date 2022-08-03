from page.models import *
import pytest


@pytest.mark.django_db
def test_groupname_creatr():
    group = GroupName.objects.create(name='nurbek')
    assert group.name == 'nurbek'
    # GroupName.objects.create_user('john')
    # assert GroupName.objects.count() == 1


def test_ex():
    assert 1 == 1
