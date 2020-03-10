import Algorithm as MyA
import copy

w = 0
count = 0
count2 = 1

while w < 100000000000:
    x = MyA.X(count)  # X Koordinates
    y = MyA.Y(count)  # Y Koordinates
    MyYon = MyA.Yonler(x, y)  # Yönlerini Bulduk
    # Max 4 Yön olacagından herbirini deniyoruz

    for i in range(4):
        # Sola Döndürür
        if i == 0:
            if MyYon[i] == 1:
                temp0 = copy.deepcopy(MyA.puzzle_BFS_States[count])
                tempDeger1 = 0  # Boş değişkenim (int)
                tempDeger1 = temp0[x][y - 1]  # -1 De
                temp0[x][y] = tempDeger1
                temp0[x][y - 1] = -1
                try:
                    MyA.puzzle_BFS_States.index(temp0)
                except:
                    count2 = count2 + 1
                    MyA.puzzle_BFS_States.append(temp0)
                if MyA.puzzle_Goal_State == temp0:
                    print("--------------------------------------------")
                    print("Çocuk (Deneme Sayısı) : ", count)
                    print(temp0[0][0], temp0[0][1], temp0[0][2])
                    print(temp0[1][0], temp0[1][1], temp0[1][2])
                    print(temp0[2][0], temp0[2][1], temp0[2][2])
                    print("--------------------------------------------")
                    print("BFS_State Eleman Sayısı  :", count2)
                    w = 100000000000
                    break
        # Yukarı Döndürür
        elif i == 1:
            if MyYon[i] == 1:
                temp1 = copy.deepcopy(MyA.puzzle_BFS_States[count])
                tempDeger1 = 0  # Boş değişkenim (int)
                tempDeger1 = temp1[x - 1][y]  # -1 De
                temp1[x][y] = tempDeger1
                temp1[x - 1][y] = -1
                try:
                    MyA.puzzle_BFS_States.index(temp1)
                except:
                    count2 = count2 + 1
                    MyA.puzzle_BFS_States.append(temp1)
                if MyA.puzzle_Goal_State == temp1:
                    print("Çocuk (Deneme Sayısı) : ", count)
                    print("--------------------------------------------")
                    print(temp1[0][0], temp1[0][1], temp1[0][2])
                    print(temp1[1][0], temp1[1][1], temp1[1][2])
                    print(temp1[2][0], temp1[2][1], temp1[2][2])
                    print("--------------------------------------------")
                    print("BFS_State Eleman Sayısı  :", count2)
                    w = 100000000000
                    break
        # Sağa Döndürür
        elif i == 2:
            if MyYon[i] == 1:
                temp2 = copy.deepcopy(MyA.puzzle_BFS_States[count])
                tempDeger1 = 0  # Boş değişkenim (int)
                tempDeger1 = temp2[x][y + 1]  # -1 De
                temp2[x][y] = tempDeger1
                temp2[x][y + 1] = -1
                try:
                    MyA.puzzle_BFS_States.index(temp2)
                except:
                    count2 = count2 + 1
                    MyA.puzzle_BFS_States.append(temp2)
                if MyA.puzzle_Goal_State == temp2:
                    print("--------------------------------------------")
                    print("Çocuk (Deneme Sayısı) : ", count)
                    print(temp2[0][0], temp2[0][1], temp2[0][2])
                    print(temp2[1][0], temp2[1][1], temp2[1][2])
                    print(temp2[2][0], temp2[2][1], temp2[2][2])
                    print("--------------------------------------------")
                    print("BFS_State Eleman Sayısı  :", count2)
                    w = 100000000000
                    break
        # Aşşagıya Döndürür
        elif i == 3:
            if MyYon[i] == 1:
                temp3 = copy.deepcopy(MyA.puzzle_BFS_States[count])
                tempDeger1 = 0  # Boş değişkenim (int)
                tempDeger1 = temp3[x + 1][y]  # -1 De
                temp3[x][y] = tempDeger1
                temp3[x + 1][y] = -1
                try:
                    MyA.puzzle_BFS_States.index(temp3)
                except:
                    count2 = count2 + 1
                    MyA.puzzle_BFS_States.append(temp3)
                if MyA.puzzle_Goal_State == temp3:
                    print("--------------------------------------------")
                    print("Çocuk (Deneme Sayısı) : ", count)
                    print(temp3[0][0], temp3[0][1], temp3[0][2])
                    print(temp3[1][0], temp3[1][1], temp3[1][2])
                    print(temp3[2][0], temp3[2][1], temp3[2][2])
                    print("--------------------------------------------")
                    print("BFS_State Eleman Sayısı  :", count2)
                    w = 100000000000
                    break
    count = count + 1
    if count % 1000 ==0 or count2 % 1000 ==0:
        print("Count (Deneme Sayısı)  :", count)
        print("Count2 (Denek Sayısı)  :", count2)
