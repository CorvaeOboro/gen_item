#import stylegan2-ada-pytorch.generate as stylegan2adagen
import random
import datetime
import subprocess
import os.path
from os import path
from os.path import abspath
import requests

# GEN_ITEM CHECKPOINT GITHUB URL and FILEPATH
checkpoint_url_start = '''https://github.com/CorvaeOboro/gen_item/releases/download/'''

ring_checkpoint_url = '''gen_item_ring_stylegan2ada_20230218/gen_item_ring_stylegan2ada_20230218.pkl'''
ring_checkpoint_filepath ="./checkpoints/gen_item_ring_stylegan2ada_20230218.pkl"
potion_checkpoint_url = '''gen_item_potion_stylegan2ada_20230430/gen_item_potion_stylegan2ada_20230430.pkl'''
potion_checkpoint_filepath ="./checkpoints/gen_item_potion_stylegan2ada_20230430.pkl"

def get_gen_item_checkpoints(checkpoint_filepath_input,checkpoint_url_input):
        # DOWNLOAD ITEM trained network checkpoint pkl
        network=checkpoint_filepath_input
        if path.exists(network) :
                print("EXISTING PKL FOUND == " + str(network))
        else:
                save_output_path = "./checkpoints/"
                try: 
                        os.mkdir(save_output_path) 
                except OSError as error: 
                        print(error)  
                network_absolute = abspath(network)
                print("GEN ABILITY PKL MISSING  == " + str(network_absolute))
                network_url = checkpoint_url_start + checkpoint_url_input
                print("DOWNLOAD PKL  == " + str(network_url))
                response = requests.get(network_url)
                print("DOWNLOADING....")
                with open(network_absolute, 'wb') as f:
                        f.write(response.content)
                print("====DOWNLOAD ABILITY ICON pkl COMPLETED====")

def gen_item_generate(checkpoint_filepath):
        # RANDOM SEED
        now = datetime.datetime.now()
        timebased_seed = int(now.strftime("%Y%m%d%H%M%S"))
        random.seed(timebased_seed)
        random_seed = int(random.random()*2147483648.0)

        # GENERATE MULTIPLE ITEMS
        total_items = 100
        truncation = 0.5  # truncation is like chaos , 0 = average 1 = furthest outliers of network
        random_seed_end = random_seed + total_items
        seeds_final = str(random_seed) +"-" +str(random_seed_end)

        # OUTPUT FOLDER
        outdir="./output"
        try: 
                os.mkdir(outdir) 
        except OSError as error: 
                print(outdir + "  EXISTS")  

        # GENERATE STYLEGAN2ADA SEEDS //=====================================================
        stylegan2ada_generate="./stylegan2-ada-pytorch/generate.py"
        if path.exists(stylegan2ada_generate) :
                print("EXISTING STYLEGAN2ADA FOUND == " + str(stylegan2ada_generate))
                p = subprocess.call(['python', 'stylegan2-ada-pytorch/generate.py', '--seeds', str(seeds_final), '--trunc', str(truncation), '--outdir', str(outdir), '--network', str(checkpoint_filepath)])
        else:
                print("==== ERROR - STYLEGAN2ADAPYTORCH NOT FOUND , GIT CLONE ====")


get_gen_item_checkpoints(ring_checkpoint_filepath,ring_checkpoint_url)
get_gen_item_checkpoints(potion_checkpoint_filepath,potion_checkpoint_url)
gen_item_generate(ring_checkpoint_filepath)
gen_item_generate(potion_checkpoint_filepath)