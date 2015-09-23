USERS = {'ehaque': 'ehaque123', 'imran': 'imran123', 'enam' : 'enam123', 'karim': 'karim123'}
GROUPS = {'ehaque': ['group_1'], 'karim': ['group_1'], 'imran': ['group_2'], 'enam':['group_2']}


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
