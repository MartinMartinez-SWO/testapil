from flask import Blueprint


from cron.controller import  get_all_api_users

cron_blueprint = Blueprint(
    'cron',
    __name__
)


@cron_blueprint.route('/all-users')
def get_all_api_users_routes():
    """
    Method to sync all employees from Personio to JumpCloud/Workspace
    return:
    """
    return get_all_api_users()


