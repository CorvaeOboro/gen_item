# GEN_ITEM
create item images , a circular workflow of refinement using procgen augmented by neural networks .
- [DOWNLOAD](https://github.com/CorvaeOboro/gen_item/archive/refs/heads/master.zip) |  [VIEW ITEMS](https://corvaeoboro.github.io/gen_item/gen_item_ring_all.htm) |  [INSTALL](#install) 
- procedurally generated 3d renders using [SideFX's Houdini](https://www.sidefx.com/) tools and [PDG TOPs](https://www.sidefx.com/products/pdg/) 
- mutated by text-to-image guided neural networks ( [VQGAN+CLIP](https://github.com/CompVis/taming-transformers) , [STABLEDIFFUSION]( https://github.com/Stability-AI/stablediffusion)
- cultivated dataset trained generative adversarial network to generate new variants (  [STYLEGAN2ADA](https://github.com/NVlabs/stylegan2-ada)  )

| <a href="https://corvaeoboro.github.io/gen_item/gen_item_ring_all.htm"> <img src="/docs/ring/item_ring_thumb.jpg?raw=true" width="200" height="200" /> </a>| <a href="https://corvaeoboro.github.io/gen_item/gen_item_potion_all.htm"> <img src="/docs/potion/item_potion_thumb.jpg?raw=true" width="200" height="200" />  </a>  |  <a href="https://corvaeoboro.github.io/gen_item/gen_item_helm_all.htm"> <img src="/docs/helm/item_helm_thumb.jpg?raw=true" width="200" height="200" />  </a>  | 
| :---: | :---: | :---: | 
|  [ring](https://corvaeoboro.github.io/gen_item/gen_item_ring_all.htm) |  [potion](https://corvaeoboro.github.io/gen_item/gen_item_potion_all.htm)  |  [helm](https://corvaeoboro.github.io/gen_item/gen_item_helm_all.htm)  | 

![item_ring_process_single](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_process_single.jpg?raw=true "item_ring_process_single")
![item_potion_process_single](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/potion/item_potion_process_single.jpg?raw=true "item_potion_process_single")
![item_helm_process_single](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/helm/item_helm_process_single.jpg?raw=true "item_helm_process_single")


# IMAGE DATASET
- a synthetic image dataset of fantasy items
- collection of favored items generated free to all 
- [DOWNLOAD IMAGES](https://github.com/CorvaeOboro/gen_item/archive/refs/heads/master.zip)  | [VIEW ITEMS](https://corvaeoboro.github.io/gen_item/gen_item_ring_all.htm) 
![item_ring_stylegan2ada_20230218_comp](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_stylegan2ada_20230218_comp.jpg?raw=true "item_ring_stylegan2ada_20230218_comp")

# STYLEGANADA CHECKPOINT
- stylegan2 network checkpoints trained on synthetic 1024x1024 images of generated selections .
- create new seeds using these notebooks or spaces :

| item | generate | fid | dataset | date | color_distribution | 
| :---: | :--- | :--- | :--- | :--- | :--- | 
| ring |[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/CorvaeOboro/gen_item_ring)  | 14.9 | 3953 | 20230427 | <img src="docs/ring/item_ring_color_graph.jpg?raw=true"  />| 
| potion |[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/CorvaeOboro/gen_item_potion) | 9.24 | 4413 | 20230218 | <img src="docs/potion/item_potion_color_graph.jpg?raw=true" />|  
| helm | space | 14.7 | 2818 | 20221013 | <img src="docs/helm/item_helm_color_graph.jpg?raw=true" />| 

![item_ring_stylegan2ada_20220618_comp_2](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_stylegan2ada_20220618_comp_2.jpg?raw=true "item_ring_stylegan2ada_20220618_comp_2")

# PROCGEN
- houdini hda tools generate 3d randomized items as a base
- included hip files setup with PDG TOPs , rendering randomized wedging  to generate the dataset
- utilizes [SideFXLabs](https://github.com/sideeffects/SideFXLabs) hda tools and [ZENV](https://github.com/CorvaeOboro/zenv) hda tools 
![item_ring_procgen](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_procgen.jpg?raw=true "item_ring_procgen")
![item_ring_pdgA_comp](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_pdgA_comp.jpg?raw=true "item_ring_pdgA_comp")

# MUTATION / REMIXING
- with initial set of procgen selected , expand the dataset and alter using multiple techniques :
- IMAGE_COLLAGE.py - given a folder of images randomly composites them with randomized color / brightness  
- z_MLOP_COLOR_GRADIENT_VARIANT.hda - given a folder of images , generates randomized color gradient variations 
- IMAGE_TEXTURIZER.py - overlay texture dataset , using subcomponent datasets for example fluids for potions , and metals for shields . 
- VQGAN+CLIP and STABLEDIFFUSION - text-to-image guided modification of input image , prompts generated from included wildcard txt files 
![item_ring_stablediffusion_20220915_comp](https://raw.githubusercontent.com/CorvaeOboro/gen_item/master/docs/ring/item_ring_stablediffusion_20220915_comp.jpg?raw=true "item_ring_stablediffusion_20220915_comp")

# INSTALL

```.bash
#open anaconda as admin
#clone gen_item
git clone 'https://github.com/CorvaeOboro/gen_item'
cd gen_item
#create conda venv from included environment.yml
conda env create --prefix venv -f environment.yml
conda activate C:/FOLDER/gen_item/venv

#clone STYLEGAN2ADA
git clone "https://github.com/NVlabs/stylegan2-ada-pytorch"

#clone VQGANCLIP 
git clone "https://github.com/openai/CLIP"
git clone "https://github.com/CompVis/taming-transformers"

#download VQGAN checkpoint imagenet 16k
mkdir checkpoints
curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384

# generate new seeds from checkpoints
python gen_item_stylegan2ada_generate.py
```
stylegan2ada requires CUDA https://developer.nvidia.com/cuda-11.3.0-download-archive

# WORKFLOW
- generate procgen renders from houdini , selecting favored renders
```.bash
# procgen houdini pdg render , requires houdini and zenv tools
python gen_item_houdini_render.py
```
- generate prompts for text2image mutation 
```.bash
# vqgan+clip text2image batch alter from init image set
python prompts/text_word_combine_complex.py  
```
- mutate those renders via text guided VQGAN+CLIP 
```.bash
# vqgan+clip text2image batch alter from init image set
python gen_item_vqganclip.py  
python gen_item_vqganclip.py --input_path="./item/ring" --input_prompt_list="./prompts/prompts_ring.txt" 
```
- combine the renders and mutants via random collaging 
```.bash
# collage from generated icon set
python gen_item_collage.py
python gen_item_collage.py --input_path="./item/ring" --resolution=1024
```
- select the favored icons to create a stylegan2 dataset 
- train stylegan2 network , then generate seeds from trained checkpoint
```.bash
# stylegan2ada generate from trained icon checkpoint
python gen_item_stylegan2ada_generate.py
```
- cultivate the complete dataset thru selection and art direction adjustments 
- repeat to expand and refine by additional text guided mutation , retraining , regenerating

# CHANGELIST
- 20230430 = added potion stylegan2ada checkpoint gen 5 
- 20230218 = added ring stylegan2ada checkpoint gen 7 
- 20221016 = added helm stylegan2ada checkpoint gen 3 

# THANKS
many thanks to 
- NVIDIA NVLabs - https://github.com/NVlabs/stylegan2-ada
- CLIP - https://github.com/openai/CLIP
- VQGAN - https://github.com/CompVis/taming-transformers
- Katherine Crowson : [https://github.com/crowsonkb](https://github.com/crowsonkb)  https://arxiv.org/abs/2204.08583
- NerdyRodent : https://github.com/nerdyrodent/VQGAN-CLIP

# AKNOWLEDGEMENTS
```
@inproceedings{Karras2020ada,
  title     = {Training Generative Adversarial Networks with Limited Data},
  author    = {Tero Karras and Miika Aittala and Janne Hellsten and Samuli Laine and Jaakko Lehtinen and Timo Aila},
  booktitle = {Proc. NeurIPS},
  year      = {2020}
}
```
```
@misc{esser2020taming,
      title={Taming Transformers for High-Resolution Image Synthesis}, 
      author={Patrick Esser and Robin Rombach and Björn Ommer},
      year={2020},
      eprint={2012.09841},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
```
@misc{https://doi.org/10.48550/arxiv.2103.00020,
  doi = {10.48550/ARXIV.2103.00020},
  url = {https://arxiv.org/abs/2103.00020},
  author = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and Krueger, Gretchen and Sutskever, Ilya},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Learning Transferable Visual Models From Natural Language Supervision},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## CREATIVE COMMONS ZERO ##
free to all , [creative commons CC0](https://creativecommons.org/publicdomain/zero/1.0/) , free to redistribute , no attribution required