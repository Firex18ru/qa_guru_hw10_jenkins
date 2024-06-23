from data.user import User
from test_demoga.pages.registration_pages import RegistrationPage


def test_form_to_registrate():
    page = RegistrationPage()
    user = User(
        name="Ivan",
        surname="Yakimenko",
        email="Def11@def.ru",
        gender="Male",
        phone="0999777601",
        date_year="1989",
        date_month="February",
        date_day="11",
        subject="Computer Science",
        hobby="Sports, Reading",
        photo="094745.png",
        address="Izhevsk",
        state="NCR",
        city="Delhi"
    )
    page.open().register(user).should_registered_user(user)
