All credits to Daveman42 for this node; 
# Davemane42's [Custom Node](https://github.com/Davemane42/ComfyUI_Dave_CustomNode) for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 
the repository created by him was archived on April 2, 2024.

I experimented with various (newer, sometimes better) available alternatives but didn’t achieve the same results with older generations. Therefore, I adapted the custom node to prevent ComfyUI from freezing. Additionally, I removed the routines for automatic installation of the JavaScript files and instead registered the node in the ComfyUI Manager.
Thus, with the current version of ComfyUI, it is no longer necessary to perform an automatic installation in 'YourPath\ComfyUI_windows_portable\ComfyUI\web\extensions'.

https://github.com/comfyanonymous/ComfyUI/issues/5425#issuecomment-2448600231 
and
https://github.com/comfyanonymous/ComfyUI/issues/5425#issuecomment-2452987079

## Installation

### Option 1: Install via ComfyUI Manager
Open ComfyUI Manager and install the **Multi Area Conditioning** (author: **gdt**) custom node.

### Option 2: Install manually
cd ComfyUI/custom_nodes/<br />
git clone https://github.com/GegenDenTag/ComfyUI-multi-area-condition-node<br />
Start Comfyui

___
# MultiAreaConditioning 2.4  

Let you visualize the ConditioningSetArea node for better control  
<details close="close">
    <summary>Right click menu to add/remove/swap layers:</summary>
    <img src="./images/RightClickMenu.png">
</details>
Display what node is associated with current input selected<br />
(only works when the node itself is focused). 

<img src="./images/MultiAreaConditioning_node.png" width="608px">

___
### Example Workflow 

<img src="./images/Screenshot 2024-09-15 221005.png" width="608px">

<details>
    <summary>Workflows embedded in images</summary>
    <img src="./images/ComfyUI_01303_.png" alt="human walker, giant, bear(avatar)" width="608px"/>
    <img src="./images/ComfyUI_01304_.png" alt="human walker, giant, bear(avatar)" width="608px"/>
    <img src="./images/ComfyUI_01305_.png" alt="human walker, giant, bear(avatar)" width="608px"/>
    <img src="./images/ComfyUI_01306_.png" alt="human walker, giant, bear(avatar)" width="608px"/>
</details>

