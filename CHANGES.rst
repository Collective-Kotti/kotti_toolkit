History
=======

1.0.1
----------------
- Use endswith instead of regex search when querying for principals with a particular email domain name.
- Add a create-user bin script.

1.0.0
----------------

- Add the following users and groups functions found in `kotti_toolkit.security`:
    - search for groups by name using the `find_group` function
    - search for groups and users by email domain name with the `find_groups_by_email_domain` and `find_users_by_email_domain` functions.
    - Easily create groups and users with the `create_group` and `create_user` functions.
- Add a `csv` renderer for **CSV** or excel output, e.g::

    @view_config(name="export-users-status", permission="admin", renderer="csv")
    def export_users(self):
        req_status = self.request.params.get("status", "all")

- Create package with ``pcreate -s kotti kotti_toolkit``.
  [b4oshany]
