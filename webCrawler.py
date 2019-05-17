import requests, sys, webbrowser, bs4, re
from bs4 import Comment
from bs4 import BeautifulSoup
class webCrawler:
    def __init__(self,currentElement):
        self.currentElement = currentElement
    def requestedlink(self):
        x=str(self.currentElement)
        request_Link=requests.get(x)
        parsed_Page=BeautifulSoup(request_Link.content,'html.parser')
        #print(type(parsed_Page))
        return parsed_Page
    def normalFile(self,parsedPage,index):
        particularLink = self.currentElement
        sms  = "Done"
        content=[]
        for text in parsedPage.find_all('div'):
            for script in text(["script", "style"]):
                script.extract()
            fetchedText = text.get_text()
            content.append(str(fetchedText))
        extracted_site_name_for_url = particularLink.split('/')
        extracted_site_name_for_url = extracted_site_name_for_url[2]
        filename = str(extracted_site_name_for_url)+str(index)+".txt"
        file = open(filename, "w" , encoding="utf-8")
        file.writelines(content)
        file.close()
        return sms
    def stackOverFlow(self,parsedPage,index):
        particularLink = self.currentElement
        sms  = "stackoverflow scraped successfully"
        content=[]
        for text in parsedPage.find_all('div', attrs={'class':'snippet-hidden'}):
            for script in text(["script", "style"]):
                script.extract()
            fetchedText = text.get_text()
            content.append(str(fetchedText))
        extracted_site_name_for_url = particularLink.split('/')
        extracted_site_name_for_url = extracted_site_name_for_url[2]
        filename = str(extracted_site_name_for_url)+str(index)+".txt"
        file = open(filename, "w" , encoding="utf-8")
        file.writelines(parsedPage)
        file.close()
        return sms

    def Quora(self,parsedPage,index):
        particularLink = self.currentElement
        sms  = "Quora scraped successfully"
        content=[]
        for text in parsedPage.find_all('div', attrs={'class':'grid_page'}):
            for script in text(["script", "style"]):
                script.extract()
            fetchedText = text.get_text()
            content.append(str(fetchedText))
        extracted_site_name_for_url = particularLink.split('/')
        extracted_site_name_for_url = extracted_site_name_for_url[2]
        filename = str(extracted_site_name_for_url)+str(index)+".txt"
        file = open(filename, "w" , encoding="utf-8")
        file.writelines(content)
        file.close()
        return sms

    def stackExchange(self,parsedPage,index):
        particularLink = self.currentElement
        sms  = "StackExchange scraped successfully"
        content=[]
        for text in parsedPage.find_all('div', attrs={'class':'snippet-hidden'}):
            for script in text(["script", "style"]):
                script.extract()
            fetchedText = text.get_text()
            content.append(str(fetchedText))
        extracted_site_name_for_url = particularLink.split('/')
        extracted_site_name_for_url = extracted_site_name_for_url[2]
        filename = str(extracted_site_name_for_url)+str(index)+".txt"
        file = open(filename, "w" , encoding="utf-8")
        file.writelines(content)
        file.close()
        return sms

if __name__ == "__main__":
    userInput=sys.argv[1:]
    queryString=""
    for particularArgument in userInput:
        queryString+=particularArgument+" "
    res = requests.get('https://google.com/search?q='+''.join(queryString))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    #print(soup.prettify())
    xx=[]
    xx.append(soup.prettify())
    filename = "searchpage.txt"
    file = open(filename, "w" , encoding="utf-8")
    file.writelines(xx)
    file.close()
    print("---------------"+"search page crwaled successfully   ")
    for div in soup.find_all('div',attrs={'class':'r'}):
        a=div.find_all('a')[1]
        print(a)
    linkElements=soup.find_all("cite")
    linkToOpen=min(20,len(linkElements))
    linkElements.pop()
    linkElements.append("https://stackoverflow.com/questions/26627080/beautifulsoup-how-to-get-nested-divs")
    for i in range(linkToOpen):
        try:
            #print(linkElements[i])
            particularLink=str(linkElements[i].get_text())
            #print(particularLink)
            if "quora" in particularLink:
                currentElement = webCrawler(particularLink)
                parsedPage = currentElement.requestedlink()
                sms = currentElement.Quora(parsedPage,(i+1))
                print(sms)
            elif "stackoverflow" in particularLink:
                currentElement = webCrawler(particularLink)
                parsedPage = currentElement.requestedlink()
                sms = currentElement.stackOverFlow(parsedPage,(i+1))
                print(sms)
            elif "stackexchange" in particularLink:
                currentElement = webCrawler(particularLink)
                parsedPage = currentElement.requestedlink()
                sms = currentElement.stackExchange(parsedPage,(i+1))
                print(sms)
            elif "youtube" in particularLink:
                print("Youtube link found no need to scrape")
                continue
            else:
                currentElement = webCrawler(particularLink)
                parsedPage = currentElement.requestedlink()
                sms = currentElement.normalFile(parsedPage,(i+1))
                print(sms)
        except:
            print("Error Occured")
            continue