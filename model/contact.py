from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email1=None, email2=None,
                 email3=None, homepage=None, birthday=None, birthmonth=None, birthyear=None, annivday=None,
                 annivmonth=None, annivyear=None, sec_address=None, sec_home=None, sec_notes=None, id=None,
                 all_email_from_home_page=None, all_phones_from_home_page=None, group=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.annivday = annivday
        self.annivmonth = annivmonth
        self.annivyear = annivyear
        self.sec_address = sec_address
        self.sec_home = sec_home
        self.sec_notes = sec_notes
        self.all_email_from_home_page = all_email_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.group = group

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

