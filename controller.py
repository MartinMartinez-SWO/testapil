from http import HTTPStatus
from json_placeholder import JsonPlaceholder
from test_api_lh import TestApil


json_placeholder = JsonPlaceholder()
test_apil = TestApil()

def get_all_api_users():

    """
    Get all the employees both from JsonPlaceholder and TestApil and return them into a list
    """
    employees = dict()
    json_placeholder_employees = json_placeholder.list_all()
    # test_apil_employees = test_apil.list_all_users()

    for employee in json_placeholder_employees:
        employee_id = employee['id']
        employees[employee_id] = employee

    # for employee in test_apil_employees:
    #     employee_id = employee['id']
    #     employees[employee_id] = employee
    
    return HTTPStatus.OK