# webbrowser module documentation
import requests, json, re, csv

#get the first request
payload = {"api-key": "YOUR API-KEY", 'begin_date': "YOUR BEGIN DATE",
  'end_date': 'YOUR END DATE', 'sort': 'newest', 'page': '1'}
r = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)
data=json.loads (r.text)
response=data['response']

# total hits and divide by 10 to get the number of pages
total_hits = response['meta']['hits']
total_pages = response['meta']['hits'] / 10

print("There are",total_pages,"total pages of results")

with open('newest.csv', 'w', newline='') as f:
    writer = csv.writer(f)

        # lets loop through 10 pages

    for x in range(0,10):

        #in each loop x with be 1 -> 10

        print("~~~~~~~~~ page",x,"~~~~~~~~~~")

        #change the page number we want to use:
        payload['page'] = x
        r = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)
        data=json.loads (r.text)
        response=data['response']

        docs=response['docs']


        for a_doc in docs:

            #write three if statements

            # let's check if there is a comma, if so split on it
            if ',' in a_doc['snippet']:
                words = a_doc['snippet'].split(',')
            elif ' and ' in a_doc['snippet']:
                words = a_doc['snippet'].split('and')
            # to split on  "in," "on," "at," or "for" we need to use a regular expression
            else:
                words = re.split("in|on|at|for",a_doc['snippet'])

            # only print it if it worked
            if len(words) > 1:
                #do something with the words here
                print(words) 
                
                writer.writerow (words)
            
            