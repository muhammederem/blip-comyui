from .nodes.nodes import *

NODE_CLASS_MAPPINGS = { 
    "Blip Processor Node": BlipProcessorNode,
    "Blip Display Node": BlipDisplayNode,
    # "Blip String Pair Display Node": ShowText,
    }
    
print("\033[34mComfyUI Tutorial Nodes: \033[92mLoaded\033[0m")