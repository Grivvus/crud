from typing import Annotated

import fastapi
from fastapi import Body

import utils

app = fastapi.FastAPI()

@app.get('/')
def get_all_notes():
    return utils.get_all_notes()


@app.get('/{note_id}')
def get_one_note(
    note_id: Annotated[int,
                        fastapi.Path(title='id note to get', ge=0)]
            ):
    # на несуществующий индекс выкидывает непонятную ошибку
    return utils.get_one_note(note_id)


@app.patch('/{note_id}')
def update_one_note(
    note_id: Annotated[int,
                       fastapi.Path(title='id note to update', ge=0)],
        name: Annotated[str | None, Body()],
    description: Annotated[str | None, Body()],
):
    utils.update_one_note(note_id, name, description)
    return {note_id: 'Changed succesfully'}

@app.patch('/{note_id}/change_status')
def change_note_status(
    note_id: Annotated[int, fastapi.Path(ge=0)],
    status: Annotated[bool, Body()]
):
    utils.change_note_status(note_id, status)
    return {note_id: 'Status changed succesfully'}


@app.delete('/{note_id}')
def delete_one_note(
    note_id: Annotated[int,
                       fastapi.Path(title='id note to delete', ge=0)]
                ):
    utils.delete_one_note(note_id)
    return {note_id: 'Deleted successfully'}


@app.post('/create_new_note')
def create_new_note(
    name: Annotated[str, Body()],
    description: Annotated[str | None, Body()],
    status: Annotated[bool | None, Body()]
):
    utils.create_new_note(name, description, status)
    return {name: 'new note created successfully'}
