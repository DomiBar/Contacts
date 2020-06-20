from faker import Fake

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
        self.job=job
        self.company=company
        self.work_phone=work_phone