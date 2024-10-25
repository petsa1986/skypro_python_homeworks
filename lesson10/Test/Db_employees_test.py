import allure
import random
from faker import Faker
from EmployeesApi import EmployeesApi
from EmployeesTable import EmployeesTable

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesTable(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
)
fake = Faker("ru_RU")


@allure.step("Метод для генерации названия организации")
def generate_company():
    name = fake.name()
    description = fake.text(max_nb_chars=20)
    return name, description


@allure.step("Метод для генерации названий сотрудника")
def generate_employee(companyId: int):
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name() + "овна"
    phone = fake.random_number(digits=11, fix_len=True)
    email = fake.email(domain="example.com")
    birthdate = '1976-07-02'
    url = fake.url(schemes=['http', 'https'])
    isActive = random.choice([True, False])
    return (
        firstName,
        lastName,
        middleName,
        phone,
        email,
        birthdate,
        url,
        isActive,
    )


@allure.step("Метод для генерации  редактирования названий сотрудника")
def generate_edit_employee(companyId: int):
    new_lastName = fake.last_name()
    new_email = fake.email(domain="example.com")
    new_url = fake.url(schemes=['http', 'https'])
    new_phone = fake.random_number(digits=11, fix_len=True)
    new_isActive = random.choice([True, False])
    return new_lastName, new_email, new_url, new_phone, new_isActive


@allure.id("SkyPro-1")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Получение списка сотрудников")
@allure.feature("READ")
@allure.title("Получение полного списка сотрудников")
@allure.suite("Тесты на работу с сотрудниками")
def test_get_list_employee():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)
    api_list = api.get_employees_list(max_id)

    db_list = db.get_emploees_db(max_id)

    with allure.step("Проверить, что список сотрудников в API и db одинаковый"):
        assert len(api_list) == len(db_list)


@allure.id("SkyPro-2")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Добавление нового сотрудника")
@allure.feature("CREATE")
@allure.title("Создание нового сотрудника")
@allure.suite("Тесты на работу с сотрудниками")
def test_add_new_employee():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить нового сотрудника"):
        (
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            isActive,
        ) = generate_employee(max_id)
        db.create_employee_db(
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            max_id,
            isActive,
        )

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    with allure.step("Проверить разницу"):
        with allure.step(
            "Проверить, что список API = db до создания сотрудника"
        ):
            assert len(api_list_before) == len(db_list_before)
        with allure.step(
            "Проверить, что список API = db после создания сотрудника"
        ):
            assert len(api_list_after) == len(db_list_after)
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в API на 1"
        ):
            assert len(api_list_after) - len(api_list_before) == 1
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в db на 1"
        ):
            assert len(db_list_after) - len(db_list_before) == 1

    with allure.step(
        "Проверить,что поля нового сотрудника. Корректно заполнены"
    ):
        assert api_list_after[-1]['firstName'] == firstName
        assert api_list_after[-1]['lastName'] == lastName
        assert api_list_after[-1]['middleName'] == middleName
        # assert api_list_after[-1]['phone'] == phone
        assert api_list_after[-1]['email'] == email
        assert api_list_after[-1]['birthdate'] == birthdate
        assert api_list_after[-1]['avatar_url'] == url
        assert api_list_after[-1]['isActive'] == isActive
        assert api_list_after[-1]['id'] == max_id_empl

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)


@allure.id("SkyPro-3")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Получение сотрудника по id")
@allure.feature("READ")
@allure.title("Получить сотрудника по id")
@allure.suite("Тесты на работу с сотрудниками")
def test_get_one_employee():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить нового сотрудника"):
        (
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            isActive,
        ) = generate_employee(max_id)
        db.create_employee_db(
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            max_id,
            isActive,
        )

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    new_employee = api.get_employee(max_id_empl)

    with allure.step("Проверить разницу"):
        with allure.step(
            "Проверить, что список API = db до создания сотрудника"
        ):
            assert len(api_list_before) == len(db_list_before)
        with allure.step(
            "Проверить, что список API = db после создания сотрудника"
        ):
            assert len(api_list_after) == len(db_list_after)
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в API на 1"
        ):
            assert len(api_list_after) - len(api_list_before) == 1
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в db на 1"
        ):
            assert len(db_list_after) - len(db_list_before) == 1

    with allure.step(
        "Проверить,что поля нового сотрудника. Корректно заполнены"
    ):
        assert new_employee["firstName"] == firstName
        assert new_employee["lastName"] == lastName
        assert new_employee["middleName"] == middleName
        assert new_employee["companyId"] == max_id
        # assert new_employee["phone"] ==  phone
        assert new_employee['avatar_url'] == url
        assert new_employee["birthdate"] == birthdate
        assert new_employee["isActive"] == False
        assert new_employee["id"] == max_id_empl

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)


