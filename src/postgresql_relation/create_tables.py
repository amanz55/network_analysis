import os
import sys

rpath = os.path.abspath('./')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

from src.postgresql_relation.data_frame_to_postgres import create_database_engine


def create_tables(engine):
    metadata = MetaData()

    # Messages Table
    messages_table = Table('messages_table', metadata,
        Column('msg_type', String),
        Column('msg_content', String),
        Column('sender_name', String),
        Column('msg_sent_time', DateTime),
        Column('msg_dist_type', String),
        Column('time_thread_start', DateTime),
        Column('reply_count', Integer),
        Column('reply_users_count', Integer),
        Column('reply_users', String),
        Column('tm_thread_end', DateTime),
        Column('channel', String)
    )

    # Reactions Table
    reactions_table = Table('reactions_table', metadata,
        Column('reaction_name', String),
        Column('reaction_count', Integer),
        Column('reaction_users_count', Integer),
        Column('message', String),
        Column('user_id', String),
        Column('channel', String)
    )

    # Users Table
    users_table = Table('users_table', metadata,
        Column('user_name', String),
        Column('user_id', String)
    )

    # Create tables
    metadata.create_all(engine)
    print("Successful")
    return True