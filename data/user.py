import dataclasses


@dataclasses.dataclass
class User:
    name: str
    surname: str
    email: str
    gender: str
    phone: str
    date_year: str
    date_month: str
    date_day: str
    subject: str
    hobby: str
    photo: str
    address: str
    state: str
    city: str