#스포츠 뉴스 정보 크롤링 하기

## 크롤링을 하기전에..
크롤링의 정의 및 크롤링에 대한 규약을 인식하고 크롤링을 시작하는 것이 바람직하다.
- [웹 크롤러](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)
- [로봇 배제 표준(robot.txt)](https://ko.wikipedia.org/wiki/%EB%A1%9C%EB%B4%87_%EB%B0%B0%EC%A0%9C_%ED%91%9C%EC%A4%80)

## 크롤링 대상(스포츠뉴스 포탈) 선택
- [다음 스포츠뉴스 - robost.txt](http://media.daum.net/robots.txt)
- [네이버 스포츠뉴스 - robots.txt](http://sports.news.naver.com/robots.txt)
- [네이트 스포츠뉴스 - robots.txt](http://sports.news.nate.com/robots.txt)

robots.txt의 규약에 대하여 다음 스포츠 뉴스가 크롤링하기에 적합하여 선택을 하였다.

## 선택된 크롤링 URI
`http://media.daum.net/breakingnews/sports`


## scrapy 다운로드
[scrapy 다운로드](https://docs.scrapy.org/en/latest/intro/install.html#installing-scrapy)
```
아래의 패키지는 scrapy에 대한 dependency이다. 
document에도 내용이며, 최소(버전)을 맞춰 줘야 설치가 가능하다.
```
```
터미널 에서 pip 사용시 
(sudo) pip install pyOpenSSL==1.xxx 식으로 버전변경을 하면 된다. 
```
- Twisted 14.0 
- lxml 3.4
- pyOpenSSL 0.14


## mongoDB 설치
- [mongoDB install](https://docs.mongodb.com/manual/administration/install-community)

## mongodb Client
- [robomongo](https://robomongo.org)
- [인텔리J 플러그인](https://plugins.jetbrains.com/plugin/7141-mongo-plugin)


## 실행
```
scrapy crawl sportsNewsCrawl
```

