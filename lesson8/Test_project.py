import pytest
from YouGile import Yougile


base_url = "https://ru.yougile.com"


@pytest.mark.positive_test
def test_add_project():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    response = yougile.create_project("Yogatime", project_data)

    assert "content" in response, "Expected 'content' in the response"
    assert (
        len(response["content"]) > 0
    ), "Expected content to have at least one project"
    project_id = response["content"][0]["id"]
    assert project_id is not None, "Expected project ID to be present"


@pytest.mark.positive_test
def test_get_list_of_projects():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )
    projects = yougile.get_list_of_projects()

    assert len(projects) > 0, "Projects list should not be empty"


@pytest.mark.positive_test
def test_update_project():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )

    project_name = "Test Project"
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    create_response = yougile.create_project(project_name, project_data)

    assert (
        "content" in create_response
    ), "Expected 'content' in the create response"
    assert (
        len(create_response["content"]) > 0
    ), "Expected content to have at least one project"

    project_id = create_response["content"][0].get("id")
    assert project_id is not None, "Expected project ID in the create response"

    new_title = "Updated Test Project"
    update_response = yougile.update_project(project_id, new_title)

    assert "id" in update_response, "Expected project ID in the update response"
    assert (
        update_response.get("id") == project_id
    ), "Expected project ID to match"


@pytest.mark.positive_test
def test_get_project_by_id():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )
    project_name = "Test Project"
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    create_response = yougile.create_project(project_name, project_data)
    print("Create response:", create_response)

    assert (
        "content" in create_response
    ), "Expected 'content' in the create response"
    assert (
        len(create_response["content"]) > 0
    ), "Expected content to have at least one project"
    project = create_response["content"][0]
    assert "id" in project, "Expected project ID in the create response"
    assert "title" in project, "Expected project title in the create response"
    project_id = project["id"]
    assert (
        project_id is not None
    ), "Expected project ID to be found in the create response"
    project_details = yougile.get_project_by_id(project_id)
    assert (
        "id" in project_details
    ), "Expected project ID in the project details response"
    assert (
        "title" in project_details
    ), "Expected project title in the project details response"
    assert (
        project_details["id"] == project_id
    ), "Project ID in details does not match the created project ID"


@pytest.mark.negative_test
@pytest.mark.xfail(reason="Expected ValueError when project name is missing.")
def test_add_project_missing_name():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )

    invalid_project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}

    with pytest.raises(ValueError, match="Project name is required."):
        yougile.create_project("", invalid_project_data)
        # Пустое имя проекта


@pytest.mark.negative_test
@pytest.mark.xfail(reason="Expected ValueError when users data is missing.")
def test_add_project_missing_users():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )

    with pytest.raises(
        ValueError,
        match="Invalid user data format. Expected a dictionary with string values.",
    ):
        yougile.create_project("Test Project", None)
        # Отсутствие данных пользователей


@pytest.mark.negative_test
@pytest.mark.xfail(
    reason="Expected ValueError when users data format is invalid."
)
def test_add_project_invalid_users_format():
    yougile = Yougile(
        "Petsane@ya.ru",
        "Technobase1986",
        "402a6faf-b338-47a6-930c-ff074d90f515",
    )

    invalid_project_data = ["invalid_user_id"]
    # Неверный формат данных пользователей

    with pytest.raises(
        ValueError,
        match="Invalid user data format. Expected a dictionary with string values.",
    ):
        yougile.create_project("Test Project", invalid_project_data)
        # Неверный формат данных пользователей
