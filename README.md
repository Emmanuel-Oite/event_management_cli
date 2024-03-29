# Event Management CLI

## Introduction

This is a simple CLI application for managing events and attendees.

## Features

- Add, remove, and edit events
- Add and remove attendees for an event
- List all events and attendees

## Setup

1. Create a virtual environment: `pipenv install`.
2. Activate the virtual environment: `pipenv shell`.
3. Install dependencies: `pipenv install`.
4. Run migrations: `alembic upgrade head`.

## Usage

1. To view all available commands: `python -m app.cli --help`
   <img src="./Presentation/--help.png" alt="Show all Commands" />

2. Add an event: -`python -m app.cli add-event "Birthday Party" --date "2024-03-15" --location "Party Venue"`
   <img src="./Presentation/add-event.png" alt="Adding An Event" />

   - Specify the event name, date, and location when adding an event.

3. List events: -`python -m app.cli list-events`
   <img src="./Presentation/list-event.png" alt="List all events" />

   - View a list of all events.

4. Edit an event: -`python -m app.cli edit-event "Original Event Name" --new_name "Updated Event Name" --new_date "2024-04-01" --new_location "New Location"`
   <img src="./Presentation/edit-event.png" alt="Edit an event" />

   - Edit the details of a registered event

5. Remove an event: -`python -m app.cli remove-event "EVENT NAME"`
   <img src="./Presentation/remove-event.png" alt="Remove an event" />

   - Provide the name of the event to remove it.

6. Add an attendee: -`python -m app.cli add-attendee "EVENT_NAME" "ATTENDEE NAME"`
   <img src="./Presentation/add-attendee.png" alt="add an attendee" />

   - Add an attendee to a specific event by providing both event and attendee names.

7. List attendees for an event: -`python -m app.cli list-attendees "EVENT NAME"`
   <img src="./Presentation/list-attendees.png" alt="list attendees" />

   - View the list of attendees for a specific event.

8. Remove an attendee: -`python -m app.cli remove-attendee "EVENT NAME" "ATTENDEE NAME"`
   <img src="./Presentation/remove attendee.png" alt="Remove an attendee" />
   - Remove a specific attendee from an event by providing event and attendee names.

## Testing

Run tests using `pytest`.

## External Libraries

- Click for CLI interface.
- SQLAlchemy for database interaction.
- Alembic for database migrations.
- Pytest for testing.
