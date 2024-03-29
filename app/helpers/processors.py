

def getvars(request):
    """
    Builds a GET variables string to be used in template links like pagination
    when persistence of the GET vars is needed.
    """
    variables = request.GET.copy()

    if 'page' in variables:
        del variables['page']

    if variables:
        return {'getvars': '&{0}'.format(variables.urlencode())}

    return ''