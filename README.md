# Python網頁爬蟲結合Line Notify通知小練習

使用Python的DJango框架，進行Weverse Shop指定商品頁面的爬蟲，<br>
當商品貨況改變時，就使用Line Notify發送貨況通知。<br><br>

目前為初始版本，只是做來自己使用，可能會有部分BUG，且爬蟲的網頁目前寫死為SEVENTEEN手燈網頁。<br>
因為已經超過一個月都等不到手燈捕貨，懶得三不五時手動去確認捕貨了沒，<br>
所以做了一個讓LINE BOT，每10分鐘爬一次商品網頁，當手燈補貨/售完時主動通知我～<br>
<br><br>
* 補貨通知<br>
  <img src="https://github.com/WanJanChen/WeverseRestockNotification/blob/main/image/sale.jpg" height="786px" width="500px" />
  <br>
* 商品售罄通知<br>
  <img src="https://github.com/WanJanChen/WeverseRestockNotification/blob/main/image/soldout.jpg" height="786px" width="500px" />
  <br><br>
後續可能會再進行功能增修。
<br><br>
-WJ
