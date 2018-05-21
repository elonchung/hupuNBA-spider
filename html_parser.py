# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    
    
    def parser(self , page_url , html_cont):
        
        if page_url is None or html_cont is None :
            return
        
        new_urls = self._get_new_url(page_url,html_cont)
        
        new_data = self._get_new_data(page_url,html_cont)
        
        return new_urls,new_data
            
    def parser_team_url (self, page_url, html_cont):
        
        if page_url is None or html_cont is None :
            return
        
        new_urls = self._get_new_url(page_url,html_cont)
            
        return new_urls
    
    def parser_team_urls (self, html_cont):
        
        soup = BeautifulSoup(html_cont,'lxml')
        
        links = soup.select('span[class="team_name"] a')
    
        new_urls = set()
    
        for link in links :
            new_urls.add(link['href'])
            
        return new_urls    

    def _get_new_url(self, page_url, html_cont):
        
        soup = BeautifulSoup(html_cont,'lxml')
        
        links = soup.find_all('a',href=re.compile(r"https://nba\.hupu\.com/players/.*html"))
    
        
        new_urls = set()
    
        for link in links :
            new_urls.add(link['href'])
            
        return new_urls
    
    
    def _get_new_data(self, page_url, html_cont):
        
        
        soup = BeautifulSoup(html_cont,'lxml')
        
        res_data = {}
        
        
        res_data['url'] = page_url 
        
        try :
            player_name = soup.find('div',class_="team_data").find('h2')
            
            
            res_data['player_name'] = player_name.get_text()
            
            player_score = soup.find('div',class_="table_team_box")
            
            res_data['player_score'] = player_score.get_text()
            
            player_team = soup.find('a',style="color:red")
            
            res_data['player_team'] = player_team.get_text()
        
            return res_data
        except:
            return res_data

        