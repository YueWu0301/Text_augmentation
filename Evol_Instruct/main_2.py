import json
import random

from openai_access import call_chatgpt
# from depth import createConstraintsPrompt, createDeepenPrompt, createConcretizingPrompt, createReasoningPrompt
from depth import createDataPrompt , createExamplePrompt
from trans import transtyle , transtructure
from breadth import createBreadthPrompt
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# fr = open('alpaca_data_cleaned.json','r')
# all_objs = json.load(fr)



def getevolprompt(instruction, type):
    """
    输入instruction 以及增广类型
    返回变换之后的文字
    
    """
    if type=='example' :
        return createExamplePrompt(instruction)
    elif type == 'data':
        return createDataPrompt(instruction)
    elif type == 'style':
        return transtyle(instruction)
    elif type == 'structure' :
        return transtructure(instruction)
    elif type == 'bread' :
        return createBreadthPrompt(instruction)
    else:
        print('use con,deep,concret,reason,bread plz')


def augment(types, num, instruction):
    """
    输入增广选择types 增广数量 num  要增广的 instruction
    返回一个list 里边是增广结果
    """
    evol_objs = []
    for i in range(0,num):
        print(i)
        type = random.choice(types)
        selected_evol_prompt = getevolprompt(instruction , type)
        evol_instruction = call_chatgpt(selected_evol_prompt)
        evol_objs.append({"type":type,"evol_prompt":evol_instruction})
    return evol_objs

one_1 = '优点：爱学习，看书，1000~2000本书，90%都看过。市场，销售财务。看书比较杂，人文。国家形式，全球的形式\
1. 对商业的趋势判断，很感兴趣。\
2. 安静的时候，能量更大。\
----中----\
多把学到应用出来，不能再看书了。要开始读无字书（人）\
卢总前两-三年都是在反腐，我管辖范围内也有出问题的。\
---待提升---\
心理素质：有时候沉不住气\
更喜欢一个人待着'

one_3 = '动力：赚钱永远赚不够。但是得给孩子做榜样。孩子明年高考，我不能躺平。领导表扬我，我就敢挑战更大的任务。等孩子考完大学吧。干一天就好好干。\
未来：孩子大学毕业后，就退居二线'

four_1_1 = '现在要求更高，消费者体验。今年要求物流更高。\
今年也在招聘人做统筹，李胜、肖千等都是从各地挖来的。用比自己高的人，大家三观正，能力强。\
今年降本增效3个亿，得支持销售才能做下去。\
定目标时，去年节约1个亿，李军说也1个亿，温总给加6000w,利清说还有6000w的员工奖励，员工待遇不能降，我加了2个亿。\
---规划---\
1. 精益生产，以工厂为主的降本增效。\
2. 物流的降本增效\
3. 争取优惠政策。\
eg：去年7000万，今年6000万，剩下的靠供应链的协同。靠集团采购，把材料轻量化，一瓶降1分钱。4000-5000万\
\
供应链的协同：分仓协同，今年要求新物流共享公用，鲜奶、奶酪，都整合。线路上重新布局。\
加工地停工部分工厂：关掉部分，重新规划地点。eg：怀柔工厂，就移到浙江金华。等等，全年关掉3个工厂。\
重新规划资产的有效性。\
武汉新工厂，借用达能墨西哥工厂的2.0版本。T字形，可灵活扩产。工厂把友芝友合并了。节省5000万\
新建了一个职能制造3.5版本的工厂\
今年时候利润年，不能承诺过高，又做不到。\
优惠政策：跟政府预计要4000w，实际打算要1个亿。\
结果：1季度，供应链比目标完成多出1500w。结果李军看能完成就又拉高。'

four_1_1_5 = '俄罗斯跟乌克兰打架，石油价格涨了。产品涨价，伊利涨，行业在涨。'

four_1_2 = '我从伊利过来，原来做包头的生产总经理，原来说有事情不敢做决定，现在好很多，及早决策，原来追求完美，现在追求效率（抓住机会）。eg:跟质量同事说，产品要抓时机。\
---------------\
分任务的时候，没把压力都传导给下属，剩下的我抗。\
李军要涨任务目标，我没同意。'

four_2_1 = '以前搞企业的注重时效，要直接面对面的交流。时间长的能接受，短的不一定能接受。在调整中。\
没有完美的个人，只有能力上的互补。原来要求完美，觉得人家这里不对，哪里也不对，现在要求牛人绽放。我的价值观也要做调整。\
---管理方向---\
1. 年轻化\
2. 性别比例，女性要变多'

four_2_1_5 = '团队很稳定，带着团队去达能墨西哥、俄罗斯的先进工厂。达能的达瓦之路，鲜奶的人都是从低温出的。能输送的人，赶紧送，超过40岁会有职业倦怠期。我想把年轻人提拔上来了。\
目标翻3倍，绩效工资完成了，只挣工资，任务自己领，谁的贡献大，谁的奖金多。\
过去五年都是A和S，靠的是流程、体系。我们通过管理和技术要效益。\
To 团队：去年1个亿，今年再定1个亿，别人不佩服你。但是今年3个亿，虽败犹荣。带领大家总结方法。大家慌了一段时间，就稳定下来了。\
物流只定了3000w，原本要求65000w。承运商，用时间换利润，签了降4%的合同，能完成4000w。常温等等都涨了。\
-----团队的吐槽----\
太支持市场和销售，什么都敢接，什么都干上，预算推翻重来也接。\
'


four_3_1 = '抓着下属给自己提建议。强制提建议。'


four_4_1 = '干一天就就全力以赴，书在家看。原来在伊利的副总，觉得价值观不一致，来了蒙牛。把自己的团队带好。\
疫情：派鲜奶多，酸奶少派，我派去物流的总监，全国每个工厂抽调两个人去支援上海。在问题面前，我们是一个蒙牛。完不成100%，但能完成80-90%'

four_5_1 = '每个职能横向都有群。'

num = 100

text_list = [one_1,one_3,  four_1_1, four_1_1_5, four_1_2, four_2_1, four_2_1_5,four_3_1, four_4_1, four_5_1]
name_list = ['one_1','one_3',  'four_1_1', 'four_1_1_5', 'four_1_2', 'four_2_1', 'four_2_1_5','four_3_1', 'four_4_1', 'four_5_1']

# for index,text in enumerate(text_list):
#     aug = augment(types=['style','structure','bread'],num=num, instruction=text)
#     with open(f'result_1/{name_list[index]}.json', 'w', encoding='utf-8') as f:
#         json.dump(aug, f, ensure_ascii=False, indent=4)
#     print(f'{index}/{num}')    

def process_task(index, text):
    aug = augment(types=['style', 'structure', 'bread'], num=num, instruction=text)
    file_path = f'result_2/{name_list[index]}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(aug, f, ensure_ascii=False, indent=4)
    print(f'{index}/{len(text_list) - 1}')

# 使用 ThreadPoolExecutor 并行执行任务
with ThreadPoolExecutor() as executor:
    # 提交所有任务
    futures = {executor.submit(process_task, index, text): index for index, text in enumerate(text_list)}
    # 等待所有任务完成
    for future in as_completed(futures):
        future.result()  # 检查任务是否引发异常