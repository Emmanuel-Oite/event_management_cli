import sys
from datetime import datetime
import click
from .models import Session, Event, Attendee

@click.group()
def cli():
    pass

@cli.command()
@click.argument('event_name')
@click.option('--date', help='Specify the date of the event')
@click.option('--location', help='Specify the location of the event')
def add_event(event_name, date, location):
    session = Session()
    event_date = datetime.strptime(date, "%Y-%m-%d").date() if date else None
    event = Event(name=event_name, date=event_date, location=location)
    session.add(event)
    session.commit()
    click.echo(f"Event '{event_name}' added successfully.")

@cli.command()
@click.argument('event_name')
def remove_event(event_name):
    session = Session()
    event = session.query(Event).filter_by(name=event_name).first()
    if event:
        session.delete(event)
        session.commit()
        click.echo(f"Event '{event_name}' removed successfully.")
    else:
        click.echo(f"Event '{event_name}' not found.")

@cli.command()
@click.argument('event_name')
@click.argument('attendee_name')
def add_attendee(event_name, attendee_name):
    session = Session()
    event = session.query(Event).filter_by(name=event_name).first()
    if event:
        attendee = Attendee(name=attendee_name, event=event)
        session.add(attendee)
        session.commit()
        click.echo(f"Attendee '{attendee_name}' added to event '{event_name}'.")
    else:
        click.echo(f"Event '{event_name}' not found.")

@cli.command()
@click.argument('event_name')
@click.argument('attendee_name')
def remove_attendee(event_name, attendee_name):
    session = Session()
    attendee = session.query(Attendee).join(Event).filter(Event.name == event_name, Attendee.name == attendee_name).first()
    if attendee:
        session.delete(attendee)
        session.commit()
        click.echo(f"Attendee '{attendee_name}' removed from event '{event_name}'.")
    else:
        click.echo(f"Attendee '{attendee_name}' not found in event '{event_name}'.")

@cli.command()
def list_events():
    session = Session()
    events = session.query(Event).all()
    for event in events:
        click.echo(f"Event: {event.name}")

@cli.command()
@click.argument('event_name')
def list_attendees(event_name):
    session = Session()
    event = session.query(Event).filter_by(name=event_name).first()
    if event:
        attendees = event.attendees
        for attendee in attendees:
            click.echo(f"Attendee: {attendee.name}")
    else:
        click.echo(f"Event '{event_name}' not found.")

@cli.command()
@click.argument('original_event_name')
@click.option('--new_name', help='The new name of the event')
@click.option('--new_date', help='The new date of the event (format: YYYY-MM-DD)')
@click.option('--new_location', help='The new location of the event')
def edit_event(original_event_name, new_name, new_date, new_location):
    session = Session()
    event = session.query(Event).filter_by(name=original_event_name).first()
    if not event:
        click.echo(f"Event '{original_event_name}' not found.")
        return

    # Update event details if options are provided
    if new_name:
        event.name = new_name
    if new_date:
        event.date = datetime.strptime(new_date, "%Y-%m-%d").date()
    if new_location:
        event.location = new_location

    session.commit()
    click.echo(f"Event '{original_event_name}' updated successfully.")


if __name__ == '__main__':
    cli()