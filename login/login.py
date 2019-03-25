import json

database_path = "login_data.json"
request_path = "login_input.json"
request_response = "login-response.json"
database = []

def check(db, request):
    for db_element in db:
        if db_element["_username"] == request["_username"]:
            if db_element["pass"] == request["pass"]:
                return 1
    return 0


def main():
    #preiau datele din db
    json_data = open(database_path)
    database = json.load(json_data)
    # print(database)

    #preiau datele din input
    request_data = open("login_input.json")
    request = json.load(request_data)

    if request["type"] == "check":
        response = check(database, request["data"] )

    #creez obiectul pentru raspuns
    response_obj = {}
    response_obj[''] = []
    if response == 1:
        response_obj[''].append({
            'status':'ok'
        })
    else:
        response_obj[''].append({
            'status':'not ok'
        })

    
    #afisez raspunsul
    print(response_obj)

if __name__ == "__main__":
    main()