```markdown
# Tambola Ticket Generator

## Description

The Tambola Ticket Generator is a Django project designed to handle APIs for generating and managing Tambola (also known as Housie or Bingo) tickets. It provides endpoints for creating Tambola tickets based on sets and retrieving data from a PostgreSQL database.

## Features

- **Ticket Generation:** Use the POST API to generate Tambola tickets based on specified sets.
- **Data Retrieval:** Utilize the GET API to fetch data from the PostgreSQL database.

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL database settings in `settings.py`.

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```
## API Endpoints

### 1. Generate Tambola Tickets

- **URL:** `/api/generate-tickets/`
- **Method:** POST
- **Parameters:**
  - `sets`: List of sets for ticket generation.

### 2. Fetch Data

- **URL:** `/api/get_tickets_data/`
- **Method:** GET


## Contribution Guidelines

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.


## Contact

For any inquiries, please contact [sejalpitale@gmail.com](mailto:your-email@example.com).
