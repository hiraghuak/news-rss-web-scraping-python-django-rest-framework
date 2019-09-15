from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup
from bs4 import CData
import bleach
import bs4

class Timesofindia(APIView):
    """ https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms """

    def get(self, request, formate=None, ):
        """"Returns a list of Apiview features """
        tp_api = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('item', )
        records = []
        for result in results:
            main = result.find('description').string

            images = main

            response_dictionary = {
                "title": result.find('title').string,
                "description": result.find('description').string,
                "link": result.find('link').string,
                "guid": result.find('guid').string,
                "images": images,
            }

            records.append(response_dictionary)
        return Response(records)


class AbpRss(APIView):
    """ https://www.abplive.in/home/feed  """

    def get(self, request, formate=None, ):
        """"Returns a list of Apiview features """
        tp_api = "https://www.abplive.in/home/feed"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('item')
        records = []
        for result in results:
            response_dictionary = {
                "title": result.find('title').get_text(),
                "description": result.find('description').get_text(),
                "guid": result.find('comments').get_text(),
            }
            records.append(response_dictionary)
        return Response(records)


class news18(APIView):
    """ https://www.news18.com/rss/books.xml  """

    def get(self, request, formate=None, ):
        """"Returns a list of Apiview features """
        tp_api = "https://www.news18.com/rss/books.xml"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('item')
        records = []
        for result in results:
            response_dictionary = {
                "title": result.find('title').string,
                "link": result.find('link').string,
                "description": result.find('description').string,
            }
            records.append(response_dictionary)
        return Response(records)


class Bhaskar(APIView):
    """ https://www.bhaskar.com/rss-feed/2322/  """

    def get(self, request, formate=None, ):
        """"Returns a list of Apiview features """
        tp_api = "https://www.bhaskar.com/rss-feed/2322/"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('item')
        records = []
        for result in results:
            response_dictionary = {
                "title": result.find('title').get_text(),
                "link": result.find('link').get_text(),
                "description": result.find('description').get_text(),
            }
            records.append(response_dictionary)
        return Response(records)


class Ndtv(APIView):
    """ http://feeds.feedburner.com/ndtvnews-top-stories  """

    def get(self, request, formate=None, ):
        """"Returns a list of Apiview features """
        tp_api = "http://feeds.feedburner.com/ndtvnews-top-stories"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('item')
        records = []
        for result in results:
            response_dictionary = {
                "title": result.find('title').get_text(),
                "fullimage": result.find('fullimage').get_text(),
                "description": result.find('description').string,
            }
            records.append(response_dictionary)
        return Response(records)


class allRss(APIView):

    def get(self, request, formate=None, ):

        # TIME OF INDIA START
        timeofindia_tp_api = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
        timeofindia_response = requests.get(timeofindia_tp_api)
        timeofindia_soup = BeautifulSoup(timeofindia_response.text, 'html.parser')
        timeofindia_results = timeofindia_soup.find_all('item', )
        timeofindia_records = []
        for timeofindia_result in timeofindia_results:
            main = timeofindia_result.find('description').string
            timeofindia_images = main
            timeofindia_response_dictionary = {
                "title": timeofindia_result.find('title').string,
                # "description": timeofindia_result.find('description').string,
                # "link": timeofindia_result.find('link').string,
                "guid": timeofindia_result.find('guid').string,
                # "images": timeofindia_images,
            }
            timeofindia_records.append(timeofindia_response_dictionary)
        # TIME OF INDIA END

        # ABP LIVE NEWS START
        abplive_tp_api = "https://www.abplive.in/home/feed"
        abplive_response = requests.get(abplive_tp_api)
        abplive_soup = BeautifulSoup(abplive_response.text, 'html.parser')
        abplive_results = abplive_soup.find_all('item')

        abplive_records = []
        for abplive_result in abplive_results:
            abplinkd = abplive_result.find('comments').text
            clearlink_n = abplinkd.replace('\n', '')
            clearlink_r = clearlink_n.replace('\r', '')
            clearlink_clean = clearlink_r.replace('\t', '')

            abplive_response_dictionary = {
                "title": abplive_result.find('title').get_text(),
                # "description": abplive_result.find('description').get_text(),
                "link": clearlink_clean,
                "img": abplive_result.find('media:thumbnail')['url'],
            }
            abplive_records.append(abplive_response_dictionary)
        # ABP LIVE NEWS END

        # NEWS18 START
        news18_tp_api = "https://www.news18.com/rss/books.xml"
        news18_response = requests.get(news18_tp_api)
        news18_soup = BeautifulSoup(news18_response.text, 'html.parser')
        news18_results = news18_soup.find_all('item')
        news18_records = []

        # for result in news18_results:
        #     news18_imgs = BeautifulSoup(result.find('description').string, 'html.parser')
        #     print(news18_imgs.img['src'])

        for news18_result in news18_results:
            news18_imgs = BeautifulSoup(news18_result.find('description').string, 'html.parser')
            get_news18_img = news18_imgs.img['src']
            news18_response_dictionary = {
                "title": news18_result.find('title').string,
                "link": news18_result.find('guid').string,
                "img": get_news18_img,

            }
            news18_records.append(news18_response_dictionary)
        # NEWS18 END

        # DAINIK BHASKAR START
        bhaskartp_apid = "https://www.bhaskar.com/rss-feed/2322/"
        bhaskar_responsed = requests.get(bhaskartp_apid)
        bhaskar_soupd = BeautifulSoup(bhaskar_responsed.text, 'html.parser')
        bhaskar_results = bhaskar_soupd.find_all('item')
        bhaskar_reconds = []

        for bhs_result in bhaskar_results:
            bhs_okmain = BeautifulSoup(bhs_result.find('description').text, 'html.parser')
            bhs_a_tag = bhs_okmain.find_all('a')
            bhs_img_tag = bhs_okmain.find_all('figure')

            bjsk_titles = bhs_result.find('title').get_text()

            for bhs_get_img_src in bhs_img_tag:
                bhs_clean_imgse = bhs_get_img_src.a.img['src']

            for bhs_resultimg in bhs_a_tag:
                bhs_bhaskar_page_link = bhs_resultimg['href']

            bhaskar_red = {
                "title": bjsk_titles,
                "link": bhs_bhaskar_page_link,
                "img": bhs_clean_imgse,
            }

            bhaskar_reconds.append(bhaskar_red)
        # DAINIK BHASKAR END

        # NDTVNEW START
        tp_api = "http://feeds.feedburner.com/ndtvnews-top-stories"
        response = requests.get(tp_api)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('item')
        records = []

        for result in results:
            response_dictionary = {
                "title": result.find('title').text,
                "link": result.find('link').text,
                "fullimage": result.find('fullimage').text,
            }

            records.append(response_dictionary)
        # NDTVNEW END

        # MAIN RESPONSE START
        ndtvnewsrss = {
            "ndtvnews": records,
            "bhaskar": bhaskar_reconds,
            "abp": abplive_records,
            "news18": news18_records,
            "timeofindia": timeofindia_records,
        }
        # MAIN RESPONSE END

        return Response(ndtvnewsrss)
