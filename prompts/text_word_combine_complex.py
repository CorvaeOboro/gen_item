# COMBINE WORDS FROM MULTIPLE LISTS FOR PROMPT
# like tapestry style random generation
# pip install tracery
import os
import numpy as np
import time
import random
from itertools import product, permutations
import tracery

# //==================================================
#// VARIABLES
total_generated = 2
path_sword = "/prompts/sword/"
path_ring = "/prompts/ring/"
path_helm = "/prompts/helm/"
path_character = "/prompts/character/"
path_ui = "/prompts/ui/"
path_staff= "/prompts/staff/"
path_shield = "/prompts/shield/"
path_potion = "/prompts/potion/"
path_gloves = "/prompts/gloves/"
path_face = "/prompts/face/"

# //==================================================
#// INPUT TEXT LIST FUNCTION
def input_text_list(input_textfile):
    print("LOADING == " + str(input_textfile))
    inputfile = input_textfile
    textfile_input = open(inputfile, 'r')
    multi_text_prompt=[]
    Lines = textfile_input.readlines()
    # Strips the newline and space character
    for line in Lines:
        if (line.strip() != ''):
            currentline_stripped = line.strip()
            multi_text_prompt.append(currentline_stripped)
    print(multi_text_prompt)
    return multi_text_prompt
            
