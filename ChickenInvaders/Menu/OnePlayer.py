import pygame
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
from ChickenInvaders.Menu.Collide import collide
import ChickenInvaders.level.Level1 as Lv1
import ChickenInvaders.level.Level2 as Lv2
import ChickenInvaders.level.Level3 as Lv3



import random


def oneplayer():
    current_level = 1  # Đây là màn chơi hiện tại

    while True:
        if current_level == 1:
            Lv1.Level1()
        # Sau khi kết thúc màn chơi hiện tại, kiểm tra điều kiện để chuyển sang màn chơi mới
            if Lv1.get_lives() > 0:  # Hoặc bất kỳ điều kiện nào bạn muốn áp dụng
                current_level += 1  # Chuyển sang màn chơi mới

                if current_level == 2:
                    Lv2.Level2()

                    if Lv2.get_lives() > 0:  # Hoặc bất kỳ điều kiện nào bạn muốn áp dụng
                        current_level += 1

                        if current_level == 3:
                            Lv3.Level3()
                            break
                        else:
                            break
                else:
                    break
            else:
                break
        else:
            # Nếu đã qua hết các màn chơi, bạn có thể thực hiện các hành động khác ở đây
            pass



