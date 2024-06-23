from selene import browser, have
import os
import allure


@allure.title("Successful fill form")
def test_demoqa_form():
    with allure.step("Открываем регистрационную форму"):
        browser.open("https://demoqa.com/automation-practice-form")
    with allure.step("Заполняем регистрационную форму"):
        browser.element("#firstName").type("Ivan")
        browser.element("#lastName").type("Yakimenko")
        browser.element("#userEmail").type("Def11@def.ru")
        browser.element('[for="gender-radio-1"]').click()
        browser.element("#userNumber").type("0999777601")
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(
            "[value = '0']"
        ).click()
        browser.element(".react-datepicker__year-select").click().element(
            "[value = '1989']"
        ).click()
        browser.all(".react-datepicker__day--001").second.click()
        browser.element("#subjectsInput").type("Computer Science").press_enter()
        browser.element("[for = hobbies-checkbox-1]").click()
        browser.element("[for = hobbies-checkbox-2]").click()
        browser.element("#uploadPicture").send_keys(os.path.abspath("picture/094745.png"))
        browser.element("#currentAddress").type("Izhevsk")
        browser.element("#state").click().element("#react-select-3-option-0").click()
        browser.element("#city").click().element("#react-select-4-option-0").click()
        browser.element("#submit").press_enter()
    with allure.step("Проверяем форму"):
        browser.element(".modal-content").element("table").all("tr").all("td").even.should(
            have.exact_texts(
                "Ivan Yakimenko",
                "Def11@def.ru",
                "Male",
                "0999777601",
                "01 February,1989",
                "Computer Science",
                "Sports, Reading",
                "094745.png",
                "Izhevsk",
                "NCR Delhi",
            )
        )

    browser.element("#closeLargeModal").click()
