# -*- coding:utf-8 -*-



class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.team_urls = set()
        self.old_team_urls = set()
    
    # 球员个人信息链接
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls or url not in self.old_urls :
            self.new_urls.add(url)
        
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0 :
            return
        for url in urls :
            self.add_new_url(url)
        
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    #球队链接
    
    def add_team_url(self,url):
        if url is None:
            return
        if url not in self.team_urls or url not in self.old_team_urls :
            self.team_urls.add(url)   
    
    def get_team_url(self):
        team_url = self.team_urls.pop()
        self.old_team_urls.add(team_url)
        return team_url    
    
    
    def add_team_urls(self,urls):
        if urls is None or len(urls)==0 :
            return
        for url in urls :
            self.add_team_url(url)
    
    
    def has_team_url(self):
        return len(self.team_urls) != 0


