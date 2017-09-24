import re


def test_all_contacts_on_home_page(app, db):
    contacts = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for contact_from_home_page in contacts:
        contact_from_db = get_contact_from_list_by_id(contacts_from_db, contact_from_home_page.id)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.sec_home]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))


def get_contact_from_list_by_id(contacts, id):
    for contact in contacts:
        if contact.id == id:
            return contact

