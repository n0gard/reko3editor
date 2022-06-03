juntuan_map = {
    0x80: '劉備', 0x81: '曹操', 0x82: '孫權', 0x83: '公孫瓚',
    0x84: '袁紹', 0x85: '董卓', 0x86: '袁術', 0x87: '呂布',
    0x88: '陶謙', 0x89: '劉表', 0x8A: '劉璋', 0x8B: '張魯',
    0x8C: '馬騰', 0x8D: '孔融', 0x8E: '無屬',
}

trigger_descr = {
    0x00: '顺序执行',
    0x01: '分支执行',
    0x02: '进入城市建筑',
    0x03: '对话',
    0x04: '单挑',
    0x05: '进入城市',
    0x06: '战场移到点',
    0x07: '战斗胜利',
    0x08: '战斗失败',
    0x09: '指定回合',
    0x0A: '未知',
    0x0B: '战场移到区域',
    0x0C: '撤退',
}

code_step = {
    0x00: {'plen': 2, 'descr': '显示带人物头像的系列对话'},
    0x01: {'plen': 5, 'descr': '指定人物在剧情场景的行动'},
    0x02: {'plen': 1, 'descr': '未知'},
    0x03: {'plen': 11 + 30 * 9, 'descr': '部署我军部队'},
    0x04: {'plen': 0, 'descr': '未知'},
    0x05: {'plen': 0, 'descr': '显示当前场景'},
    0x06: {'plen': 0, 'descr': '未知'},
    0x07: {'plen': 2, 'descr': '显示图片'},
    0x08: {'plen': 2, 'descr': '在屏幕中央显示多行信息'},
    0x09: {'plen': 2, 'descr': '指定战场/场景/大地图'},
    0x0A: {'plen': 5, 'descr': '部署非战斗模式中的人物'},
    0x0B: {'plen': 2, 'descr': '在画面中心显示信息'},
    0x0C: {'plen': 4, 'descr': '未知'},
    0x0D: {'plen': 2, 'descr': '在画面左下角框中显示信息'},
    0x0E: {'plen': 2, 'descr': '在画面中央显示信息'},
    0x0F: {'plen': 1, 'descr': '重新读入本章本节某段剧本指令'},
    0x10: {'plen': 4, 'descr': '武将单挑'},
    0x11: {'plen': 2, 'descr': '切换到地图/场景/战场'},
    0x12: {'plen': 0, 'descr': '本章结束'},
    0x13: {'plen': 0, 'descr': '段指令强制结束'},
    0x14: {'plen': 2, 'descr': '设置事件开关'},
    0x15: {'plen': 2, 'descr': '是否出战的对话框显示'},
    0x16: {'plen': 4, 'descr': '未知'},
    0x17: {'plen': 1, 'descr': '剧情模式开关'},
    0x18: {'plen': 2, 'descr': '人物消失、部队撤退'},
    0x19: {'plen': 0, 'descr': '未知'},
    0x1A: {'plen': 2, 'descr': '援军出现'},
    0x1B: {'plen': 1, 'descr': '获得道具'},
    0x1C: {'plen': 5, 'descr': '改变人物AI'},
    0x1D: {'plen': 4, 'descr': '未知'},
    0x1E: {'plen': 0, 'descr': '未知'},
    0x1F: {'plen': 0, 'descr': '未知'},
    0x20: {'plen': 99, 'descr': '子指令数目'},
    0x21: {'plen': 99, 'descr': '检查事件是否触发'},
    0x22: {'plen': 1 + 30 * 13, 'descr': '部署敌军'},
    0x23: {'plen': 0, 'descr': '选择我军出战部队'},
    0x24: {'plen': 3, 'descr': '修改武将阵营'},
    0x25: {'plen': 2, 'descr': '显示决定供选择'},
    0x26: {'plen': 3, 'descr': '改变战场地形'},
    0x27: {'plen': 3, 'descr': '放火或放水'},
    0x28: {'plen': 3, 'descr': '战场改变武将阵营'},
    0x29: {'plen': 0, 'descr': '游戏失败'},
    0x2A: {'plen': 1, 'descr': '显示游戏结局'},
    0x2B: {'plen': 3, 'descr': '给予黄金/残存部队获得经验'},
    0x2C: {'plen': 0, 'descr': '未知'},
    0x2D: {'plen': 2, 'descr': '兵力士气减半'},
    0x2E: {'plen': 5, 'descr': '切换所在城市'},
    0x2F: {'plen': 3, 'descr': '修改人物未知属性'},
    0x30: {'plen': 2, 'descr': '显示目标（剧情目标或战斗目标）'},
    0x31: {'plen': 0, 'descr': '与道具屋有关，废弃指令'},
    0x32: {'plen': 1, 'descr': '设置道具屋贩卖物品，废弃指令'},
    0x33: {'plen': 0, 'descr': '关闭单挑动画'},
    0x34: {'plen': 0, 'descr': '开启单挑动画'},
    0x35: {'plen': 3, 'descr': '单挑动画'},
    0x36: {'plen': 0, 'descr': '切换到战斗模式'},
    0x37: {'plen': 3, 'descr': '未知'},
    0x38: {'plen': 1, 'descr': '播放游戏音乐'},
    0x39: {'plen': 3, 'descr': '人物等级上升'},
    0x3A: {'plen': 3, 'descr': '改变人物兵种'},
    0x3B: {'plen': 2, 'descr': '重新定位场景位置'},
    0x3C: {'plen': 2, 'descr': '定位军团'},
    0x3D: {'plen': 1, 'descr': '一般存盘/战场存盘'},
    0xFF: {'plen': 0, 'descr': '本段指令结束'},
}

build_list = {
    0x00: '宫殿', 0x01: '宫殿', 0x02: '议事厅', 0x03: '议事厅',
    0x04: '议事厅', 0x05: '议事厅', 0x06: '集会所', 0x07: '酒馆',
    0x08: '官邸', 0x09: '集会所', 0x0A: '？', 0x0B: '？',
    0x0C: '庭院', 0x0D: '官邸', 0x0E: '营帐', 0x0F: '营帐',
    0x10: '营帐', 0x11: '陈留', 0x12: '官邸', 0x13: '？',
    0x14: '茅庐', 0x15: '草庐', 0x16: '陶谦官邸',
}

ai_type_descr = {
    0x00: '原地警戒(攻击)',
    0x01: '主动出击',
    0x02: '原地待命',
    0x03: '主动攻击仇人',
    0x04: '移动到坐标(攻击)',
    0x05: '襄阳II关羽消灭曹仁',
    0x06: '移动到坐标(不攻击)',
    0x07: '这是什么AI？',
}