# this is a test project
i hope to improve in the future so watchout

## Permissions and Groups Setup

This app uses Django's built-in permissions and groups to control access:

### Custom Permissions (defined in Article model):
- `can_view`: View articles
- `can_create`: Create articles
- `can_edit`: Edit articles
- `can_delete`: Delete articles

### Groups:
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_create`, `can_edit`
- **Admins**: Assigned all permissions

### Enforcement:
Views are protected using `@permission_required` decorators.

## Security Measures Implemented

- `DEBUG = False`: Prevents sensitive error info from being exposed.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Enforces HTTPS-only cookies.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`: Adds browser-level protections.
- `django-csp`: Enforces a strict Content Security Policy to mitigate XSS.
- All forms include `{% csrf_token %}`.
- Views use Django ORM and forms to prevent SQL injection and validate input.