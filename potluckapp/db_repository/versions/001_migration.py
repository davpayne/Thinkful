from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item = Table('item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('event_id', Integer),
    Column('category', String(length=20)),
    Column('person', String(length=140)),
)

event = Table('event', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('event_id', String),
    Column('event_date', String),
    Column('about_me', String),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].create()
    pre_meta.tables['event'].columns['about_me'].drop()
    pre_meta.tables['event'].columns['event_date'].drop()
    pre_meta.tables['event'].columns['event_id'].drop()
    pre_meta.tables['event'].columns['last_seen'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].drop()
    pre_meta.tables['event'].columns['about_me'].create()
    pre_meta.tables['event'].columns['event_date'].create()
    pre_meta.tables['event'].columns['event_id'].create()
    pre_meta.tables['event'].columns['last_seen'].create()
