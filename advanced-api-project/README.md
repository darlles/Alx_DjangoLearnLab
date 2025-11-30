# Advanced API Project

## Book API Endpoints
- `GET /api/books/` → List all books (public)
- `GET /api/books/<id>/` → Retrieve a single book (public)
- `POST /api/books/create/` → Create a new book (authenticated users only)
- `PUT /api/books/<id>/update/` → Update a book (authenticated users only)
- `DELETE /api/books/<id>/delete/` → Delete a book (authenticated users only)

## Permissions
- Read-only endpoints are open to everyone.
- Write endpoints require authentication.
- Custom permissions can be added (e.g., only authors can edit their own books).

## Customizations
- `perform_create` and `perform_update` hooks allow injecting custom logic.
- Validation ensures `publication_year` is not in the future.

# Advanced Query Features for Book API

## Filtering
- `/api/books/?title=1984`
- `/api/books/?author__name=George Orwell`
- `/api/books/?publication_year=1949`

## Searching
- `/api/books/?search=Farm` → matches "Animal Farm"

## Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year` → descending order

# API Testing

## Running Tests
Execute:
```bash
python manage.py test api