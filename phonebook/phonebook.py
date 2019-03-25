import sys
import json
import os
from copy import deepcopy

REQUEST_DATA = "data"
REQUEST_TYPE = "type"
NAME_FIELD = "_name"
PHONE_FIELD = "phone"
COUNTRY_FIELD = "country"

PHONEBOOK_ENTRY = {
    NAME_FIELD: "",
    PHONE_FIELD: "",
    COUNTRY_FIELD: ""
}

DATABASE_PATH = "phonebook.json"
DATABASE = []

def READ_DATABASE():
    global DATABASE
    with open(DATABASE_PATH, "rb") as f:
        DATABASE = json.load(f)

def UPDATE_DATABASE():
    with open(DATABASE_PATH, "wb") as f:
        json.dump(DATABASE, f, indent=4, sort_keys=True)

def POST_REQUEST(request_data):
    pb_entry = deepcopy(PHONEBOOK_ENTRY)
    for key in PHONEBOOK_ENTRY:
        if key in request_data:
            pb_entry[key] = request_data[key]
        else:
            return "ERROR" #TODO: as json
    DATABASE.append(pb_entry)
    UPDATE_DATABASE()
    return "OK"
    
def GET_REQUEST(request_data):
    if NAME_FIELD in request_data:
        name_value = request_data[NAME_FIELD]
        for entry in DATABASE:
            if name_value == entry[NAME_FIELD]:
                return entry
    return "ERROR"
    
def UPDATE_REQUEST(request_data):
    if NAME_FIELD in request_data:
        name_value = request_data[NAME_FIELD]
        for pb_entry in DATABASE:
            if name_value == pb_entry[NAME_FIELD]:
                for key in PHONEBOOK_ENTRY:
                    if key in request_data:
                        pb_entry[key] = request_data[key]
                UPDATE_DATABASE()
                return pb_entry
    return "ERROR"
    
def DELETE_REQUEST(request_data):
    if NAME_FIELD in request_data:
        name_value = request_data[NAME_FIELD]
        for entry in DATABASE:
            if name_value == entry[NAME_FIELD]:
                DATABASE.pop(entry)
                return "OK"
    return "ERROR"

REQUEST_TYPES = {
    "POST": POST_REQUEST,
    "GET": GET_REQUEST,
    "UPDATE": UPDATE_REQUEST,
    "DELETE": DELETE_REQUEST
}





def main():
    if os.path.exists(DATABASE_PATH):
        READ_DATABASE()
    request = json.load(sys.stdin)
    if REQUEST_TYPE in request and REQUEST_DATA in request and request[REQUEST_TYPE] in REQUEST_TYPES and request:
        print REQUEST_TYPES[ request[REQUEST_TYPE] ]( request[REQUEST_DATA] )

if __name__ == "__main__":
    main()
