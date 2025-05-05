import requests

BASE_URL = "http://chrisbrooks.pythonanywhere.com/"


#Plural GET of famous programmers: /api/programmers
#This returns a list of programmers, embedded in a top-level dictionary with a single element
def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    r = requests.get(BASE_URL + "api/programmers") #sends a GET request and gets the url and returns a response
    r.raise_for_status()
    data = r.json()
    return len(data.get("programmers", []))

# the second one is to Singular GET of a famous programmer: /api/programmers/<id>
#get by ID
def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    r = requests.get(BASE_URL + f"api/programmers/{pid}") #same url but we're getting by a single Id of a famous programmer
    if r.status_code !=200: #if it does return a 200 ok, then return an empty list--dict
        return {} #returns it empty
    return r.json() #python dict

# Plural (zero or more responses)
# GET of a list of famous programmers matching a given first name: /api/programmers/by_first_name/<first_name>
def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    r = requests.get(BASE_URL + "api/programmers/by_first_name/{first_name}") #same thing but we're getting first names

    return ""
