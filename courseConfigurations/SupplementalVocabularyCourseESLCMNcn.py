__author__ = 'vagrant'
# -*- coding: utf-8 -*-

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesESLCMNcn"

languageDict = [
    ["x for Chinese speakers", "English"],
]
unitMap = {
    u"见面与问候": ["Meeting-and-Greeting-1",
              "Meeting-and-Greeting-2"],
    u"获取语言学习的帮助": ["Communication-Facilitation-1",
                  "Communication-Facilitation-2",
                  "Communication-Facilitation-3",
                  "Communication-Facilitation-4",
                  "Communication-Facilitation-5",
                  "Communication-Facilitation-6",
                  "Communication-Facilitation-7"],
    u"获取更多语言学习的帮助": ["Helper-Relationship-Facilitation",
                    "Language-Learning-Facilitation-1",
                    "Language-Learning-Facilitation-2",
                    "Translation-Facilitation"],
    u"礼貌交谈": ["Polite-Conversation-1",
             "Polite-Conversation-2",
             "Polite-Conversation-3",
             "Useful-Expressions"],
    u"形状和颜色": ["Shapes",
              "Colors"],
    u"衣服": ["Clothing-1",
           "Clothing-2",
           "Clothing-3"],
    u"购物与商店": ["Stores",
              "Shopping-1",
              "Shopping-2",
              "Shopping-3",
              "Shopping-4",
              "Shopping-5"],
    u"房子和公寓": ["House-Apartment-1",
              "House-Apartment-2"],
    u"房间": ["Living-Room",
           "Dining-Room",
           "Kitchen",
           "Bathroom-1",
           "Bathroom-2",
           "Bedroom"],
    u"家庭": ["Family-1",
           "Family-2",
           "Family-3",
           "Family-4"],
    u"办公室与职业": ["Office-1",
               "Office-2",
               "Professions-1",
               "Professions-2"],
    u"身体部位": ["Parts-of-the-Body-1",
             "Parts-of-the-Body-2"],
    u"紧急情况": ["Emergencies-1",
             "Emergencies-2",
             "Emergencies-3",
             "Emergencies-4",
             "Emergencies-5"],
    u"地方与问路": ["Places-1",
              "Places-2",
              "Asking-for-Directions-1",
              "Asking-for-Directions-2"],
    u"学校": ["School-1",
           "School-2",
           "School-3"],
    u"乐器": ["Musical-Instruments-1",
           "Musical-Instruments-2"],
    u"娱乐": ["Recreation-1",
           "Recreation-2",
           "Recreation-3"],
    u"自然界": ["Nature-1",
            "Nature-2"],
    u"动物": ["Animals-1",
           "Animals-2"],
    u"食物1": ["Meals",
            "Beverages",
            "Fruit",
            "Vegetables",
            "Grains"],
    u"食物2": ["Dairy",
            "Meat",
            "Seafood",
            "Spices-Condiments",
            "Dessert"],
    u"去餐馆": ["At-the-Restaurant-1",
            "At-the-Restaurant-2",
            "At-the-Restaurant-3",
            "At-the-Restaurant-4",
            "At-the-Restaurant-5"],
    u"语言": ["Languages-1",
           "Languages-2",
           "Languages-3",
           "Languages-4"],
    u"国名": ["Continents",
           "Countries-1",
           "Countries-2",
           "Countries-3"],
    u"旅游": ["Travel-1",
           "Travel-2",
           "Travel-3",
           "Travel-4",
           "Travel-5"],
    u"买票": ["Buying-Tickets-1",
           "Buying-Tickets-2",
           "Buying-Tickets-3"],
    u"乘出租车": ["Taking-a-Taxi-1",
             "Taking-a-Taxi-2",
             "Taking-a-Taxi-3"],
    u"住旅馆": ["At-the-Hotel-1",
            "At-the-Hotel-2",
            "At-the-Hotel-3",
            "At-the-Hotel-4"],
    u"去银行": ["Going-to-the-Bank-1",
            "Going-to-the-Bank-2",
            "Going-to-the-Bank-3",
            "Going-to-the-Bank-4"],
    u"数字": ["Numbers-Cardinal-1",
           "Numbers-Cardinal-2",
           "Numbers-Cardinal-3",
           "Numbers-Cardinal-4",
           "Numbers-Ordinal",
           "Numbers-Other"],
    u"星期和时间": ["Days-of-the-Week-1",
              "Days-of-the-Week-2",
              "Time-1",
              "Time-2",
              "Asking-the-Time"],
    u"季节和天气": ["Months",
              "Seasons",
              "Weather-1",
              "Weather-2"],
    u"人称代词 和 所有格形容词": ["Personal-Pronouns",
                      "Possessive-Adjectives",
                      "Conjunctions"],
    u"形容词 和 副词": ["Adjectives-1",
                 "Adjectives-2",
                 "Adjectives-3",
                 "Adverbs"],
    u"动词": ["Verbs-1",
           "Verbs-2",
           "Verbs-3",
           "Verbs-4",
           "Verbs-5",
           "Verbs-6",
           "Verbs-7",
           "Verbs-8"],
    u"介词": ["Prepositions-1",
           "Prepositions-2",
           "Prepositions-3",
           "Prepositions-4"]
}
unitNameList = [
    u"见面与问候",
    u"获取语言学习的帮助",
    u"获取更多语言学习的帮助",
    u"礼貌交谈",
    u"形状和颜色",
    u"衣服",
    u"购物与商店",
    u"房子和公寓",
    u"房间",
    u"家庭",
    u"办公室与职业",
    u"身体部位",
    u"紧急情况",
    u"地方与问路",
    u"学校",
    u"乐器",
    u"娱乐",
    u"自然界",
    u"动物",
    u"食物1",
    u"食物2",
    u"去餐馆",
    u"语言",
    u"国名",
    u"旅游",
    u"买票",
    u"乘出租车",
    u"住旅馆",
    u"去银行",
    u"数字",
    u"星期和时间",
    u"季节和天气",
    u"人称代词 和 所有格形容词",
    u"形容词 和 副词",
    u"动词",
    u"介词",
]
lessonOrder = unitMap
isESLTrue = True
lessonNameToListNameMap = {
"Adjectives-1": u"形容词 1",
"Adjectives-2": u"形容词 2",
"Adjectives-3": u"形容词 3",
"Adverbs": u"副词",
"Animals-1": u"动物 1",
"Animals-2": u"动物 2",
"Asking-for-Directions-1": u"问路 1",
"Asking-for-Directions-2": u"问路 2",
"Asking-the-Time": u"问时间",
"At-the-Hotel-1": u"在旅馆里 1",
"At-the-Hotel-2": u"在旅馆里 2",
"At-the-Hotel-3": u"在旅馆里 3",
"At-the-Hotel-4": u"在旅馆里 4",
"At-the-Restaurant-1": u"在饭馆里 1",
"At-the-Restaurant-2": u"在饭馆里 2",
"At-the-Restaurant-3": u"在饭馆里 3",
"At-the-Restaurant-4": u"在饭馆里 4",
"At-the-Restaurant-5": u"在饭馆里 5",
"Bathroom-1": u"卫生间 1",
"Bathroom-2": u"卫生间 2",
"Bedroom": u"卧室",
"Beverages": u"饮料",
"Buying-Tickets-1": u"买票 1",
"Buying-Tickets-2": u"买票 2",
"Buying-Tickets-3": u"买票 3",
"Clothing-1": u"衣服 1",
"Clothing-2": u"衣服 2",
"Clothing-3": u"衣服 3",
"Colors": u"颜色",
"Communication-Facilitation-1": u"促进语言沟通 1",
"Communication-Facilitation-2": u"促进语言沟通 2",
"Communication-Facilitation-3": u"促进语言沟通 3",
"Communication-Facilitation-4": u"促进语言沟通 4",
"Communication-Facilitation-5": u"促进语言沟通 5",
"Communication-Facilitation-6": u"促进语言沟通 6",
"Communication-Facilitation-7": u"促进语言沟通 7",
"Conjunctions": u"连词",
"Continents": u"七大洲",
"Countries-1": u"国名 1",
"Countries-2": u"国名 2",
"Countries-3": u"国名 3",
"Dairy": u"乳品",
"Days-of-the-Week-1": u"一星期的日子 1",
"Days-of-the-Week-2": u"一星期的日子 2",
"Dessert": u"甜点",
"Dining-Room": u"餐厅",
"Emergencies-1": u"紧急情况 1",
"Emergencies-2": u"紧急情况 2",
"Emergencies-3": u"紧急情况 3",
"Emergencies-4": u"紧急情况 4",
"Emergencies-5": u"紧急情况 5",
"Family-1": u"家庭 1",
"Family-2": u"家庭 2",
"Family-3": u"家庭 3",
"Family-4": u"家庭 4",
"Fruit": u"水果",
"Going-to-the-Bank-1": u"去银行 1",
"Going-to-the-Bank-2": u"去银行 2",
"Going-to-the-Bank-3": u"去银行 3",
"Going-to-the-Bank-4": u"去银行 4",
"Grains": u"谷类",
"Helper-Relationship-Facilitation": u"促进与帮手沟通",
"House-Apartment-1": u"房子／公寓 1",
"House-Apartment-2": u"房子／公寓 2",
"Kitchen": u"厨房",
"Language-Learning-Facilitation-1": u"促进语言学习 1",
"Language-Learning-Facilitation-2": u"促进语言学习 2",
"Languages-1": u"语言种类 1",
"Languages-2": u"语言种类 2",
"Languages-3": u"语言种类 3",
"Languages-4": u"语言种类 4",
"Living-Room": u"起居室",
"Meals": u"饮食",
"Meat": u"肉类",
"Meeting-and-Greeting-1": u"问候语 1",
"Meeting-and-Greeting-2": u"问候语 2",
"Months": u"月份",
"Musical-Instruments-1": u"乐器 1",
"Musical-Instruments-2": u"乐器 2",
"Nature-1": u"自然界 1",
"Nature-2": u"自然界 2",
"Numbers-Cardinal-1": u"数字：基数 1",
"Numbers-Cardinal-2": u"数字：基数 2",
"Numbers-Cardinal-3": u"数字：基数 3",
"Numbers-Cardinal-4": u"数字：基数 4",
"Numbers-Ordinal": u"序数",
"Numbers-Other": u"其它数字",
"Office-1": u"办公室 1",
"Office-2": u"办公室 2",
"Parts-of-the-Body-1": u"身体部位 1",
"Parts-of-the-Body-2": u"身体部位 2",
"Personal-Pronouns": u"代词",
"Places-1": u"地方 1",
"Places-2": u"地方 2",
"Polite-Conversation-1": u"礼貌交谈 1",
"Polite-Conversation-2": u"礼貌交谈 2",
"Polite-Conversation-3": u"礼貌沟通 3",
"Possessive-Adjectives": u"所有格形容词",
"Prepositions-1": u"介词 1",
"Prepositions-2": u"介词 2",
"Prepositions-3": u"介词 3",
"Prepositions-4": u"介词 4",
"Professions-1": u"职业 1",
"Professions-2": u"职业 2",
"Recreation-1": u"娱乐 1",
"Recreation-2": u"娱乐 2",
"Recreation-3": u"娱乐 3",
"School-1": u"学校 1",
"School-2": u"学校 2",
"School-3": u"学校 3",
"Seafood": u"海鲜",
"Seasons": u"季节",
"Shapes": u"形状",
"Shopping-1": u"买东西 1",
"Shopping-2": u"买东西 2",
"Shopping-3": u"买东西 3",
"Shopping-4": u"买东西 4",
"Shopping-5": u"买东西 5",
"Spices-Condiments": u"香料／调味品",
"Stores": u"商店",
"Taking-a-Taxi-1": u"乘出租车 1",
"Taking-a-Taxi-2": u"乘出租车 2",
"Taking-a-Taxi-3": u"乘出租车 3",
"Time-1": u"时间 1",
"Time-2": u"时间 2",
"Translation-Facilitation": u"请求翻译",
"Travel-1": u"旅游 1",
"Travel-2": u"旅游 2",
"Travel-3": u"旅游 3",
"Travel-4": u"旅游 4",
"Travel-5": u"旅游 5",
"Useful-Expressions": u"常用短语",
"Vegetables": u"蔬菜",
"Verbs-1": u"动词 1",
"Verbs-2": u"动词 2",
"Verbs-3": u"动词 3",
"Verbs-4": u"动词 4",
"Verbs-5": u"动词 5",
"Verbs-6": u"动词 6　",
"Verbs-7": u"动词 7",
"Verbs-8": u"动词 8",
"Weather-1": u"天气 1",
"Weather-2": u"天气 2",
}
baseText = u"""
通过本单元的学习，你会：

-记住与主题有关的单词和短语
-能读、能打出这些单词和短语
-能辨别词语的发音并能正确地发音

首先，通过一些诸如“Language Comparison”[语言对比]和“Pronunciation Practice”[发音练习]的活动，帮助你更熟悉学习材料。

其次，做语音方面的选择题和配对练习，以强化单词和短语记忆。

然后，做听写和打字练习，以训练说写能力。

最后，完成每个单元结束时的评估活动，以测试对单词和短语的掌握程度。"""

