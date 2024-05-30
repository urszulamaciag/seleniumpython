import random
import string

from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.home_page import HomePage
from pages.admin_page import AdminPage
from pages.project_list_page import ProjectListPage
from pages.project_creation_page import ProjectCreatingPage


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def test_search_project(browser):
    my_project_name = generate_random_string(10)
    my_project_suffix = generate_random_string(5)

    home_page = HomePage(browser)
    home_page.open_admin_panel()

    admin_page = AdminPage(browser)
    admin_page.open_new_project_creating_page()

    project_creating_page = ProjectCreatingPage(browser)
    project_creating_page.add_project(my_project_name, my_project_suffix)
    project_creating_page.back_to_project_list()

    project_list_page = ProjectListPage(browser)
    project_list_page.search_project_on_project_list(my_project_name)
    # project_list_page.verify_project_added('my_project_name')
    assert project_list_page.is_project_in_list(my_project_name), f"Project '{my_project_name}' not found in the project list."

