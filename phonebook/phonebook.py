import sys
import json
import os
from copy import deepcopy

REQUEST_DATA = "data"
REQUEST_TYPE = "type"
NAME_FIELD = "_name"
PHONE_FIELD = "phone"
COUNTRY_FIELD = "country"
RESPONSE_STATUS_CODE = "status_code"
RESPONSE_DATA = "data"
STATUS_SUCCESS = 200
STATUS_NOT_FOUND = 404
STATUS_BAD_REQUEST = 400

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
    for pb_entry in DATABASE:
        if request_data[NAME_FIELD] == pb_entry[NAME_FIELD]:
            return {
                RESPONSE_STATUS_CODE: STATUS_BAD_REQUEST
            }
    for key in PHONEBOOK_ENTRY:
        if key in request_data:
            pb_entry[key] = request_data[key]
        else:
            return {
                RESPONSE_STATUS_CODE: STATUS_BAD_REQUEST
            }
    DATABASE.append(pb_entry)
    UPDATE_DATABASE()
    return {
        RESPONSE_STATUS_CODE: STATUS_SUCCESS,
        RESPONSE_DATA: pb_entry
    }
    
def GET_REQUEST(request_data):
    if NAME_FIELD in request_data:
        for pb_entry in DATABASE:
            if request_data[NAME_FIELD] == pb_entry[NAME_FIELD]:
                return {
                    RESPONSE_STATUS_CODE: STATUS_SUCCESS,
                    RESPONSE_DATA: pb_entry
                }
    return {
        RESPONSE_STATUS_CODE: STATUS_NOT_FOUND
    }
    
def UPDATE_REQUEST(request_data):
    if NAME_FIELD in request_data:
        name_value = request_data[NAME_FIELD]
        for pb_entry in DATABASE:
            if name_value == pb_entry[NAME_FIELD]:
                for key in PHONEBOOK_ENTRY:
                    if key in request_data:
                        pb_entry[key] = request_data[key]
                UPDATE_DATABASE()
                return {
                    RESPONSE_STATUS_CODE: STATUS_SUCCESS,
                    RESPONSE_DATA: pb_entry
                }
    return {
        RESPONSE_STATUS_CODE: STATUS_NOT_FOUND
    }
    
def DELETE_REQUEST(request_data):
    if NAME_FIELD in request_data:
        name_value = request_data[NAME_FIELD]
        for pb_entry in DATABASE:
            if name_value == pb_entry[NAME_FIELD]:
                DATABASE.remove(pb_entry)
                UPDATE_DATABASE()
                return {
                    RESPONSE_STATUS_CODE: STATUS_SUCCESS,
                    RESPONSE_DATA: pb_entry
                }
    return {
        RESPONSE_STATUS_CODE: STATUS_NOT_FOUND
    }



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
        print json.dumps(REQUEST_TYPES[ request[REQUEST_TYPE] ]( request[REQUEST_DATA] ), sort_keys=True)

if __name__ == "__main__":
    main()
