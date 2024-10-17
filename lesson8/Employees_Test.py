import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")


def test_add_new_employee():
    # Создать новую компанию
    name = "Book Ra"
    descr = "magazin books"
    result = api.create_company(name, descr)
    new_id = result["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотруднико до...
    body = api.get_employees_list(companyId)
    len_before = len(body)
    # добавить нового сотрудника
    firstName = "petr"
    lastName = "volodin"
    middleName = "romanovich"
    company = companyId
    email = "petsane@ya.ru"
    url = "string"
    phone = "89889544323"
    birthdate = "1986-07-24T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(
        firstName,
        lastName,
        middleName,
        companyId,
        email,
        url,
        phone,
        birthdate,
        isActive,
    )
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "petr"
    assert body[-1]["lastName"] == "volodin"
    assert body[-1]["middleName"] == "romanovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89889544323"
    assert body[-1]["birthdate"] == "1986-07-24"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id


def test_get_employees_id():
    # Создать новую компанию
    name = "Грузовичек"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    # Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании до....
    body = api.get_employees_list(companyId)
    begin_list = len(body)
    # добавить нового сотрудника
    firstName = "petr"
    lastName = "volodin"
    middleName = "romanovich"
    company = companyId
    email = "petsane@ya.ru"
    url = "string"
    phone = "89889544323"
    birthdate = "1986-07-24T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(
        firstName,
        lastName,
        middleName,
        companyId,
        email,
        url,
        phone,
        birthdate,
        isActive,
    )
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "petr"
    assert body[-1]["lastName"] == "volodin"
    assert body[-1]["middleName"] == "romanovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89889544323"
    assert body[-1]["birthdate"] == "1986-07-24"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id


def test_patch_employee():
    # Создать новую компанию
    name = "ПЭК"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "mariya"
    lastName = "volodina"
    middleName = "igorevna"
    company = companyId
    email = "volodina123@mail.ru"
    url = "string"
    phone = "89612856596"
    birthdate = "1993-01-20"
    isActive = True
    new_employee = api.create_employee(
        firstName,
        lastName,
        middleName,
        companyId,
        email,
        url,
        phone,
        birthdate,
        isActive,
    )
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Погосян"
    new_email = "pogosyan123@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(
        employee_id, new_lastName, new_email, new_url, new_phone, new_isActive
    )
    assert edited["email"] == "pogosyan23@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False


def test_delete_employee():
    # Создать новую компанию
    name = "Бетономешалка"
    descr = "строительство"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Сергей"
    lastName = "Кононенко"
    middleName = "Игоревич"
    company = companyId
    email = "kononenko123@mail.ru"
    url = "string"
    phone = "89996665577"
    birthdate = "1985-05-06"
    isActive = True
    new_employee = api.create_employee(
        firstName,
        lastName,
        middleName,
        companyId,
        email,
        url,
        phone,
        birthdate,
        isActive,
    )
    emp_id = new_employee["id"]
    # удалить сотрудника
    del_emp = api.delete_employee(emp_id)

    # Проверить, что сотрудник был удален
    assert del_emp is not None, "Сотрудник не был удален"
