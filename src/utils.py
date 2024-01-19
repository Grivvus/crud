import sqlalchemy

from db import get_db_session
from models import Note

def get_all_notes():
    notes_dict = dict()
    session = get_db_session()
    notes = sqlalchemy.select(Note)

    for note in session.scalars(notes):
        notes_dict[note.id] = note

    return notes_dict


def get_one_note(id: int):
    session = get_db_session()
    note = sqlalchemy.select(Note).where(Note.id==id)
    note_ = session.scalar(note)

    return {note_.name: note_}

def update_one_note(id: int, new_name: str | None,
                    new_desc: str | None):
    args_to_update = dict()
    with get_db_session() as session:
        if new_name is not None and new_desc is not None:
            args_to_update[Note.description] = new_desc
            args_to_update[Note.name] = new_name
        elif new_name is not None:
            args_to_update[Note.name] = new_name
        elif new_desc is not None:
            args_to_update[Note.description] = new_desc
        else:
            raise ValueError('Нельзя поменять значение объкта'+
                             ' на пустой параметр')
        session.query(Note).filter(Note.id==id).\
            update(args_to_update)
        session.commit()


def change_note_status(id: int, new_status: bool):
            with get_db_session() as session:
                session.query(Note).filter(Note.id==id).\
                update({Note.status: new_status})
                session.commit()


def delete_one_note(id: int):
    with get_db_session() as session:
        session.query(Note).filter(Note.id==id).delete()
        session.commit()

def create_new_note(name: str, desc: str | None, status: bool = False):
    new_note = Note(name=name, description=desc, status=status)
    with get_db_session() as session:
        session.add(new_note)
        session.commit()