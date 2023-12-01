import os
import sys

import pandas as pd
from sqlalchemy import create_engine

rpath = os.path.abspath('./')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader
from src.postgresql_relation.create_tables import create_tables
from src.postgresql_relation.data_frame_to_postgres import create_database_engine


def map_df_to_user_table(engine, dataframe):
    table_name = 'user_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')

def map_df_to_reaction_table(engine, dataframe):
    table_name = 'reaction_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')

def map_df_to_message_table(engine, dataframe):
    table_name = 'message_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')

if __name__ == "__main__":
    sl = SlackDataLoader()
    user_df = sl.create_users_df()
    reaction_df = sl.create_reaction_data_frame()
    message_df = sl.create_data_frame()

    engine = create_database_engine()
    create_tables(engine)
    map_df_to_user_table(engine, user_df)
    map_df_to_reaction_table(engine, reaction_df)
    map_df_to_message_table(engine, message_df)