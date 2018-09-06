# encoding=utf8

# xml解析 dom sax

from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element:%s, attrs:%s' %(name, attrs))

    def end_element(self, name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)



# 练习：请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：


class WeatherSaxHandler(object):
    weather={'city':'', 'forecast':[]}
    def start_element(self, name, attrs):
        print('sax:start_element:%s, attrs:%s' %(name, attrs))
        if name=='yweather:location':
            self.weather['city']=attrs['city']
        if name =='yweather:forecast':
            self.weather['forecast'].append({'date':attrs['date'], 'day':attrs['day'], 'high':attrs['high'], 'low':attrs['low']})


class WeatherQuery(object):
    # woeid 城市名称
    def __init__(self, woeid):
        self.woeid = woeid
        self.api='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%#&format=xml'
        self.data = ''
        self.weather = ''

    def __query__(self):
        url = self.api.replace('#',self.woeid)
        print('URL: %s' % url)
        req = request.Request(url)
        with request.urlopen(req) as f:
            print('Status:', f.status, f.reason)
            self.data = f.read().decode('UTF-8')
            print('Response data : ', self.data)


    def __parseXml__(self):
        handler = WeatherSaxHandler()
        weatherParser = ParserCreate()
        weatherParser.StartElementHandler = handler.start_element
        weatherParser.Parse(self.data)
        self.weather = handler.weather;

    def show(self):
        self.__query__()
        self.__parseXml__()
        print('weather result:\n %s\n' % self.weather)

print('\nBegin:=====================================')
beijing_weather = WeatherQuery('202141331')
beijing_weather.show()
print('End:=======================================')






















