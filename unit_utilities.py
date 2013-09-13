# -*- coding: utf-8 -*-
import os
import re
from BeautifulSoup import BeautifulStoneSoup, Tag, NavigableString
import lxml
from lxml import etree
import yaml
import collections


__author__ = 'S. P. Powers'

byki_modes = ['Preview', 'SelfReportingRecognize', 'RecognizeWritten', 'SelfReportingRecognize',
              'ProduceWritten']
activityName = {
    "Reading": "Language Comparison",
    "Preview": "Preview It",
    "SelfReportingRecognize": "Recognize & Say It",
    "Pronunciation": "Pronunciation Practice",
    "AudioMultiChoice": "Audio Multiple Choice",
    "MultipleChoice2": "Multiple Choice",
    "Matching": "Matching",
    "SelfReportingProduce": "Produce & Say It",
    "Dictation2": "Dictation",
    "ProduceWritten": "Produce & Write It"
}
spanishActivityNameDict = dict(Reading=u"Comparación de idiomas", Preview=u"Ver", SelfReportingRecognize=u'Reconozca y diga',
    Pronunciation=u"Práctica de la pronunciación", AudioMultiChoice=u"Opción múltiple (Audio)", MultipleChoice2=u"Opción múltiple",
    Matching=u"Correspondientes", SelfReportingProduce=u"Produzca y diga", Dictation2=u"Dictado", ProduceWritten=u"Produzca y escriba")
eslActivityNames = {"SPANISH": spanishActivityNameDict,
                    "INDONESIAN": activityName,
                    "CHINESE": activityName,}
knownLanguageValues = {
    "CHINESE": {"uiFont": "Chinese", "knownFont": "Chinese", },
    "ENGLISH": {"uiFont": "Latin", "knownFont": "Latin", },
    "SPANISH": {"uiFont": "Latin", "knownFont": "Latin", },
    "INDONESIAN": {"uiFont": "Latin", "knownFont": "Latin", },
}


