from selene import browser, be, have
import os


def test_practice_form_create_user():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Vadim')
    browser.element('#lastName').type('Korolev')
    browser.element('#userEmail').type('v@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('79151411144')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>option:nth-child(12)').click()
    browser.element('.react-datepicker__year-select>[value = "1998"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').type('ph').press_enter()
    browser.element('#subjectsInput').type('b').press_enter()
    browser.element('//label[@for="hobbies-checkbox-1"]').click()
    browser.element('//label[@for="hobbies-checkbox-2"]').click()
    browser.element('//label[@for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("files/photo_man.png"))
    browser.element('#currentAddress').type('Test, 65')
    browser.element('#react-select-3-input').type("NC").press_enter()
    browser.element('#react-select-4-input').type("De").press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.present)
    browser.element('.table').all('td').even.should(have.exact_texts
                                                    ('Vadim Korolev', 'v@gmail.com', 'Other',
                                                     '79151411144', '27 December,1998', 'Physics, Biology',
                                                     'Sports', 'Reading', 'Music', 'photo_man.png', 'Test, 65', 'NCR Delhi'))
