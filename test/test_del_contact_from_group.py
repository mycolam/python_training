from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    groups = db.get_group_list()
    index = random.randrange(len(groups))
    group_id = groups[index].id
    if len(db.get_contacts_in_group(Group(id=group_id))) == 0:
        app.contact.create(Contact(firstname="firstDEL", lastname="lastDEL", address="addressDEL", group=group_id))
    old_contacts = db.get_contacts_in_group(Group(id=group_id))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_in_group(Group(id=group_id))
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)