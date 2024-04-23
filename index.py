import random
import os #ファイル、フォルダのパス取得

def save_score(score,high_score):
    if score > high_score:
        with open("high_score.txt","w") as file:
            file.write(str(score))
        return score
    return high_score

def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt","r") as file:
            return int(file.read())
    else:
        return 0


def game_main():
    player = 1
    score = 0
    high_score = load_high_score()
    obstacle = [random.randint(1,3) for __ in range(20)] #障害物（運尽き）
    
    try:
        while True:
            print("～ CRAP LUCK GAME ～")#クソ運ゲー
            print(f"ハイスコア：{high_score}")
            print(f"スコア：{score}")
            for i in range(1,4):
                if i == player:
                    if i in obstacle[:3]:#始点インデックス
                        print(end=" ")
                    else:
                        print(end=" ")
                else:
                    if i in obstacle[:3]:
                        print(end=" ")
                    else:
                        print("",end=" ")
            print("１,２,３の数字を入力で選択,\"Q\" でゲーム終了します >>")

            obstacle = obstacle[1:] + [random.randint(1,3)]
            move = input()
            if move =="q":
                break
            elif move in["1","2","3"]:
                player = int(move)

            if player in obstacle[:3]:
                print("ゲームオーバー！")
                print("運に見放されました。")
                print(f"スコア：{score}")
                high_score = save_score(score,high_score)
                break
            score += 1

    except:
        print("ゲームを終了します")

game_main()