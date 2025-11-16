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