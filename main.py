from datetime import date


class User:
    # Assign values for name and date of birth

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    # Return an Integer representing the user's current age

    def age(self):
        today = date.today()
        dob = self.date_of_birth
        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day))
        return age

    # Return a Date object for the user's current upcoming birthday

    def next_birthday(self):
        today = date.today()
        birthday_this_year = self.date_of_birth.replace(year=today.year)
        if today < birthday_this_year:
            next_birthday = birthday_this_year
        else:
            next_birthday = birthday_this_year.replace(year=today.year + 1)
        return next_birthday
