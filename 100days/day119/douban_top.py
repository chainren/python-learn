"""
练习： 抓取豆瓣电影评分top250
所需要获取的信息如下：名称，导演，国家，链接，上映时间，类型，评分（五星，四星占比）以及评价人数
"""

import requests
import re
import bs4


# 生成top250url地址
def getUrls():
    url_init = 'https://movie.douban.com/top250?start={0}&filter='
    urls = [url_init.format(index*25) for index in range(10)]
    return urls


# 获取网页
def get_page_html(url):
    headers = {
        'Referer': 'https://movie.douban.com/chart',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException as e:
        print('request fail.url:%s, exception:%s' % (url, e))
        return None


# 从html中解析出电影详情页url
def get_movie_url(html):
    if html is None:
        return None
    ans = []
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.select('li > div.item')
    for item in items:
        href = item.select('div.info > div.hd > a')[0]['href']
        ans.append(href)
    return ans


# 解析详情页
def get_movie_info(url):
    if url is None:
        return None
    html = get_page_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    content = soup.find('div', id='content')

    # 电影名称
    title = content.find('span', property='v:itemreviewed').text
    # 年份
    year = content.find('span', property='year')
    # 导演
    directors = content.find('span', class_='attrs').find_all('a')

    director = []

    for i in range(len(directors)):
        director.append(directors[i].text)

    # 上映国家/地区
    country = content.find(text=re.compile('制片国家/地区')).next_element

    # 类型
    typeList = content.find_all('span', property='v:genre')

    # 影片类型
    types = []
    for obj in typeList:
        types.append(obj.text)

    # 评分
    average = content.find('strong', property='v:average').text

    # 评价人数
    votes = content.find('span', property='v:votes').text

    # 具体评分（五星 四星人数占比）
    rating_per_items = content.find(
        'div', class_='ratings-on-weight').find_all('div', class_='item')
    rating_per = [rating_per_items[0].find('span', class_='rating_per').text,
                  rating_per_items[1].find('span', class_='rating_per').text]

    return {
        'title': title,
        'url': url,
        'director': director,
        'country': country,
        'year': year,
        'type': type,
        'average': average,
        'votes': votes,
        'rating_per': rating_per
    }


def wirte_to_file(details):
    file_name = 'doubanTop250.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        for detail in details:
            if detail is None:
                continue
            f.write(str(detail)+'\n')


if __name__ == '__main__':
    list_htmls = [get_page_html(url) for url in getUrls()]
    movie_urls = []
    for html in list_htmls:
        urls = get_movie_url(html)
        if len(urls) > 0:
            movie_urls.extend(urls)
    movie_details = [get_movie_info(url) for url in movie_urls]
    wirte_to_file(movie_details)
