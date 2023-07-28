from app.helpers.gcp_helper import ScrapingMail

class Scrap():
    
    def __init__(self):
        self.SCOPES = ['https://mail.google.com/']
    
    def starting_scrap(self,query):
        service = ScrapingMail.service(self.SCOPES)
        results = ScrapingMail.search_messages(service,query)
        
        for msg in results:
            parts, headers = ScrapingMail.read_message(self,service,msg)
            # Here you have to write what to do with each email
            # Also in gcp_helper has function to extract and save pdf attached to email

        ScrapingMail.mark_as_read(service, query)
    
if __name__ == '__main__':
    
    scraping = Scrap()
    query="label:INBOX is:unread"
    Scrap.starting_scrap(query)