def build_unit_xml(language_data, basedir, config):
    '''accepts language data as a dictionary and a basedir for the unit.xml to be generated in.
    '''
    #module name to activity name map

    translit_state = 'false'
    lesson_files = os.listdir(os.path.join(basedir, 'data'))
    soup = BeautifulStoneSoup()

    #generate the top tag and insert it an empty soup object
    top_tag = Tag(soup, 'cw1Unit')
    top_tag['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
    top_tag['xsi:noNamespaceSchemaLocation'] = 'cw1Unit_schema.xsd'
    unit_name = os.path.split(basedir)[1]
    top_tag['name'] = config['name']
    top_tag['knownLanguage'] = 'ENGLISH'
    top_tag['learningLanguage'] = language_data['code']
    top_tag['learningFontUrl'] = 'fonts/{0:>s}.swf'.format(language_data['swfFont'])
    if 'rtl' in language_data.attrMap:
        top_tag['isRTL'] = language_data['rtl']
    else:
        top_tag['isRTL'] = 'false'
    top_tag['transliterated'] = translit_state
    if 'hasalphabet' in language_data.attrMap:
        top_tag['hasAlphabet'] = language_data['hasalphabet']
    else:
        top_tag['hasAlphabet'] = 'false'
    if 'hasscriptassistant' in language_data.attrMap:
        top_tag['hasScriptAssistant'] = language_data['hasscriptassistant']
    else:
        top_tag['hasScriptAssistant'] = 'false'

    top_tag['formatversion'] = '1'
    soup.insert(0, top_tag)

    #generate the lesson tags
    lesson_counter = 1
    for lesson in lesson_files:
        if lesson == 'config.yaml' or lesson == 'unit.xml':
            continue
        name = re.sub('_', ' ', lesson)
        lesson_tag = Tag(soup, 'lesson')
        lesson_tag['name'] = 'Lesson {0:>d}'.format(lesson_counter)
        top_tag.insert(lesson_counter - 1, lesson_tag)
        counter = 0
        #generate the activity tag within the lesson tag
        activity_group = 'activities'
        if 'TLX' in lesson:
            activity_group = 'tlx_activities'
        for activity in config[activity_group]:
            activity_tag = Tag(soup, 'activity')
            activity_tag['required'] = 'false'
            activity_tag['name'] = activityName[activity] #'Lesson {0:>d}'.format(lesson_counter)
            activity_tag['moduleUrl'] = 'modules/{0:>s}.swf'.format(activity)
            activity_tag['dataUrl'] = 'data/{0:>s}'.format(lesson)
            if activity in byki_modes:
                activity_tag.attrib['isB4u'] = 'true'
            else:
                activity_tag.attrib['isB4u'] = 'false'
            lesson_tag.insert(counter, activity_tag)
            counter += 1
        lesson_counter += 1

    #generate the assessment tag
    assessment_tag = Tag(soup, 'assessment')
    assessment_tag['name'] = 'Assessment'
    module_str = ''
    for module in config['assessment']['modules']:
        module_str += 'modules/{0:>s}.swf,'.format(module)
    assessment_tag['moduleUrl'] = module_str[:-1]
    assessment_tag['minscore'] = config['assessment']['minscore']
    assessment_tag['maxitems'] = config['assessment']['maxitems']
    assessment_tag['showhints'] = config['assessment']['showhints']
    top_tag.insert(len(lesson_files), assessment_tag)
    for lesson in lesson_files:
        if lesson == 'config.yaml' or lesson == 'unit.xml':
            continue
        item_tag = Tag(soup, 'item')
        item_tag['dataUrl'] = 'data/{0:>s}'.format(lesson)
        assessment_tag.insert(0, item_tag)

    #generage the description tag
    if unit_name in config.keys():
        description = NavigableString('<![CDATA[<div>{0:>s}</div>]]>'.format(config[unit_name]))
    elif 'description' in config.keys():
        description = NavigableString('<![CDATA[<div>{0:>s}</div>]]>'.format(config['description']))
    else:
        description = NavigableString('')
    desc_tag = Tag(soup, 'description')
    desc_tag.insert(0, description)
    top_tag.insert(len(lesson_files) + 1, desc_tag)

    fd = open(os.path.join(basedir, 'data', 'unit.xml'), 'w')
    fd.write('<?xml version="1.0" encoding="UTF-8"?>\n' + soup.prettify())
    fd.close()


def build_unit_xml2(language_data, basedir, config):
    '''accepts language data as a dictionary and a basedir for the unit.xml to be generated in.
    '''
    translit_state = str(config['isTranslit']).lower()
    lesson_files = os.listdir(basedir)

    root = etree.Element('cw1Unit')
    #root.attrib['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
    #root.attrib['xsi:noNamespaceSchemaLocation'] = 'cw1Unit_schema.xsd'
    knownLanguage = os.path.split(os.path.split(os.path.split(os.path.split(basedir)[0])[0])[0])[1]
    knownLanguage = knownLanguage[6:]
    knownLanguage = knownLanguage.replace("Speakers", "")
    knownLanguage = knownLanguage.replace("speakers", "")
    knownLanguage = knownLanguage.replace(" ", "")
    unit_name = config["name"].replace('-', ' ') #os.path.split(basedir)[1].replace('-', ' ')
    root.attrib['name'] = config["name"].replace('-', ' ') #os.path.split(os.path.split(basedir)[0])[1].replace('-', ' ')
    root.attrib['knownLanguage'] = knownLanguage.upper()
    root.attrib['learningLanguage'] = language_data['code']
    root.attrib['learningFontUrl'] = 'fonts/{0:s}.swf'.format(language_data['font'])
    root.attrib['uiFont'] =  'fonts/{0:s}.swf'.format(knownLanguageValues[knownLanguage.upper()]['uiFont'])
    root.attrib['knownFont'] = 'fonts/{0:s}.swf'.format(knownLanguageValues[knownLanguage.upper()]['knownFont'])
    if 'rtl' in language_data.attrMap:
        root.attrib['isRTL'] = language_data['rtl']
    else:
        root.attrib['isRTL'] = 'false'
    root.attrib['transliterated'] = translit_state
    if 'hasalphabet' in language_data.attrMap:
        root.attrib['hasAlphabet'] = language_data['hasalphabet']
    else:
        root.attrib['hasAlphabet'] = 'false'
    if 'hasscriptassistant' in language_data.attrMap:
        root.attrib['hasScriptAssistant'] = language_data['hasscriptassistant']
    else:
        root.attrib['hasScriptAssistant'] = 'false'
    root.attrib['formatversion'] = '1'

    lesson_counter = 1
    new_lesson_files = {}
    if config['isESLTrue']:
        for lesson in lesson_files:
            if lesson[12:] in config['lessonListMap'].keys():  #config['lessonListMap'][lesson[12:]]
                new_lesson_files.update({config['lessonOrder'].index(lesson[12:]): [config['lessonListMap'][lesson[12:]], lesson]})
    else:
        for lesson in lesson_files:
            if lesson[12:] in config['lessonOrder']:
                new_lesson_files.update({config['lessonOrder'].index(lesson[12:]): [lesson[12:], lesson]})
    new_lesson_files = collections.OrderedDict(new_lesson_files)
    for lesson in new_lesson_files:
        lesson = new_lesson_files[lesson]
        if lesson[1] == 'config.yaml' or lesson[1] == 'unit.xml':
            continue
        lesson_tag = etree.SubElement(root, 'lesson')
        lesson_tag.attrib['name'] = lesson[0].replace("-", " ")
        counter = 0
        activity_group = 'activities'
        if 'TLX' in lesson:
            activity_group = 'tlx_activities'

        for activity in config[activity_group]:
            if activity == "Pronunciation" or activity == "MultipleChoice2":
                activity_tag = etree.SubElement(lesson_tag, 'activity')
                config_tag = etree.SubElement(activity_tag, 'config')
                config_tag.attrib['speech'] = 'true'
                activity_tag.attrib['required'] = 'false'
                if config["isESLTrue"]:
                    activity_tag.attrib['name'] = eslActivityNames[knownLanguage][activity]
                else:
                    activity_tag.attrib['name'] = activityName[activity] #'Lesson {0:d}'.format(lesson_counter)
                activity_tag.attrib['moduleUrl'] = 'modules/{0:s}.swf'.format(activity)
                activity_tag.attrib['dataUrl'] = 'data/{0:s}'.format(lesson[1])
                if activity in byki_modes:
                    activity_tag.attrib['isB4u'] = u'true'
                else:
                    activity_tag.attrib['isB4u'] = u'false'
                counter += 1
            else:
                activity_tag = etree.SubElement(lesson_tag, 'activity')
                activity_tag.attrib['required'] = 'false'
                activity_tag.attrib['name'] = activityName[activity] #'Lesson {0:d}'.format(lesson_counter)
                activity_tag.attrib['moduleUrl'] = 'modules/{0:s}.swf'.format(activity)
                activity_tag.attrib['dataUrl'] = 'data/{0:s}'.format(lesson[1])
                if activity in byki_modes:
                    activity_tag.attrib['isB4u'] = u'true'
                else:
                    activity_tag.attrib['isB4u'] = u'false'
                counter += 1
        lesson_counter += 1

    assessment_tag = etree.SubElement(root, 'assessment')
    assessment_tag.attrib['name'] = 'Assessment'
    module_str = ''
    for module in config['assessment']['modules']:
        module_str += 'modules/{0:s}.swf,'.format(module)
    assessment_tag.attrib['moduleUrl'] = module_str[:-1]
    assessment_tag.attrib['minscore'] = str(config['assessment']['minscore'])
    assessment_tag.attrib['maxitems'] = str(config['assessment']['maxitems'])
    assessment_tag.attrib['showhints'] = str(config['assessment']['showhints']).lower()
    for lesson in new_lesson_files:
        lesson = new_lesson_files[lesson]
        if lesson[1] == 'config.yaml' or lesson[1] == 'unit.xml':
            continue
        item_tag = etree.SubElement(assessment_tag, 'item')
        item_tag.attrib['dataUrl'] = 'data/{0:s}'.format(lesson[1])
    if unit_name in config.keys():
        description = config[unit_name]
    elif 'description' in config.keys():
        description = config['description']
    else:
        description = ''
    desc_tag = etree.SubElement(root, 'description')
    description = "<span whiteSpaceCollapse='preserve'>" + description + "</span>"
    desc_tag.text = etree.CDATA(description)

    fd = open(os.path.join(basedir, 'unit.xml'), 'w+')
    fd.write(lxml.etree.tostring(root, method='xml', encoding='UTF-8', pretty_print=True, xml_declaration=True))
    fd.close()


def get_configuration(basedir):
    '''gets the activities from the config file and returns it as a list.
    '''
    stream = file(os.path.join(basedir, 'config.yaml'))
    config = yaml.load(stream)
    stream.close()
    return config