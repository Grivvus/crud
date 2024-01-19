from typing import Optional
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import BOOLEAN
from sqlalchemy import DATETIME
from sqlalchemy import MetaData
from sqlalchemy import null
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = 'user'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True)
#     first_name: Mapped[str] = mapped_column(String(30))
#     second_name: Mapped[str] = mapped_column(String(30))


#     def __repr__(self) -> str:
#         return f'User(id={self.id}, username={self.username},
#         first_name={self.username}, second_name={self.second_name})'



class Note(Base):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True)
    # user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(), nullable=True)
    # status=False -> not complited; status=True -> complited
    status: Mapped[bool] = mapped_column(BOOLEAN(), default=False)
    # opened_time: Mapped[DATETIME] = mapped_column(DATETIME(), default=...)
    # closed_time: Mapped[DATETIME] = mapped_column(DATETIME(), nullable=True,
    #                                               default=null)


    def __repr__(self) -> str:
        if self.status == True:
            s = 'closed'
        else:
            s = 'opened'

        return (f'Note(id={self.id}, name={self.name}, status={s},' +
                f'opened_at={self.opened_time})')
