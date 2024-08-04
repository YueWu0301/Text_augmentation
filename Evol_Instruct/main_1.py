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


all_objs = []
str1 = '优点：爱学习，看书，1000~2000本书，90%都看过。市场，销售财务。看书比较杂，人文。国家形式，全球的形式\
1. 对商业的趋势判断，很感兴趣。\
2. 安静的时候，能量更大。\
----中----\
多把学到应用出来，不能再看书了。要开始读无字书（人）\
卢总前两-三年都是在反腐，我管辖范围内也有出问题的。\
---待提升---\
心理素质：有时候沉不住气\
更喜欢一个人待着\
'
# str2 = '19年5月到粤海大区，做交接和市场调研面临一些问题，从粤海过往销售来讲，挑战比较大，业绩完成困难，业绩达成，费用预算超支。在两年间，保障业绩的达成，来的时候30多亿，现在是53亿，明年第三，2025有希望成为规模第一的大区。我们还有一项艰巨的任务，大区经营上，我们预算缺口有1.6个亿，通过3年时间，各方面整合资源，实现业绩的同时，补平预算缺口。分子公司的经营管理，粤海过去是10家分子公司，实现利润指标，20年疫情对直营业务挑战较大，21年分子公司能实现年度预算，利润的部分。这几年的扭亏的额度比较大，亏损2000万，去年扭转。海南2000万亏损，结合海南自贸港的政策，把以前的分公司关掉，成立新的分公司，节约中后台成本，利用海南返税的政策。实现有盈利。\
# 深圳市场，以前公司投资22个点到15个点，节约了大量的费用投资。\
# 有点：长期坚持，大区经理做了十多年，依然保持一份积极正能量心态，激情和活力。\
# 待发展：突破认知边界，更加能够激进式创新。\
# '
all_objs.append(str1)
# all_objs.append(str2)


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

one_1 = '19年5月到粤海大区，做交接和市场调研面临一些问题，从粤海过往销售来讲，挑战比较大，业绩完成困难，业绩达成，费用预算超支。\
在两年间，保障业绩的达成，来的时候30多亿，现在是53亿，明年第三，2025有希望成为规模第一的大区。我们还有一项艰巨的任务，大区经营上，我们预算缺口有1.6个亿，通过3年时间，各方面整合资源，实现业绩的同时，补平预算缺口。\
分子公司的经营管理，粤海过去是10家分子公司，实现利润指标，20年疫情对直营业务挑战较大，21年分子公司能实现年度预算，利润的部分。这几年的扭亏的额度比较大，亏损2000万，去年扭转。海南2000万亏损，结合海南自贸港的政策，把以前的分公司关掉，成立新的分公司，节约中后台成本，利用海南返税的政策。实现有盈利。\
深圳市场，以前公司投资22个点到15个点，节约了大量的费用投资。\
有点：长期坚持，大区经理做了十多年，依然保持一份积极正能量心态，激情和活力。\
待发展：突破认知边界，更加能够激进式创新。'

four_1_1 = '市场差异：市场容量差异很大，广东乳制品接近200亿，云贵广80亿。把所有销售策略符合每个地级市，县城。云南广西贵州三个省不一样，符合当地。广东业务主要构成珠三角，占60%人口，70%的经济，深圳和广州大的市场贡献50%的生意，聚焦核心城市。聚焦核心产品，特仑苏小醇这些产品，业绩增长非常可观。特仑苏排名第一单品，全国特仑苏销售全国第一。深圳份额超越竞聘，广州份额超越竞聘，带来粘性优势。把广州深圳份额提升明显。就有谈判话语权，和市场溢价空间和带货能力。云贵广比较欠缺奶源和货源，18年再云南建立工厂。广东也需要增加产能，再清远建立第二个工厂。广东需要建立研发中心，深圳平均年龄33多，全国最年轻的城市。\
22年挑战：1、22年完成53亿的指标是没问题的，再完成业绩的同时，今年深圳对竞争对手整体的超越。传统渠道还有一点差距。广州今年份额缩小在5个点。2、每个城市份额的突破。市场客户布局，完成市场开发，所有县城，乡镇，开发一级客户60-100个，疫情持续，现在行业零售大环境，经济发展挑战和需求收缩利润的变窄，对开发客户今年会造成一定困难，3、经营上，每家分子公司都能实现盈利。\
城市份额突破：产品聚焦，发挥他的功能和价值，特仑苏还有增长空间。传统渠道，产品小纯奶份额贡献，传统渠道网络搭建。持续推城市店仓销售模式，做到了500个店仓，11万个售点，今年实现15万个售点。营养生活家自建店业务，有81家，五一突破100家。中秋节突破200家。对竞争对手造成比较大的竞争和抢夺。\
'

four_1_2 = '业绩的驱动，合作伙伴经销商有盈利的能力。必须要接入到合作伙伴和经销商经营里。要求团队去关注'

