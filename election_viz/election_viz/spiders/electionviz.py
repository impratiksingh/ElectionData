# -*- coding: utf-8 -*-
import scrapy


class ElectionvizSpider(scrapy.Spider):
    name = 'electionviz'
    

    #2004
    # allowed_domains = ['myneta.info/loksabha2004/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']
    # start_urls = ['http://myneta.info/loksabha2004/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']

    #2009
    # allowed_domains = ['myneta.info/ls2009/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']
    # start_urls = ['http://myneta.info/ls2009/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']

    #2014
    # allowed_domains = ['myneta.info/ls2014/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']
    # start_urls = ['http://myneta.info/ls2014/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']

    # 2019
    #allowed_domains = ['myneta.info/LokSabha2019/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary']
    #start_urls = ['http://myneta.info/LokSabha2019/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary/']

    # 2019 Winners Only
    allowed_domains = ['myneta.info/LokSabha2019/index.php?action=summary&subAction=winner_analyzed&sort=candidate#summary']
    start_urls = ['http://myneta.info/LokSabha2019/index.php?action=summary&subAction=winner_analyzed&sort=candidate#summary']

    
    
    def parse(self, response):
    	rows=response.xpath('//table')[2].xpath('.//tr')
    	for row in rows[2:]:
    		#td=row.xpath('.//td/text()').extract()
    		#print(td)
    		sno=row.xpath('.//td[1]/text()').extract()
    		candidate=row.xpath('.//td[2]/a/text()').extract()
    		constituency=row.xpath('.//td[3]/text()').extract()
    		party=row.xpath('.//td[4]/text()').extract()
    		cases=row.xpath('.//td[5]/span/text()').extract()
    		print('Cases is : ',cases)
    		education=row.xpath('.//td[6]/text()').extract()
    		asset=row.xpath('.//td[7]/text()').extract()
    		liabilities=row.xpath('.//td[8]/text()').extract()

    		yield {
    		'SerialNo':sno,
    		'Candidate':candidate,
    		'Constituency':constituency,
    		'Party':party,
    		'CriminalCases':cases,
    		'Education':education,
    		'Assest':asset,
    		'Liabilities':liabilities
    		}

    		
        
