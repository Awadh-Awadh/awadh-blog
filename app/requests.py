import requests as rq
# base_url = None

# def configure_requests():
#     global base_url
#     base_url = app.config['BASE_URL']

base_url='http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():

    with rq.get(base_url) as data:
       quotes = data.json

    return quotes
