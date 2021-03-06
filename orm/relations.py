def pluralize(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'



# TODO get url name instead of this heuristic shit
def get_name(relation):
    """
    supported relattions
        mailalias-list
        zone-refresh-serial
    """
    if relation.endswith('-list'):
        name = relation.replace('-list', '')
        name = pluralize(name)
    elif relation.endswith('-detail'):
        name = relation.replace('-detail', '')
    else:
        name = '-'.join(relation.split('-')[1:])
    name = name.replace('-', '_')
    return name
