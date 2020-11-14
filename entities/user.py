class User:

    def __init__(self, email="yecenal453@rvemold.com", first_name="John", last_name="Doe",
                 company="Top Corp", mobile="555-555-5555"):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.company = company
        self.mobile = mobile
