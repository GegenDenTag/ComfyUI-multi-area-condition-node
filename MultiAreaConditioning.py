# 02/04/2023 Made by Davemane42#0042 for ComfyUI 
# 2024-11-09 Fix gdt
# https://github.com/comfyanonymous/ComfyUI/issues/5425
# 2025-06-12 MultiAreaConditioning.js 
#   Add Canvas last so it appears after the input(control) widgets

import torch
from nodes import MAX_RESOLUTION # 16384 == 2^14 Why... 😁

class MultiAreaConditioning:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        data_in = {
            "required": {
                "conditioning0": ("CONDITIONING", ),
                "conditioning1": ("CONDITIONING", )
            },
            "hidden": {"extra_pnginfo": "EXTRA_PNGINFO", "unique_id": "UNIQUE_ID"},
        }
    
        return data_in
    
    RETURN_TYPES = ("CONDITIONING", "INT", "INT")
    RETURN_NAMES = ("CONDITIONING", "resolutionX", "resolutionY")
    FUNCTION = "apply_node"
    CATEGORY = "gdt"

    def apply_node(self, extra_pnginfo, unique_id, **kwargs):

        c = []
        values = []
        resolutionX = 1024
        resolutionY = 1024

        for node in extra_pnginfo["workflow"]["nodes"]:
            if node["id"] == int(unique_id):
                values = node["properties"]["values"]
                resolutionX = node["properties"]["width"]
                resolutionY = node["properties"]["height"]
                break
        k = 0
        for arg in kwargs:
            if k > len(values): 
                break
            if not torch.is_tensor(kwargs[arg][0][0]): 
                continue
            
            x, y = values[k][0], values[k][1]
            w, h = values[k][2], values[k][3]

            # If fullscreen
            if (x == 0 and y == 0 and w == resolutionX and h == resolutionY):
                for t in kwargs[arg]:
                    c.append(t)
                k += 1
                continue
            
            if x+w > resolutionX:
                w = max(0, resolutionX-x)
            
            if y+h > resolutionY:
                h = max(0, resolutionY-y)

            if w == 0 or h == 0: 
                continue

            for t in kwargs[arg]:
                n = [t[0], t[1].copy()]
                n[1]['area'] = (h // 8, w // 8, y // 8, x // 8)
                n[1]['strength'] = values[k][4]
                n[1]['min_sigma'] = 0.0
                n[1]['max_sigma'] = 99.0                
                c.append(n)            
            k += 1

        return (c, resolutionX, resolutionY)