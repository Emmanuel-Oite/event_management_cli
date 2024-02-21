# Event Management CLI

## Introduction

This is a simple CLI application for managing events and attendees.

## Setup

1. Create a virtual environment: `pipenv install`.
2. Activate the virtual environment: `pipenv shell`.
3. Install dependencies: `pipenv install`.
4. Run migrations: `alembic upgrade head`.

## Usage

- Add an event: `# Event Management CLI

## Introduction

This is a simple CLI application for managing events and attendees.

## Setup

1. Create a virtual environment: `pipenv install`.
2. Activate the virtual environment: `pipenv shell`.
3. Install dependencies: `pipenv install`.
4. Run migrations: `alembic upgrade head`.

## Usage

- Add an event: `python app/cli.py add_event "EVENT_NAME" --date "2024-02-20" --location "Event Location"`

  - Specify the event name, date, and location when adding an event.

- Remove an event: `python app/cli.py remove_event "EVENT_NAME"`

  - Provide the name of the event to remove it.

- Add an attendee: `python app/cli.py add_attendee "EVENT_NAME" "ATTENDEE_NAME"`

  - Add an attendee to a specific event by providing both event and attendee names.

- Remove an attendee: `python app/cli.py remove_attendee "EVENT_NAME" "ATTENDEE_NAME"`

  - Remove a specific attendee from an event by providing event and attendee names.

- List events: `python app/cli.py list_events`

  - View a list of all events.

- List attendees for an event: `python app/cli.py list_attendees "EVENT_NAME"`
  - View the list of attendees for a specific event.

## Testing

Run tests using `pytest`.

## External Libraries

- Click for CLI interface.
- SQLAlchemy for database interaction.
- Alembic for database migrations.
- Pytest for testing.

## Why These Libraries?

Explain briefly why you chose these external libraries and how they contribute to the functionality and maintainability of your project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Usage

- To view all available commands: `python -m app.cli --help`

- ## Add an event: `python -m app.cli add-event "Birthday Party" --date "2024-03-15" --location "Party Venue"`

  - Specify the event name, date, and location when adding an event.

- ## Remove an event: `python -m app.cli remove-event "EVENT NAME"`

  - Provide the name of the event to remove it.

- ## Add an attendee: `python -m app.cli add-attendee "EVENT_NAME" "ATTENDEE NAME"`

  - Add an attendee to a specific event by providing both event and attendee names.

- ## Remove an attendee: `python -m app.cli remove-attendee "EVENT NAME" "ATTENDEE NAME"`

  - Remove a specific attendee from an event by providing event and attendee names.

- ## List events: `python -m app.cli list-events`

  - View a list of all events.

- ## List attendees for an event: `python -m app.cli list-attendees "EVENT NAME"`

  - View the list of attendees for a specific event.

- ## Edit and event : `python -m app.cli edit_event "Original Event Name" --new_name "Updated Event Name" --new_date "2024-04-01" --new_location "New Location"`
  - Edit the details of a registered event

## Testing

Run tests using `pytest`.

## External Libraries

- Click for CLI interface.
- SQLAlchemy for database interaction.
- Alembic for database migrations.
- Pytest for testing.

## Why These Libraries?

Explain briefly why you chose these external libraries and how they contribute to the functionality and maintainability of your project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
