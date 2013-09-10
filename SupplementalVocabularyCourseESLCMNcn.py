__author__ = 'vagrant'
# -*- coding: utf-8 -*-

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesESLCMNcn"

languageDict = [
    ["x for Chinese speakers", "English"],
]
unitMap = {
    "见面与问候": ["Meeting-and-Greeting-1",
              "Meeting-and-Greeting-2"],
    "获取语言学习的帮助": ["Communication-Facilitation-1",
                  "Communication-Facilitation-2",
                  "Communication-Facilitation-3",
                  "Communication-Facilitation-4",
                  "Communication-Facilitation-5",
                  "Communication-Facilitation-6",
                  "Communication-Facilitation-7"],
    "获取更多语言学习的帮助": ["Helper-Relationship",
                    "Language-Learning-Facilitation-1",
                    "Language-Learning-Facilitation-2",
                    "Translation-Facilitation"],
    "礼貌交谈": ["Polite-Conversation-1",
             "Polite-Conversation-2",
             "Polite-Conversation-3",
             "Useful-Expressions"],
    "形状和颜色": ["Shapes",
              "Colors"],
    "衣服": ["Clothing-1",
           "Clothing-2",
           "Clothing-3"],
    "购物与商店": ["Stores",
              "Shopping-1",
              "Shopping-2",
              "Shopping-3",
              "Shopping-4",
              "Shopping-5"],
    "房子和公寓": ["House-Apartment-1",
              "House-Apartment-2"],
    "房间": ["Living-Room",
           "Dining-Room",
           "Kitchen",
           "Bathroom-1",
           "Bathroom-2",
           "Bedroom"],
    "家庭": ["Family-1",
           "Family-2",
           "Family-3",
           "Family-4"],
    "办公室与职业": ["Office-1",
               "Office-2",
               "Professions-1",
               "Professions-2"],
    "身体部位": ["Parts-of-the-Body-1",
             "Parts-of-the-Body-2"],
    "紧急情况": ["Emergencies-1",
             "Emergencies-2",
             "Emergencies-3",
             "Emergencies-4",
             "Emergencies-5"],
    "地方与问路": ["Places-1",
              "Places-2",
              "Asking-for-Directions-1",
              "Asking-for-Directions-2"],
    "学校": ["School-1",
           "School-2",
           "School-3"],
    "乐器": ["Musical-Instruments-1",
           "Musical-Instruments-2"],
    "娱乐": ["Recreation-1",
           "Recreation-2",
           "Recreation-3"],
    "自然界": ["Nature-1",
            "Nature-2"],
    "动物": ["Animals-1",
           "Animals-2"],
    "食物1": ["Meals",
            "Beverages",
            "Fruit",
            "Vegetables",
            "Grains"],
    "食物2": ["Dairy",
            "Meat",
            "Seafood",
            "Spices-Condiments",
            "Dessert"],
    "去餐馆": ["At-the-Restaurant-1",
            "At-the-Restaurant-2",
            "At-the-Restaurant-3",
            "At-the-Restaurant-4",
            "At-the-Restaurant-5"],
    "语言": ["Languages-1",
           "Languages-2",
           "Languages-3",
           "Languages-4"],
    "国名": ["Continents",
           "Countries-1",
           "Countries-2",
           "Countries-3"],
    "旅游": ["Travel-1",
           "Travel-2",
           "Travel-3",
           "Travel-4",
           "Travel-5"],
    "买票": ["Buying-Tickets-1",
           "Buying-Tickets-2",
           "Buying-Tickets-3"],
    "乘出租车": ["Taking-a-Taxi-1",
             "Taking-a-Taxi-2",
             "Taking-a-Taxi-3"],
    "住旅馆": ["At-the-Hotel-1",
            "At-the-Hotel-2",
            "At-the-Hotel-3",
            "At-the-Hotel-4"],
    "去银行": ["Going-to-the-Bank-1",
            "Going-to-the-Bank-2",
            "Going-to-the-Bank-3",
            "Going-to-the-Bank-4"],
    "数字": ["Numbers-Cardinal-1",
           "Numbers-Cardinal-2",
           "Numbers-Cardinal-3",
           "Numbers-Cardinal-4",
           "Numbers-Ordinal",
           "Numbers-Other"],
    "星期和时间": ["Days-of-the-Week-1",
              "Days-of-the-Week-2",
              "Time-1",
              "Time-2",
              "Asking-the-Time"],
    "季节和天气": ["Months",
              "Seasons",
              "Weather-1",
              "Weather-2"],
    "人称代词 和 所有格形容词": ["Personal-Pronouns",
                      "Possessive-Adjectives",
                      "Conjunctions"],
    "形容词 和 副词": ["Adjectives-1",
                 "Adjectives-2",
                 "Adjectives-3",
                 "Adverbs"],
    "动词": ["Verbs-1",
           "Verbs-2",
           "Verbs-3",
           "Verbs-4",
           "Verbs-5",
           "Verbs-6",
           "Verbs-7",
           "Verbs-8"],
    "介词": ["Prepositions-1",
           "Prepositions-2",
           "Prepositions-3",
           "Prepositions-4"]
}
unitNameList = unitMap.keys()
lessonOrder = unitMap
isESLTrue = True
lessonNameToListNameMap = {
    "形容词 1": "Adjectives-1",
    "形容词 2": "Adjectives-2",
    "形容词 3": "Adjectives-3",
    "副词": "Adverbs",
    "动物 1": "Animals-1",
    "动物 2": "Animals-2",
    "问路 1": "Asking-for-Directions-1",
    "问路 2": "Asking-for-Directions-2",
    "问时间": "Asking-the-Time",
    "在旅馆里 1": "At-the-Hotel-1",
    "在旅馆里 2": "At-the-Hotel-2",
    "在旅馆里 3": "At-the-Hotel-3",
    "在旅馆里 4": "At-the-Hotel-4",
    "在饭馆里 1": "At-the-Restaurant-1",
    "在饭馆里 2": "At-the-Restaurant-2",
    "在饭馆里 3": "At-the-Restaurant-3",
    "在饭馆里 4": "At-the-Restaurant-4",
    "在饭馆里 5": "At-the-Restaurant-5",
    "卫生间 1": "Bathroom-1",
    "卫生间 2": "Bathroom-2",
    "卧室": "Bedroom",
    "饮料": "Beverages",
    "买票 1": "Buying-Tickets-1",
    "买票 2": "Buying-Tickets-2",
    "买票 3": "Buying-Tickets-3",
    "衣服 1": "Clothing-1",
    "衣服 2": "Clothing-2",
    "衣服 3": "Clothing-3",
    "颜色": "Colors",
    "促进语言沟通 1": "Communication-Facilitation-1",
    "促进语言沟通 2": "Communication-Facilitation-2",
    "促进语言沟通 3": "Communication-Facilitation-3",
    "促进语言沟通 4": "Communication-Facilitation-4",
    "促进语言沟通 5": "Communication-Facilitation-5",
    "促进语言沟通 6": "Communication-Facilitation-6",
    "促进语言沟通 7": "Communication-Facilitation-7",
    "连词": "Conjunctions",
    "七大洲": "Continents",
    "国名 1": "Countries-1",
    "国名 2": "Countries-2",
    "国名 3": "Countries-3",
    "乳品": "Dairy",
    "一星期的日子 1": "Days-of-the-Week-1",
    "一星期的日子 2": "Days-of-the-Week-2",
    "甜点": "Dessert",
    "餐厅": "Dining-Room",
    "紧急情况 1": "Emergencies-1",
    "紧急情况 2": "Emergencies-2",
    "紧急情况 3": "Emergencies-3",
    "紧急情况 4": "Emergencies-4",
    "紧急情况 5": "Emergencies-5",
    "家庭 1": "Family-1",
    "家庭 2": "Family-2",
    "家庭 3": "Family-3",
    "家庭 4": "Family-4",
    "水果": "Fruit",
    "去银行 1": "Going-to-the-Bank-1",
    "去银行 2": "Going-to-the-Bank-2",
    "去银行 3": "Going-to-the-Bank-3",
    "去银行 4": "Going-to-the-Bank-4",
    "谷类": "Grains",
    "促进与帮手沟通": "Helper-Relationship-Facilitation",
    "房子／公寓 1": "House-Apartment-1",
    "房子／公寓 2": "House-Apartment-2",
    "厨房": "Kitchen",
    "促进语言学习 1": "Language-Learning-Facilitation-1",
    "促进语言学习 2": "Language-Learning-Facilitation-2",
    "语言种类 1": "Languages-1",
    "语言种类 2": "Languages-2",
    "语言种类 3": "Languages-3",
    "语言种类 4": "Languages-4",
    "起居室": "Living-Room",
    "饮食": "Meals",
    "肉类": "Meat",
    "问候语 1": "Meeting-and-Greeting-1",
    "问候语 2": "Meeting-and-Greeting-2",
    "月份": "Months",
    "乐器 1": "Musical-Instruments-1",
    "乐器 2": "Musical-Instruments-2",
    "自然界 1": "Nature-1",
    "自然界 2": "Nature-2",
    "数字：基数 1": "Numbers-Cardinal-1",
    "数字：基数 2": "Numbers-Cardinal-2",
    "数字：基数 3": "Numbers-Cardinal-3",
    "数字：基数 4": "Numbers-Cardinal-4",
    "序数": "Numbers-Ordinal",
    "其它数字": "Numbers-Other",
    "办公室 1": "Office-1",
    "办公室 2": "Office-2",
    "身体部位 1": "Parts-of-the-Body-1",
    "身体部位 2": "Parts-of-the-Body-2",
    "代词": "Personal-Pronouns",
    "地方 1": "Places-1",
    "地方 2": "Places-2",
    "礼貌交谈 1": "Polite-Conversation-1",
    "礼貌交谈 2": "Polite-Conversation-2",
    "礼貌沟通 3": "Polite-Conversation-3",
    "所有格形容词": "Possessive-Adjectives",
    "介词 1": "Prepositions-1",
    "介词 2": "Prepositions-2",
    "介词 3": "Prepositions-3",
    "介词 4": "Prepositions-4",
    "职业 1": "Professions-1",
    "职业 2": "Professions-2",
    "娱乐 1": "Recreation-1",
    "娱乐 2": "Recreation-2",
    "娱乐 3": "Recreation-3",
    "学校 1": "School-1",
    "学校 2": "School-2",
    "学校 3": "School-3",
    "海鲜": "Seafood",
    "季节": "Seasons",
    "形状": "Shapes",
    "买东西 1": "Shopping-1",
    "买东西 2": "Shopping-2",
    "买东西 3": "Shopping-3",
    "买东西 4": "Shopping-4",
    "买东西 5": "Shopping-5",
    "香料／调味品": "Spices-Condiments",
    "商店": "Stores",
    "乘出租车 1": "Taking-a-Taxi-1",
    "乘出租车 2": "Taking-a-Taxi-2",
    "乘出租车 3": "Taking-a-Taxi-3",
    "时间 1": "Time-1",
    "时间 2": "Time-2",
    "请求翻译": "Translation-Facilitation",
    "旅游 1": "Travel-1",
    "旅游 2": "Travel-2",
    "旅游 3": "Travel-3",
    "旅游 4": "Travel-4",
    "旅游 5": "Travel-5",
    "常用短语": "Useful-Expressions",
    "蔬菜": "Vegetables",
    "动词 1": "Verbs-1",
    "动词 2": "Verbs-2",
    "动词 3": "Verbs-3",
    "动词 4": "Verbs-4",
    "动词 5": "Verbs-5",
    "动词 6　": "Verbs-6",
    "动词 7": "Verbs-7",
    "动词 8": "Verbs-8",
    "天气 1": "Weather-1",
    "天气 2": "Weather-2"
}
baseText = """
通过本单元的学习，你会：

-记住与主题有关的单词和短语
-能读、能打出这些单词和短语
-能辨别词语的发音并能正确地发音

首先，通过一些诸如“Language Comparison”[语言对比]和“Pronunciation Practice”[发音练习]的活动，帮助你更熟悉学习材料。

其次，做语音方面的选择题和配对练习，以强化单词和短语记忆。

然后，做听写和打字练习，以训练说写能力。

最后，完成每个单元结束时的评估活动，以测试对单词和短语的掌握程度。"""

