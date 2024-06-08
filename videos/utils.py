"""
file: utils.py
location: videos/utils.py
"""
# from pymongo import MongoClient
# # pylint: disable=unused-argument
# def get_db_handle(db_name, host, port, username, password):
#     '''
#     function: get_db_handle
#     description: This function is used to get the database handle.
#     '''
#     client = MongoClient(host=host,
#         port=int(port),
#         username=username,
#         password=password
#     )
#     db_handle = client['db_name']
#     return db_handle, client
from pymongo import MongoClient
client = MongoClient('connection_string')
db = client['db_name']
