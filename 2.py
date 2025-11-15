a, b, c, x = map(int,input().split())

if x % a == 0:
    print("Tanjiro menggunakan jurus pertama")

elif x % b == 0:
    print("Tanjiro menggunakan jurus kedua")

elif x % c == 0:
    print("Tanjiro menggunakan jurus ketiga")

else:
    print("Tanjiro tidak bisa mengalahkan Iblis Halilintar")