# -*- coding:utf-8 -*-
import urllib


class HtmlDownload(object):
    
    
    def downloader(self,url):
        if url is None :
            return
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200 :
            return
    
        return response.read().decode('utf-8')


