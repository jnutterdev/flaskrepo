import sqlite3
from flask import Blueprint

models = Blueprint('models', __name__)

#  DATABASE FUNCTIONS
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', 
        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post 