# -*- coding:utf-8 -*-

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self ,data):
        if data is None :
            return
        self.datas.append(data)
        
    
    
    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<ul>')
            
        for data in self.datas :
            fout.write('<li>%s - %s</li>' % (data['player_name'],data['player_team']))
#             fout.write('<li>%s</li>' % data['player_team'])
#             fout.write('<li>%s</li>' % data['player_score'])
                
        fout.write('</ul>')
        fout.write('</body>')
        fout.write('</html>')

