USERS = {'ehaque': 'haque123', 'ehsan': 'ehsan123'}
GROUPS = {'ehaque': ['group_1'], 'ehsan': ['group_2']}


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
