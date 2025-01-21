def check_access(request_user, username=None):
    """
    Small helper function to check that the current (possibly unauthenticated)
    user can access a URL that the owner user shared the link.

    Raises Http404 in case of error (no read-only access allowed)

    :param request_user: the user in the current request
    :param username: the username
    :return: a tuple: (is_owner, user)
    """

    if username:
        user = get_object_or_404(User, username=username)
        if request_user.username == username:
            user = request_user
        elif not user.userprofile.ro_access:
            raise Http404('You are not allowed to access this page.')

    # If there is no user_pk, just show the user his own data
    else:
        if not request_user.is_authenticated:
            raise Http404('You are not allowed to access this page.')
        user = request_user

    is_owner = request_user == user
    return is_owner, user
