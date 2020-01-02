# Project8-2_Garbled_circuit
## Garbled Circuit:
1063514 李晨宇 60%  主程式CODE編譯&電路構圖
1051537 康宇良 40%  嘗試SHA256設計畫電路
## g^x mod p

### 預想路圖
![](https://cdn.discordapp.com/attachments/623345235585662980/637325632283607060/IMG_20191026_002410.jpg)

選用閘:AND OR NOT ｜　XOR(教授建議不要用)
#### 參考工研院Garbled Circuit文章:　https://ictjournal.itri.org.tw/content/Messagess/contents.aspx?PView=1&KeyWord=&SiteID=654246032665636316&MmmID=654304432061644411&SSize=10&MSID=1003030116602767736

g^x mod p 固定為k bit
Garbled circuit 
困難點: 前面處理模運算和指數運算二次方器
比較器(比較大小來弄出前面要的數列
### 試著畫個2bit和3bit的版本
可能要的話就是先弄個and  or  xor  not  gate的function，二進位然後只能兩位數，然後要弄得話應該要剛輸入就建好要得能處理那位數的電路，建立大點的，只是每次跑都會跑到底所以會比較花時間，前面的話就動態，要知道它的規律去建，比較器能疊加使用
然後都一定會是2倍數的數字的比較，2位數就用4位數的比較器(2個2位數比較器然後後面接文中的那樣方式)
#### 比較器參考文章:http://nfudee.nfu.edu.tw/ezfiles/43/1043/img/326/dc17.pdf

### 基數位數的解決方式
4位數+2位數的
然後以此類推
0111>0010
相減
0101
右移
0010
0010=0010(或<0010就結束?)
然後餘數就為1，右移應該k位數最多k-1次吧?那直接生成k層的電路(或用遞迴方式)應該也行<=時餘數補0

### 當天看到P的要求並沒有我們想的這麼簡單->P很大!!!
![](https://cdn.discordapp.com/attachments/623345235585662980/638589759924600832/DSC_2078.JPG)
因為此份比較難完成，教授有另提一個方案SHA256
### SHA256
![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/SHA-2.svg/400px-SHA-2.svg.png)
#### 參考SHA 文章:https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/602774/
![](https://cdn.discordapp.com/attachments/623345235585662980/637331182899429387/unknown.png)
![](https://cdn.discordapp.com/attachments/623345235585662980/637332513131462674/unknown.png)
## 討論
input_key
那當作1-5左邊為0或1(其實就兩種狀態)，gate1部分當作是預先寫好的，gate1~5都是先設好，然後gcircuit那不是1   2   gate1   6嗎?所以gate1出來的
10011101    1
10000011    0
10000011    0
10000011    0
當作是6這樣看，然後後面以此類推，推下去最後狀態會是gate5的output 狀態10

![](https://media.discordapp.net/attachments/623345235585662980/639645138712526858/Screenshot_20191101-100116.png?)

#### 參考隊員提供以前相似作業:https://docs.google.com/document/d/1PfZ-ZYhfhDsEo-5WPRYCVF7TCkz255RyU-HSRpgIv9c/edit?usp=sharing

---
先不管亂數標籤，先建立起來真值表
0   1
0 0   0
1  0    1
貼上標籤
_   a   b
c e   e
d e   f
然後a~f都是亂數貼上，最後使用者要輸入，ad才會有f的輸出
#### 預想電路圖:
![](https://i.imgur.com/vnHcqBE.png)
![](https://i.imgur.com/ArLDfN2.png)
![](https://media.discordapp.net/attachments/623345235585662980/640063659040702464/unknown.png)
#### Input.txt: one wire get two inputs
#### Circuit.txt: simulate the circuit work X Y AND Z
>X=>wire1 
Y=>wire2 
Z=>Gate's output

Gate 串接想法參考:https://youtu.be/jkHc2-4cu4E
參考文章:https://blog.csdn.net/Black_BearB/article/details/81228578


