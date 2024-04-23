import requests
import json
from time import sleep
from LineBot.models import Product
from LineBot.line import line_notify

class WeverseShopSpider():
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
        }
    def getProductDetail(self, token):
            """ 
            商品詳情
            :saleId: 商品Id
            :artistsId:藝人Id
            :return product_detail: requests 商品詳細資料
            """

            s = requests.Session()
            url = f'https://shop.weverse.io/{token}'
            r = s.get(url, headers=self.headers)
    
            if r.status_code != requests.codes.ok:
                print('找不到該商品！', r.status_code)
                return

            saleId = r.json()['pageProps']['$dehydratedState']['queries'][3]['state']['data']['saleId']
            artistId = r.json()['pageProps']['$dehydratedState']['queries'][3]['state']['data']['labelArtistId']
            status = r.json()['pageProps']['$dehydratedState']['queries'][3]['state']['data']['status']
            name = r.json()['pageProps']['$dehydratedState']['queries'][3]['state']['data']['name']
            url = f'https://shop.weverse.io/zh-tw/shop/GL_USD/artists/{artistId}/sales/{saleId}'
            
            return saleId, artistId, name, status, url

if __name__ == '__main__':
    WeverseShop_Spider = WeverseShopSpider()

#範例商品(每10秒爬一次)

while True:
    WeverseShop_Spider = WeverseShopSpider()
    saleId, artistId, name, status, url = WeverseShop_Spider.getProductDetail('_next/data/3ovDOeFNl2plwxAo2s8Rm/zh-tw/shop/GL_USD/artists/7/sales/13690.json?shopAndCurrency=GL_USD&artistId=7&saleId=13690')
    if not Product.objects(SaleId=str(saleId)):
        task = Product(SaleId= str(saleId), ArtistId=str(artistId), Name=name, Status=status)
        task.save() 
    else:
        result = Product.objects.get(SaleId=str(saleId))
        tempStatus = result.Status
        #上一次爬到的貨況不等於本次爬到的貨況時，根據貨況改變的條件發LINE通知
        if result.TempStatus != "" and result.TempStatus != status :
            if status == 'SOLD_OUT':
                line_notify('喔哦！商品：'+ name +'已經售完囉:(\n'+ url)
            elif status == 'SALE':
                line_notify('商品：'+ name +'已補貨！趕快去購買吧～\n'+ url)
            elif status == 'STOP':
                line_notify('喔不！商品：'+ name +'已停止販售:('+ url)
            else:
                line_notify('商品貨況不明！')

        Product.objects(SaleId=str(saleId)).update_one(TempStatus=tempStatus, Status=status)
        print('商品名稱：', name, '商品狀態：', status, '網址:', url)

    sleep(600)