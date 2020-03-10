import copy

puzzle_initial_state = [[2, 8, 3],
                        [1, 6, 4],
                        [7, -1, 5]]
#Amaç
puzzle_Goal_State = [[1, 2, 3],
                     [8, -1, 4],
                     [7, 6, 5]]
#Basamaklar İlk Basamak initail States (Başlangıç basamagı)
puzzle_BFS_States = copy.deepcopy([puzzle_initial_state])
#Değişecek Elemanın X sini bulur
def X(state):
    for x in range(3):
        for y in range(3):
            if puzzle_BFS_States[state][x][y] == -1:
                return x
#Değişecek Elemanın Y sini bulur
def Y(state):
    for x in range(3):
        for y in range(3):
            if puzzle_BFS_States[state][x][y] == -1:
                return y
#Koordinatları bulunan X,Y Deki elemanın hangi yöne gidebileceğini bulur
def Yonler(x, y):
    if (x < 3 and y < 3) and (x >= 0 and y >= 0):
        yon = [0, 0, 0, 0, 0]
        # 1  y == 1 or y == 2  ===> sayi sola swap yapabilir
        # 2  x == 1 or x == 2  ===> sayi yukari swap yapabilir

        # 3  y == 0 or y == 1  ===> sayi sağ swap yapabilir
        # 4  x == 0 or x == 1  ===> sayi assa swap yapabilir
        if (y == 1 or y == 2):
            yon[0] = 1  # Sola
            yon[4] = yon[4] + 1
        else:
            yon[0] = -1

        if (x == 1 or x == 2):
            yon[1] = 1  # Yukarıya
            yon[4] = yon[4] + 1
        else:
            yon[1] = -1

        if (y == 0 or y == 1):
            yon[2] = 1  # Sağa
            yon[4] = yon[4] + 1
        else:
            yon[2] = -1

        if (x == 0 or x == 1):
            yon[3] = 1  # Aşşagıya
            yon[4] = yon[4] + 1
        else:
            yon[3] = -1

        return yon
    else:
        return print("Girilen indis 3x3 lük matrisin dışındadır!")
