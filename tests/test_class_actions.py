import pytest

# @pytest.mark.usefixtures("test_list_vacancies")
# def test_read_vacancies(test_JSONWorker, test_list_vacancies):
#     assert type(test_JSONWorker.read_vacancies()) == list

@pytest.mark.usefixtures("test_list_vacancies")
def test_delete_vacancies(test_JSONWorker):
    assert test_JSONWorker.delete_vacancies() == None

