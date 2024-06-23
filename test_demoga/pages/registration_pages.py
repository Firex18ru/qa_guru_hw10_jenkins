from pathlib import Path
from selene import browser, have
from data.user import User
import allure


class RegistrationPage:
    def __init__(self):
        self._state = browser.element("#state")
        self._city = browser.element("#city")

    def open(self):
        browser.open("/automation-practice-form")
        return self

    @allure.step("Заполняю форму /automation-practice-form")
    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def _choice_gender(self, gender):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def _fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def _fill_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
        return self

    def _choice_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    def _choice_hobbies(self, hobbies):
        browser.element("[for = hobbies-checkbox-1]").click()
        browser.element("[for = hobbies-checkbox-2]").click()
        return self

    def _upload_picture(self, file):
        browser.element("#uploadPicture").type(str(Path(__file__).parent.parent.joinpath(f"resources/", file)))
        return self

    def _fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def _choice_state(self, state):
        browser.element("#state").click().element("#react-select-3-option-0").click()
        return self

    def _choice_city(self, city):
        browser.element("#city").click().element("#react-select-4-option-0").click()
        return self

    def _submit(self):
        browser.element("#submit").click()
        return self

    def register(self, student: User):
        (
            self._fill_first_name(student.name)
            ._fill_last_name(student.surname)
            ._fill_email(student.email)
            ._choice_gender(student.gender)
            ._fill_phone_number(student.phone)
            ._fill_birthday(student.date_year, student.date_month, student.date_day)
            ._choice_subjects(student.subject)
            ._choice_hobbies(student.hobby)
            ._upload_picture(student.photo)
            ._fill_address(student.address)
            ._choice_state(student.state)
            ._choice_city(student.city)
            ._submit()
        )
        return self

    def should_registered_user(self, student: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f'{student.name} {student.surname}',
                student.email,
                student.gender,
                student.phone,
                f'{student.date_day} {student.date_month},{student.date_year}',
                student.subject,
                student.hobby,
                student.photo,
                student.address,
                f'{student.state} {student.city}'
            )
        )
        return self