unitObjectives = {
    u"见面与问候": u"本单元学习有关见面和问候的单词和短语。" + "\n" + baseText,
    u"获取语言学习的帮助": u"本单元学习有关获取语言学习的帮助的单词和短语。" + "\n" + baseText,
    u"获取更多语言学习的帮助": u"本单元学习有关获取更多语言学习的帮助的单词和短语。" + "\n" + baseText,
    u"礼貌交谈": u"本单元学习有关礼貌交谈的单词和短语。" + "\n" + baseText,
    u"形状和颜色": u"本单元学习有关形状和颜色的单词和短语。" + "\n" + baseText,
    u"衣服": u"本单元学习有关衣服的单词和短语。" + "\n" + baseText,
    u"购物与商店": u"本单元学习有关购物与商店的单词和短语。" + "\n" + baseText,
    u"房子和公寓": u"本单元学习有关房子和公寓的单词和短语。" + "\n" + baseText,
    u"房间": u"本单元学习有关房间的单词和短语。" + "\n" + baseText,
    u"家庭": u"本单元学习有关家庭的单词和短语。" + "\n" + baseText,
    u"办公室与职业": u"本单元学习有关办公室与职业的单词和短语。" + "\n" + baseText,
    u"身体部位": u"本单元学习有关身体部位的单词和短语。" + "\n" + baseText,
    u"紧急情况": u"本单元学习有关紧急情况的单词和短语。" + "\n" + baseText,
    u"地方与问路": u"本单元学习有关地方与问路的单词和短语。" + "\n" + baseText,
    u"学校": u"本单元学习有关学校的单词和短语。" + "\n" + baseText,
    u"乐器": u"本单元学习有关乐器的单词和短语。" + "\n" + baseText,
    u"娱乐": u"本单元学习有关娱乐的单词和短语。" + "\n" + baseText,
    u"自然界": u"本单元学习有关自然界的单词和短语。" + "\n" + baseText,
    u"动物": u"本单元学习有关动物的单词和短语。" + "\n" + baseText,
    u"食物1": u"本单元学习有关食物的单词和短语。" + "\n" + baseText,
    u"食物2": u"本单元学习有关食物的单词和短语。" + "\n" + baseText,
    u"去餐馆": u"本单元学习有关去餐馆的单词和短语。" + "\n" + baseText,
    u"语言": u"本单元学习有关语言的单词和短语。" + "\n" + baseText,
    u"国名": u"本单元学习有关国名的单词和短语。" + "\n" + baseText,
    u"旅游": u"本单元学习有关旅游的单词和短语。" + "\n" + baseText,
    u"买票": u"本单元学习有关买票的单词和短语。" + "\n" + baseText,
    u"乘出租车": u"本单元学习有关乘出租车的单词和短语。" + "\n" + baseText,
    u"住旅馆": u"本单元学习有关住旅馆的单词和短语。" + "\n" + baseText,
    u"去银行": u"本单元学习有关去银行的单词和短语。" + "\n" + baseText,
    u"数字": u"本单元学习有关数字的单词和短语。" + "\n" + baseText,
    u"星期和时间": u"本单元学习有关星期和时间的单词和短语。" + "\n" + baseText,
    u"季节和天气": u"本单元学习有关季节和天气的单词和短语。" + "\n" + baseText,
    u"人称代词 和 所有格形容词": u"本单元学习有关人称代词和所有格形容词的单词和短语。" + "\n" + baseText,
    u"形容词 和 副词": u"本单元学习有关形容词和副词的单词和短语。" + "\n" + baseText,
    u"动词": u"本单元学习有关动词的单词和短语。" + "\n" + baseText,
    u"介词": u"本单元学习有关介词的单词和短语。" + "\n" + baseText
}
isTranslit = False

def createSVCConfiguration():
    """
    takes the above information and builds a course object for the rest of the scripts

    :return: a filled out course object
    """
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    configObject.unitObjectives = unitObjectives
    configObject.lessonOrder = lessonOrder
    configObject.unitNumbers = configObject.createUnitNumbers(unitNameList)
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitNameList)
    configObject.isTranslit = isTranslit

    return configObject