import os
import argparse
import requests
import json
from github import Github
from dotenv import load_dotenv
load_dotenv()

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

# def setup():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-o", "--org", help="choose what company you what to see", required=True)
#     parser.add_argument("-t", "--token", help="OAuth token from GitHub", required=True)
#     args = parser.parse_args()
#     return args

def list_orgs(AUTH_TOKEN):
    g = Github(AUTH_TOKEN)
    orgslist = []
    for orgs in g.get_user().get_orgs():
        orgslist.append(orgs.login)
    return orgslist

print(list_orgs(AUTH_TOKEN))

def list_org_members(org, AUTH_TOKEN):
    s = requests.Session()
    s.headers.update({'Authorization': 'token ' + AUTH_TOKEN})
    g = Github(AUTH_TOKEN)
    namesmembers = []
    # try:
    #     filename = "memblist_" + org + ".txt"
    #     text_file = open(filename, "r")
    #     loginmembers = text_file.read().split(',')
    # except:
    loginmembers = []
    for orgs in g.get_user().get_orgs():
        if orgs.login == org:
            for memb in orgs.get_members():
                if memb.login not in loginmembers:
                    loginmembers.append(memb.login)
        else:
            next
    if loginmembers[0] == "":
        loginmembers.pop(0)
    for member in loginmembers:
        r = s.get("https://api.github.com/users/" + member)
        r_user = json.loads(r.text)
        try:
            if r_user["name"] != None:
                namesmembers.append(r_user["name"])
            else:
                namesmembers.append(r_user["login"])
        except:
            next
    return loginmembers, namesmembers

logins_names = {l:n for l, n in zip(list_org_members(list_orgs(AUTH_TOKEN)[1], AUTH_TOKEN)[0],list_org_members(list_orgs(AUTH_TOKEN)[1], AUTH_TOKEN)[1])}

print(logins_names)