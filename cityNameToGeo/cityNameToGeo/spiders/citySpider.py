import scrapy
import csv
import os

class CitySpiderGeo(scrapy.Spider):
    name = "citySpider"
    print("   ************* #0# Start Scrapy ************* ")
    cityName = 'تهران'
    start_urls = [
        'http://www.google.com/search?q=' + cityName + '+longitude+and+latitude&aq=t',
    ]

    def csvRead(self):
        with open('cities_iran.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            googleStartUrls=[]
            for row in csv_reader:
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # print(f'\t{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}')
                    line_count += 1
                    googleStartUrls.append("http://www.google.com/search?q=" +row[1]+"+longitude+and+latitude&aq=t")
            print("   ************* #1# cities read ************* ")
            print(f'Processed {line_count} lines.')
            return googleStartUrls


    def parse(self, response):
        # save html of page
        page = response.url.split("/")[-3]
        filename = f'city-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # extract coordinate of city
        n = response.xpath('//div[@class="BNeawe iBp4i AP7Wnd"]/text()').get()
        yield {
            'coordinate': n,
        }
        print("   ************* #2# Coordinate of City ************* ")
        print(n)


