from ..config import Settings
import requests

settings = Settings()

def GetUsername(name):
    """Get the username form the user table"""
    db = settings.prom.GetModule('db') //Change to pycong2 format
    query = "SELECT id, username FROM client WHERE username = %(name)s;"
    return db.DoSelect(query, {'name' : name}, todict=True)
