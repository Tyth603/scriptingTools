__author__ = 'S. P. Powers'

import os
import sys
import argparse
from BeautifulSoup import BeautifulStoneSoup
import unit_utilities



def parse_arguments():
    ''' parse_arguments sets up a Parser for the command line arguments.  The parsed results are then returned'''
    parser = argparse.ArgumentParser(description="Unit.xml generator for TL courseware products")
    parser.add_argument('-u', '--unit' ,action='store_true', default=False, help='use per unit configuration instead of per language')
    parser.add_argument('-b', '--batch', action='store_true', default=False, help='Execute in batch mode (multi language)')
    parser.add_argument('-p', '--path', help='path to the directory containing the unit directory', required=True)
    return parser.parse_args(sys.argv[1:])


def run_generator():
    '''run_generator will run the method  required to generate a unit.xml file for every subdirectory of a language
    directory, or if the -batch flag is enabled then for multiple language directories.  The name of the language
    directory must correspond to the language code entry, however does not need to be of correct case.  This is handled
    within the program.
    '''
    if args.batch:
        #run a batch of multiple languages
        if not os.path.isdir(args.path):
            sys.stderr.write('the path specified does not exist')
            sys.exit(2)
        for dir in os.listdir(args.path):
            if not os.path.isdir(os.path.join(args.path, dir)):
                continue
            lang_data = get_language_data(dir.upper())
            if lang_data is not None:
                for inner_dir in os.listdir(os.path.join(args.path, dir)):
                    if inner_dir != 'config.yaml' and os.path.isdir(os.path.join(args.path, dir, inner_dir)):
                        full_dir = os.path.join(args.path, dir, inner_dir)
                        if args.unit:
                            config = unit_utilities.get_configuration(os.path.join(args.path, dir, inner_dir))
                        else:
                            config = unit_utilities.get_configuration(os.path.join(args.path,dir))
                        if os.path.isdir(full_dir):
                            if config:
                                unit_utilities.build_unit_xml2(lang_data, full_dir, config)
    else:
        #run for a single language
        if not os.path.isdir(args.path):
            sys.stderr.write('the path specified does not exist')
            sys.exit(2)
        path1 = os.path.split(args.path)
        path = os.path.split(path1[0])
        if len(path)==1:
            if path.upper() == "CHINESE, MANDARIN":
                lang_data = get_language_data("MANDARIN")
            else:
                lang_data = get_language_data(path.upper())
        else:
            if path[1].upper() == "CHINESE, MANDARIN":
                lang_data = get_language_data("MANDARIN")
            else:
                lang_data = get_language_data(path[1].upper())

        if lang_data is not None:
            if not args.unit:
                config = unit_utilities.get_configuration(args.path)
                if config:
                    for dir in os.listdir(args.path):
                        if dir != 'config.yaml':
                            unit_utilities.build_unit_xml2(lang_data, os.path.join(args.path, dir), config)
            else:
                for dir in os.listdir(args.path):
                    if dir != 'config.yaml':
                        if dir.endswith(".b4u") is not True:
                            if dir != "OUTPUT_B4Xs_1":
                                config = unit_utilities.get_configuration(os.path.join(args.path, dir))
                                if config:
                                    unit_utilities.build_unit_xml2(lang_data, os.path.join(args.path, dir), config)
        else:
            print 'unable to find language data :('
            sys.exit()
    print 'Done :)'

def get_language_data(name):
    '''gets the language data for a particular language code from the language information xml parse tree'''
    return lang_tree.find(code=name)



if __name__ == "__main__":
    args = parse_arguments()
    f=open(os.path.join(os.path.dirname(sys.argv[0]), 'LanguageInfo.xml'), 'r')
    lang_tree = BeautifulStoneSoup(f)
    f.close()
    run_generator()