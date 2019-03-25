import json

database_path = "login_data.json"
database = []

def main():
    json_data = open(database_path)
    database = json.load(json_data)
    # print(database)

    request_data = open("login_input.json")
    request = json.load(request_data)
    print(request)
    if request_type in request == 'GET'
        print('MATA')



if __name__ == "__main__":
    main()