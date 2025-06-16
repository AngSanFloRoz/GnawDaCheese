# GnawDaCheese
A web scraping project using Python by the Hacktouille team

---

## What is web scrapping?

Web scraping is an automation technique used to collect specific data from web pages, using mechanisms and scripts that analyze the source code of the page in question to filter large amounts of information and obtain the required data.

### Which are its purposes?

Some of its purposes are:
1. Data collection for analysis and research
2. Competition monitoring
3. Database generation
4. Data collection for AI training
5. Social networks analysis and trend monitoring

### WARNINGS

These are some recommendations to consider before practicing web scraping:
1. Always verify the terms of service
2. Avoid the collection of personal data without consent
3. Do not overload servers
4. Make sure that the use of data is ethical and legal

--- 

## Class diagram

---
```mermaid
  classDiagram
direction TB
    class Url {
      +string direction
      +url_status()
    }
    class Petition {
      +string filter
      +access()
    }
    class Search{
      +webs: list
      +add_web()
    }    
    class Website {
	    +"Url"
	    +string name
	    +string creation_date
	    +list_titles()
	    +list_hyperlinks()
    }

    Url --o Website: "has a"

    class SocialNetwork {
	    +string gender
	    +string marital_status
	    +string birthdate
	    +average_daily_posts()
    }

    class News {
	    -string date
	    -string author
	    -string place_of_events
	    -people_involved()
    }

    class Wiki {
      +list related_articles
	    +string name
	    +int num_images
	    +filter_by_topic()
    }

    class OnlineStore {
      -list products
      -float price
      -string seller
      -float punctuation
      -search_cheapest()
      -search_best_quality()
    }

    class WebScraping{
      +"Petition"
      +list websites
      +export_info()   
    }
    
    Website <|-- OnlineStore: "is a"
    Website <|-- SocialNetwork: "is a"
    Website <|-- News: "is a"
    Website <|-- Wiki: "is a"
    OnlineStore --o WebScraping: "has a"
    SocialNetwork --o WebScraping: "has a"
    News --o WebScraping: "has a"
    Wiki --o WebScraping: "has a"
    Petition --o WebScraping: "has a"
    Search --o WebScraping: "has a"
```
## preleminary solution
With Web scraping we purpose is find information quickly using OOP to achieve it
