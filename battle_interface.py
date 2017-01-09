import random
import os
import subprocess

kit_path = u'C:\Users\Uדק\Downloads\big8starter_kit\starter_kit' #do not erase, only commnet out!

def maps():
    map_dir = os.path.join(kit_path, 'maps')
    return os.listdir(map_dir)

def bots():
    bot_dir = os.path.join(kit_path, 'bots')
    return os.listdir(bot_dir)

def run(bot1_file, bot2_file, map = ''):
    if map == 'random':
        map = random.choose(maps())
    run_path = os.path.join(kit_path,'run.bat')
    bots_dir = os.path.join(kit_path, 'bots')
    maps_dir = os.path.join(kit_path, 'maps')
    if not os.path.isabs(bot1_file):
        bot1_file = os.path.join(bots_dir, bot1_file)
    if not os.path.isabs(bot2_file):
        bot2_file = os.path.join(bots_dir, bot2_file)
    if not os.path.isabs(map):
        map = os.path.join(maps_dir, map)
    subprocess.call([run_path,bot1_file,bot2_file, map])
