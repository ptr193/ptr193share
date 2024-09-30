"""
文字游戏
自己用Python做的第一个游戏
"""

#导入区
import random,sys,time

#函数定义区
#物品生成函数
def wp():
    t=0
    wp_sc=[]
    wp_list=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","2","2","2","3","3","3","3","4","4","$"]
    while t<3:
        i=random.choice(wp_list)
        if i=="1":
            wp_sc.append("金币")
        elif i=="2":
            wp_sc.append("闪电技能")
        elif i=="3":
            wp_sc.append("加速技能")
        elif i=="4":
            wp_sc.append("飞行炮")
        else:
            wp_sc.append("外星矿石")
        t +=1
    return wp_sc

#技能选择函数
def cz_01(wp_shc):
    jnb=[]
    print("#################开始################")
    print("请选择一个:",wp_shc)
    jn=str(input("输入中文名称:"))
    if jn in wp_shc:
        jnb.append(jn)
    else:
        print("您没有此技能，请重新输入(也有可能您打错字了)")
    return jnb

#背包函数
def bag_cc(bag):
    jbs=0
    new_bag=[]
    if "金币" in bag:
        for jn_jb in bag:
            if jn_jb=="金币":
                jbs+=1
    jcw="金币"
    for jcwp in bag:
        if jcwp !=jcw:
            new_bag.append(jcwp)
    return jbs,new_bag

#游戏命令行函数
def wd_cmd(fs,newbag):
    ml=input("操作名称:")
    run=True
    if ml=="@#*":
        ml_ts=input("请输入命令:")
        if ml_ts=="分数":
            print(fs)
        elif ml_ts=="背包":
            print(newbag)
        elif ml_ts=="X":
            print("感谢您的使用:)")
            time.sleep(1)
            print("游戏即将关闭……")
            time.sleep(3)
            sys.exit()
        else:
            print("请重新输入。")

#怪物生成函数
def gw_sc():
    pass

#玩家函数
def wj():
    pass

#计时函数
def _time_():
    pass

#游戏开始问好函数
def hello():
    print("欢迎来到我的第一个游戏:)")
    time.sleep(1)
    print("谢谢您的支持:)")
    time.sleep(1)
    print("即将开始游戏:)")
    time.sleep(1)
    print("加载中……")
    time.sleep(1)
    print("………………………………………………………………………………")
    time.sleep(3)

#游戏资料查询函数
def zl_wen():
    yxzl=input("是否要查看游戏资料？(y/n)")
    if yxzl=="y":
        time.sleep(2)
        print("***************************************************")
        print("注:这个游戏没有存档系统！")
        print("游戏背景:你是一个普通的机器人，你现在正在被怪物追赶，现在你正在公路上奔跑……")
        print("游戏规则/操作:每回合系统都会给你三个选项，你要选择其中一个，然后在下一行输入操作。")
        print("金币:加分项；闪电技能:攻击方式，攻击力为5；加速技能:加快逃跑速度；飞行炮:攻击项，攻击力为15；外星矿石:货币/收集物")
        print("在操作区域输入要使用的技能，技能就会自动输出。")
        print("在“$\>”后输入“X”可以关闭游戏。")
        time.sleep(1)
    else:
        time.sleep(2)

#特殊命令行函数
def cmd_ts():
    ml=input("$\>")
    if ml== "X":
        print("感谢您的使用:)")
        time.sleep(1)
        print("游戏即将关闭……")
        time.sleep(3)
        sys.exit()
    else:
        print("################结束#################")
    

#游戏主体函数
def zhuti():
    hello()
    yxzt=input("是否开始游戏？(y/n)")
    if yxzt=="y":
        run=True
    elif yxzt=="n":
        print("感谢您的使用:)")
        time.sleep(1)
        print("游戏即将关闭……")
        time.sleep(3)
        sys.exit()
    else:
        print("对不起，请重新开启游戏。")
        time.sleep(1)
        print("游戏即将关闭……")
        time.sleep(3)
        sys.exit()
    zl_wen()
    while run:
        wp_shc=wp()
        bag=cz_01(wp_shc)
        fs,newbag=bag_cc(bag)
        wd_cmd(fs,newbag)
        gw_sc()
        wj()
        _time_()
        cmd_ts()


#游戏主体
if __name__=="__main__":
    zhuti()


