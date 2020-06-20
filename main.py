from faker import Faker


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone} {self.email}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}: {self.phone}-{self.email}"

    def contact(self):
        print(
            f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.name} {self.surname}")


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, job, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.job = job
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        print(
            f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}")


def create_contacts(type, quantity):
    contacts = []
    fake = Faker("pl_PL")
    if type == 'basic':
        for i in range(quantity):
            person = BaseContact(
                fake.first_name(), fake.last_name(), fake.phone_number(),
                fake.email()
            )
            contacts.append(person)
    elif type == 'work':
        for i in range(quantity):
            person = BusinessContact(fake.first_name(), fake.last_name(), fake.phone_number(),
                                     fake.email(), fake.job(), fake.company(), fake.phone_number()
                                     )
            contacts.append(person)
    return contacts


my_contacts = create_contacts('work', 3)