four_2_1 = '弱势区域：增加了CBU业务的布局，品来布局，同时CBU业务选拔一些年轻人上来，在机会品类，儿童奶各个企业关注不多，广东人口多，出生率高。 质量和市场秩序调整到直接管理，面对不确定性，质量食品安全还是很有风险，这个很重要。运营和行销做整合，让目标资源更加高效快速协同。把业务重心放到一线，大区销售支持服务适当优化和精简。'

four_2_2 = '业绩的驱动，合作伙伴经销商有盈利的能力。必须要接入到合作伙伴和经销商经营里。要求团队去关注。追求事业和人生目标，好行业和好企业，好区域，有不一样的文化和使命。团队会对比，感受到团队越来越好。人会珍惜现在的工作和平台。日常的沟通上，给大家发信息分享，行业的动态和公司的政策。管理者以身作则。'

four_2_3 = '人才选拔多元一点，从全国范围选拔人才。北方南方都有。行销经理朱涛，比我小一点86年的，几年历练，多次轮岗。未来作为接班人培养，再输出一个区域的负责人。大区经理最好干过运营和分子公司经理。考虑事情就不全面，容易偏激，单一。'

four_3_1 = '有些事情必须自己做亲历亲为，有些能授权的授权下去，混沌课程学习。优秀企业的参访交流。\
不熟悉的领域，财务管理这方面，到粤海工作后，大区层面面临预算的缺口。分子公司，财务团队共同学习，再财务和经营管理，司马咨询，做阿米巴经营公司。共同学习探讨。品牌管理上，过去不是很关注，广东工作这几年市场和品牌有科学方法，舰长有品牌管理方面课程，通过市场走访，建立认知和意识'

four_3_2 = '费用花费高，价格水平低，市场秩序不好，19来了以后，上了一个市场秩序经理。大力度抓市场秩序的治理。市场秩序管好了以后，窜货很少发生，各地价格得到保护。渠道商有利差，经营结果有帮助。过程中少发费用。特仑苏产品，一个月卖500万箱，中间价格上浮2块钱，多了1000万毛利，一年一个亿毛利，如果下调1块钱，一个月少了1000的渠道利润，一年一个亿就没有了。管秩序管价格。来自于内部挑战，管窜货以前窜货的经销商，销量有虚假的成分，我们就要去调研，是否有虚假，虚假程度有多少去核实，给适当的调整。我们根据他的人口，经济水平，市场网点测算正常销售，能卖多少。根据和竞争对手份额，应该卖多少，有个合理的值。这个地区正常销1000万，实际他买了1500万。而不是一味的看过去的数据。把虚假成分挤掉。对于销售，面对有窜货地方，这些地方城市经理管理没有尽到责任，第一个是要约谈，违反制度和食品安全法，要求改善。城市经理调整市场。去年追溯到市场上18年19年市场上发生窜货行为，该开除就开除。中间商链条做侦察，调动社会资源。建立起来一个文化，不想不敢窜货的文化。'

four_4_1 = '不断在追踪，落实'

six_1 = '在日常沟通上，销售会议上，开年第一次大会，把思想价值观层面做年度开篇共识。阶段性沟通，感觉到团队思想上，认识上有些松懈。点滴营养，绽放每一个生命，本土疫情有关注的时候，跟大家讲接受度比较高。春节期间，消费者购买需求旺盛的时候，跟大家再讲一讲。自建店，中老年人，当我们看到中老年人看就买牛奶，说明他们是刚需。不是单向告知，指导我们的业务行为和指导动作。\
比如说，让牛人绽放，选人用人中，让年轻人上，加单子，再来看牛人就是要绽放的。\
好的：消费者第一第一第一，什么时候就是消费者，我们的经销商，客户，员工和零售合作伙伴权益分配的时候，把消费者摆到前面。待提升：异想天开，推动公司落地研发中心，区域营销，一些事情有想法，平时自己业务繁忙。两年时间很快过去，推动公司变革上，RTM部署上，大的部署还可以做的更好。'

seven_7_4 = '发展方向：第一种去做全国性的销售管理，第二种品牌市场方面，在这个领域比较缺乏。\
发展方式：扩大职责，承担总部一些职责。和销管事业部层面轮岗，兼职的方式。'

num = 100

text_list = [one_1, four_1_1, four_1_2, four_2_1, four_2_2, four_2_3, four_3_1, four_3_2, four_4_1, six_1, seven_7_4]
name_list = ['one_1', 'four_1_1', 'four_1_2', 'four_2_1', 'four_2_2', 'four_2_3', 'four_3_1', 'four_3_2', 'four_4_1', 'six_1', 'seven_7_4']


# for index,text in enumerate(text_list):
#     aug = augment(types=['style','structure','bread'],num=num, instruction=text)
#     with open(f'result_1/{name_list[index]}.json', 'w', encoding='utf-8') as f:
#         json.dump(aug, f, ensure_ascii=False, indent=4)
#     print(f'{index}/{num}')    

def process_task(index, text):
    aug = augment(types=['style', 'structure', 'bread'], num=num, instruction=text)
    file_path = f'result_1/{name_list[index]}.json'
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