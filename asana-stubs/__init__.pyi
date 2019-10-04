from . import resources

class Client:
    users = resources.users.Users()
    user_task_lists = resources.user_task_lists.UserTaskLists()

    @classmethod
    def access_token(Klass, accessToken: str) -> Client: ...