@allure.id("SkyPro-4")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Редактирование данных сотрудника")
@allure.feature("UPDATE")
@allure.title("Редактирование данных сотрудника")
@allure.suite("Тесты на работу с сотрудниками")
def test_patch_employee():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить нового сотрудника"):
        (
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            isActive,
        ) = generate_employee(max_id)
        db.create_employee_db(
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            max_id,
            isActive,
        )

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    with allure.step("Редактировать данные сотрудника"):
        new_lastName, new_email, new_url, new_phone, new_isActive = (
            generate_edit_employee(max_id)
        )
        edited = api.edit_employee(
            new_lastName,
            new_email,
            new_url,
            new_phone,
            new_isActive,
            max_id_empl,
        )

    with allure.step("Проверить разницу"):
        with allure.step(
            "Проверить, что список API = db до создания сотрудника"
        ):
            assert len(api_list_before) == len(db_list_before)
        with allure.step(
            "Проверить, что список API = db после создания сотрудника"
        ):
            assert len(api_list_after) == len(db_list_after)
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в API на 1"
        ):
            assert len(api_list_after) - len(api_list_before) == 1
        with allure.step(
            "Проверить, что список ДО меньше списка ПОСЛЕ в db на 1"
        ):
            assert len(db_list_after) - len(db_list_before) == 1

    with allure.step(
        "Проверить,что поля сотрудника изменены. Корректно заполнены"
    ):
        assert edited["url"] == new_url
        assert edited["isActive"] == new_isActive
        assert edited["email"] == new_email
        # assert edited["phone"] == new_phone
        # assert edited["lastName"] == new_lastName

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)


@allure.id("SkyPro-5")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Удаление сотрудника")
@allure.feature("DELETE")
@allure.title("Удалить сотрудника по id")
@allure.suite("Тесты на работу с сотрудниками")
def test_delete_employee():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить нового сотрудника"):
        (
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            isActive,
        ) = generate_employee(max_id)
        db.create_employee_db(
            firstName,
            lastName,
            middleName,
            phone,
            email,
            birthdate,
            url,
            max_id,
            isActive,
        )

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    db.delete_employee_db(max_id_empl)

    db.delete(max_id)

    with allure.step(
        "Проверить, что сотрудник в организации с максимальным id удален"
    ):
        assert not db.get_emploees_db(max_id)


@allure.id("SkyPro-6")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Добавление и удаление несколько сотрудников")
@allure.feature("ADD, DELETE")
@allure.title("Добавить и удалить сразу нескольких сотрудников")
@allure.suite("Тесты на работу с сотрудниками")
def test_add_del_several_empl():
    with allure.step("Cоздать новую организацию"):
        name, description = generate_company()
        db.create_company_db(name, description)

    max_id = db.get_max_id_company(id)

    new_company = api.get_company(max_id)

    api_list_before = api.get_employees_list(max_id)
    db_list_before = db.get_emploees_db(max_id)

    with allure.step("Добавить несколько сотрудников в организацию"):
        with allure.step("Вызвать цикл для добавления сотрудников"):
            for i in range(10):
                (
                    firstName,
                    lastName,
                    middleName,
                    phone,
                    email,
                    birthdate,
                    url,
                    isActive,
                ) = generate_employee(max_id)
                db.create_employee_db(
                    firstName,
                    lastName,
                    middleName,
                    phone,
                    email,
                    birthdate,
                    url,
                    max_id,
                    isActive,
                )

    max_id_empl = db.get_max_id_employee(id)

    api_list_after = api.get_employees_list(max_id)
    db_list_after = db.get_emploees_db(max_id)

    with allure.step("Удалить несколько сотрудников"):
        with allure.step("Вызвать цикл для удаления всех сотрудников"):
            for i in range(10):
                db.delete_employee_db(max_id_empl - i)

    db.delete(max_id)

    with allure.step(
        "Проверить, что список ДО меньше списка ПОСЛЕ в API на 10"
    ):
        assert len(api_list_after) - len(api_list_before) == 10

    with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ в db на 10"):
        assert len(db_list_after) - len(db_list_before) == 10

    with allure.step(
        "Проверить, что сотрудник в организации с максимальным id удален"
    ):
        assert not db.get_emploees_db(max_id)
