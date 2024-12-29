
def emailParser(mymail):
    
    email = mymail
    emailDomain = ''

    emailSlices = {
        "username": "",
        "domain": ""
    }

    email = email.split("@")

    emailSlices["username"] = email[0]

    emailDomain = email[1]
    emailDomain = emailDomain.split(".")
    emailSlices["domain"] = emailDomain[0]




    print("your username is ", emailSlices["username"], " & domain is ",emailSlices["domain"])
    
    
emailParser("noorzarei@gmail.com")