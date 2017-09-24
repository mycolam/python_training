from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
from random import randrange

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    index = randrange(len(groups))
    group_id = groups[index].id
    contact = Contact(firstname="firstname", lastname="lastname", address="address", group=group_id)
    old_contacts = db.get_contacts_in_group(Group(id=group_id))
    app.contact.create(contact)
    new_contacts = db.get_contacts_in_group(Group(id=group_id))
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