def gen_item_base(item_name):
    path_item = "/" + str(item_name) + "/"
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_item + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_item + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_item + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts_' + str(item_name) + '.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + "  " + str(item_name))
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //==================================================
#// TRACERY RANDOMIZED TEXT GEN for CHARACTER
def gen_character():
    listOfStr = ['text','input','human','hair','clothes','addons','modifier','type','lighting','artist']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#input# #human# with #hair# , and wearing #clothes# , and #addons# , #modifier#,  #modifier#,  #modifier#, #lighting# , art by #artist#"
    rules["input"]=input_text_list('./' + path_character + '/input.txt')
    rules["human"]=input_text_list('./' + path_character + '/human.txt')
    rules["hair"]=input_text_list('./' + path_character + '/hair.txt')
    rules["clothes"]=input_text_list('./' + path_character + '/clothes.txt')
    rules["addons"]=input_text_list('./' + path_character + '/addons.txt')
    rules["modifier"]=input_text_list('./' + path_character + '/modifier.txt')
    rules["type"]=input_text_list('./' + path_character + '/type.txt')
    rules["lighting"]=input_text_list('./' + path_character + '/lighting.txt')
    rules["artist"]=input_text_list('./' + path_character + '/artist.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_character.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " CHARACTERS")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")


# //==================================================
#// TRACERY RANDOMIZED TEXT GEN for CHARACTER
def gen_face():
    listOfStr = ['text','input','human','modifier','lighting','artist']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    #rules["text"]="#input# #input# , #modifier# ,  #modifier# ,  #modifier# , #lighting# , by #artist# and #artist#"
    rules["text"]="a photo of beautiful female face , #human# , #human# , #input# , #modifier# ,  #modifier# ,  #modifier# , #lighting# , ulzzang idol , symmetrically centered , realism , award winning photo , perfect skin makeup , sharp focus , cinematic lighting"
    rules["input"]=input_text_list('./' + path_face + '/input.txt')
    rules["human"]=input_text_list('./' + path_face + '/human.txt')
    rules["modifier"]=input_text_list('./' + path_face + '/modifier.txt')
    rules["lighting"]=input_text_list('./' + path_face + '/lighting.txt')
    rules["artist"]=input_text_list('./' + path_face + '/artist.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_face.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " FACES")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_helm():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_helm + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_helm + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_helm + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_helm.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " HELMS")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")


# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_ring():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    #rules["text"]="#object# made of #material# , of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["text"]="#object# of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_ring + '/object.txt')
    rules["material"]=input_text_list('./' + path_ring + '/material.txt')
    #rules["adjective"]=input_text_list('./' + path_ring + '/adjective.txt')
    rules["modifier"]=input_text_list('./' + path_ring + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_ring + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_ring.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " RINGS")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for SWORD
def gen_sword():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    #rules["text"]="#object# made of #material# , of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["text"]="#object# made of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_sword + '/object.txt')
    rules["material"]=input_text_list('./' + path_sword + '/material.txt')
    #rules["adjective"]=input_text_list('./' + path_ring + '/adjective.txt')
    rules["modifier"]=input_text_list('./' + path_sword + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_sword + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_sword.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " SWORDS")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for STAFF
def gen_staff():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# made of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_staff + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_staff + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_staff + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_staff.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " STAFF")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_shield():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# made of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_shield + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_shield + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_shield + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_shield.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " SHIELD")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_potion():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# made of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_potion + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_potion + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_potion + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_potion.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " POTIONS")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_gloves():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]="#object# made of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#"
    rules["object"]=input_text_list('./' + path_gloves + '/object.txt')
    rules["modifier"]=input_text_list('./' + path_gloves + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_gloves + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_gloves.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " GLOVES")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

# //=======================================================================================================
#// TRACERY RANDOMIZED TEXT GEN for HELM
def gen_ui():
    listOfStr = ['text','object','modifier','render']
    rules = dict.fromkeys(listOfStr , 1)
    print("RULES DICTIONARY == " + str(rules))
    rules["text"]=["#object# #material# of #modifier# and #modifier# , sharp focus , cinematic lighting , #render#","#object# #material# of #modifier# , sharp focus , cinematic lighting , #render#"]
    #rules["text"].append("#object# #material# of #modifier# , sharp focus , cinematic lighting , #render#")
    rules["object"]=input_text_list('./' + path_ui + '/object.txt')
    rules["material"]=input_text_list('./' + path_ui + '/material.txt')
    #rules["adjective"]=input_text_list('./' + path_ring + '/adjective.txt')
    rules["modifier"]=input_text_list('./' + path_ui + '/modifier.txt')
    rules["render"]=input_text_list('./' + path_ui + '/render.txt')
    print("RULES FINAL DICTIONARY == " + str(rules))

    grammar = tracery.Grammar(rules)
    grammar.flatten("#text#")

    #// TEXT OUTPUT START WRITING
    output_textfile = './prompts/prompts_ui.txt'
    textfile_output_final = open(output_textfile, 'w')
    time.sleep(1.0)
    i = 0
    print("GENERATING " + str(total_generated) + " UI")
    while i < total_generated:
        final_text = grammar.flatten("#text#")
        textfile_output_final.write(str(final_text))
        textfile_output_final.write('\n') # newline
        time.sleep(0.01)
        i = i+1
    time.sleep(2.0)
    textfile_output_final.close
    time.sleep(2.0)
    print("+++++++++++ COMPLETE +++++++++++++")

#//================================================================
#// OLD MAIN LOOP
def old_main_loop():
    i = 0
    while i < total_generated:
        random.shuffle(current_wordlist)
        current_word = current_wordlist[0]
        if current_word != None :
            current_secondwordlist = current_wordlist
            random.shuffle(current_secondwordlist)
            current_combo_word = current_word + " " + current_secondwordlist[1] + " " + current_secondwordlist[2] + " " + current_secondwordlist[3]+ " " + current_secondwordlist[4]+ " " + current_secondwordlist[5]+ " " + current_secondwordlist[6]+ " " + current_secondwordlist[7]
            
            textfile_output_final.write(current_combo_word)
            textfile_output_final.write('\n') # newline
            i = i+1

    time.sleep(2.0)


#// ITEMS===================================
gen_item_base("amulet")
gen_item_base("helm")
gen_item_base("ring")
gen_item_base("sword")
gen_item_base("staff")
gen_item_base("potion")
gen_item_base("glove")
gen_item_base("hammer")
gen_item_base("chest")
gen_item_base("focus")
gen_item_base("shield")

print("+++++++++++ COMPLETE +++++++++++++")