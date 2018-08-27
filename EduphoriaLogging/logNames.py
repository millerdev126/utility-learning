'''
This script's purpose is to simplify and automate the process of giving attendees credit in Eduphoria.
It will read a Google Sheet, and pull the names of attendees listed there, search for each one in turn,
and when found, give that user credit for the course they attended.

Current issues: Unable to get script to interact with spreadsheet at all. The error code indicates that it's
                looking for a string, bytes or path as an argument and it's getting a list. Seems to be coming from
                the OAuth2 client trying to access the .json file with the credentials in it. My head hurts so
                I'm saving trouble shooting for after lunch. Forgive me.

8/27/17
Michael Miller
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_p12_keyfile('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Sign In Names").sheet1

list_of_hashes = sheet.get_all_records(()
                                       )
print(list_of_hashes)