unitObjectives = {
    "见面与问候": "本单元学习有关见面和问候的单词和短语。" + "\n" + baseText,
    "获取语言学习的帮助": "本单元学习有关获取语言学习的帮助的单词和短语。" + "\n" + baseText,
    "获取更多语言学习的帮助": "本单元学习有关获取更多语言学习的帮助的单词和短语。" + "\n" + baseText,
    "礼貌交谈": "本单元学习有关礼貌交谈的单词和短语。" + "\n" + baseText,
    "形状和颜色": "本单元学习有关形状和颜色的单词和短语。" + "\n" + baseText,
    "衣服": "本单元学习有关衣服的单词和短语。" + "\n" + baseText,
    "购物与商店": "本单元学习有关购物与商店的单词和短语。" + "\n" + baseText,
    "房子和公寓": "本单元学习有关房子和公寓的单词和短语。" + "\n" + baseText,
    "房间": "本单元学习有关房间的单词和短语。" + "\n" + baseText,
    "家庭": "本单元学习有关家庭的单词和短语。" + "\n" + baseText,
    "办公室与职业": "本单元学习有关办公室与职业的单词和短语。" + "\n" + baseText,
    "身体部位": "本单元学习有关身体部位的单词和短语。" + "\n" + baseText,
    "紧急情况": "本单元学习有关紧急情况的单词和短语。" + "\n" + baseText,
    "地方与问路": "本单元学习有关地方与问路的单词和短语。" + "\n" + baseText,
    "学校": "本单元学习有关学校的单词和短语。" + "\n" + baseText,
    "乐器": "本单元学习有关乐器的单词和短语。" + "\n" + baseText,
    "娱乐": "本单元学习有关娱乐的单词和短语。" + "\n" + baseText,
    "自然界": "本单元学习有关自然界的单词和短语。" + "\n" + baseText,
    "动物": "本单元学习有关动物的单词和短语。" + "\n" + baseText,
    "食物1": "本单元学习有关食物的单词和短语。" + "\n" + baseText,
    "食物2": "本单元学习有关食物的单词和短语。" + "\n" + baseText,
    "去餐馆": "本单元学习有关去餐馆的单词和短语。" + "\n" + baseText,
    "语言": "本单元学习有关语言的单词和短语。" + "\n" + baseText,
    "国名": "本单元学习有关国名的单词和短语。" + "\n" + baseText,
    "旅游": "本单元学习有关旅游的单词和短语。" + "\n" + baseText,
    "买票": "本单元学习有关买票的单词和短语。" + "\n" + baseText,
    "乘出租车": "本单元学习有关乘出租车的单词和短语。" + "\n" + baseText,
    "住旅馆": "本单元学习有关住旅馆的单词和短语。" + "\n" + baseText,
    "去银行": "本单元学习有关去银行的单词和短语。" + "\n" + baseText,
    "数字": "本单元学习有关数字的单词和短语。" + "\n" + baseText,
    "星期和时间": "本单元学习有关星期和时间的单词和短语。" + "\n" + baseText,
    "季节和天气": "本单元学习有关季节和天气的单词和短语。" + "\n" + baseText,
    "人称代词 和 所有格形容词": "本单元学习有关人称代词和所有格形容词的单词和短语。" + "\n" + baseText,
    "形容词 和 副词": "本单元学习有关形容词和副词的单词和短语。" + "\n" + baseText,
    "动词": "本单元学习有关动词的单词和短语。" + "\n" + baseText,
    "介词": "本单元学习有关介词的单词和短语。" + "\n" + baseText
}


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

    return configObject