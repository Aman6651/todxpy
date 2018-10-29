status_aliases_dict = {
    'v': '✓',
    'x': '✗'
}

def status_aliases(status):
    if status in status_aliases_dict:
        return status_aliases_dict[status]
    else:
        return status
