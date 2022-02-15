import requests
from tabulate import tabulate


def get_user_from_api(page, urutan="asc"):
    if not isinstance(page, int):
        return "Error!! page harus berbentuk angka!"

    headers = {'app-id': '61d4660ec7b62522ea430bdf'}
    response = requests.get(f"https://dummyapi.io/data/v1/user?page={page}&limit=10", headers=headers)
    data = (response.json()["data"])

    print(urutan)
    if urutan == "desc":
        data = sorted(data, key=lambda i: i['firstName'], reverse=True)
        result = tabulate(data, headers="keys", tablefmt="orgtbl")
        return result

    data = sorted(data, key=lambda i: i['firstName'])
    result = tabulate(data, headers="keys", tablefmt="orgtbl")
    return result


page = int(input("masukkan page: "))
urutan = input("Pilih urutan [asc/desc] (default is asc) : ")
print(get_user_from_api(page, urutan))
