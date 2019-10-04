from typing import Any, Dict


class _UserTaskLists:
    def find_by_user(self,
                     user: str,
                     params: Dict[str, Any] = {},
                     **options) -> Dict: ...
    def tasks(self,
              user_task_list: str,
              params: Dict[str, Any] = {},
              **options) -> Dict: ...
