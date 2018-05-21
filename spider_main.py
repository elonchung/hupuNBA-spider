# -*- coding:utf-8 -*-

from NBA_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    

    def __init__(self):
        
        # 初始化 url管理器、html下载器、html解析器、html输出器
        
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def carw(self, root_url):
        
        #获取所有球队网页
        html_cont = self.downloader.downloader(root_url)
        team_urls = self.parser.parser_team_urls(html_cont)
        
        # 存储球队链接
        self.urls.add_team_urls(team_urls)
        
        #获取球队子页面的所有球员链接
        if team_urls is None :
            print("no teams")
            return
        
        count = 1 
        for team_url in team_urls:
            
            #获取球队子页面的所有球员链接
            print(len(self.urls.team_urls))
            
            team_url = self.urls.get_team_url() 
        
            html_cont = self.downloader.downloader(team_url)
            
            # 解析器解析球队页面，获取此球队的所有球员链接
            
            new_urls = self.parser.parser_team_url(team_url,html_cont)
            
            self.urls.add_new_urls(new_urls)
    
            #判断遍历所有球员页面
            while self.urls.has_new_url():
                try:
                    old_urls_len = len(self.urls.old_urls)
     
                    new_url = self.urls.get_new_url() 
                      
                    print ('craw %d : %s' % (old_urls_len,new_url))          
                     
    #                 if old_urls_len >= 2 :
    #                     break;  
                  
                    html_cont = self.downloader.downloader(new_url)
                      
                    new_urls,new_data = self.parser.parser(new_url,html_cont)
                        
                    self.outputer.collect_data(new_data)
                except:
                    print('failed')
                    
            if count == 1:
                print('end')
                break 
            else:      
                count = count + 1
                
                
        self.outputer.output_html()
            

if __name__ == "__main__" :
    root_url = "https://nba.hupu.com/players/rockets"
    obj_spider = SpiderMain()
    obj_spider.carw(root_url)