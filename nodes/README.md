# BLIP Custom Nodes for ComfyUI

This repository contains custom nodes for integrating BLIP (Bootstrapped Language-Image Pretraining) into ComfyUI for advanced image-based question answering and text generation.

## Features

- **BlipProcessorNode**: Processes an input image and answers up to 10 questions about it.
- **ListToTextNode**: Converts a list of strings into a single string, useful for formatting outputs.
- **Integration with Show Text Node**: Uses a custom script to display the results in ComfyUI.

## Installation

### Step 1: Clone the my Repository
Clone this repository into the `custom_nodes` directory of your ComfyUI installation:

```bash
cd path/to/ComfyUI/custom_nodes
git clone git@github.com:muhammederem/blip-comyui.git
```

### Step 2: Install Additional Nodes (Optional)

To enhance functionality, you can also install the ```ComfyUI-Custom-Scripts``` repository, which includes the ShowTextNode for displaying outputs:

```bash
cd path/to/ComfyUI/custom_nodes
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git
```

This script is optional but recommended for displaying question-answer outputs in a user-friendly format.

### Step 3: Restart ComfyUI
After cloning the repositories, restart ComfyUI to load the new nodes.

## How to Add Custom Nodes and Integrate

1. Ensure the cloned repositories are inside the custom_nodes folder of your ComfyUI installation.

2. Open ComfyUI and check the Blip category in the node menu. You should see the following nodes:

   - BlipProcessorNode
   - ListToTextNode
3. Drag and drop the nodes into your workflow as needed.

## How to Use the Blip Nodes

### BlipProcessorNode

**Inputs**:

- Image: Provide an input image (from an IMAGE node).
- Question: Specify a mandatory question (default: "What is in the image?").
- Optional Questions: Add up to 9 additional questions (optional).

**Outputs**:

A list of answers to the questions asked about the image.


### Example Workflow:
* Add an ```IMAGE``` node and load your image.
* Add a ```BlipProcessorNode``` and connect it to the IMAGE node.
* Enter your questions in the node's input fields.
* Connect the output of BlipProcessorNode to a ```ListToTextNode``` or ``ShowText`` for viewing results.
  
### ListToTextNode
**Inputs**:
* A list of strings (e.g., the answers from the BlipProcessorNode).

**Outputs**:
* A single text string, useful for further text-based workflows.


### ShowText (Optional)
 * Use the ```ShowText``` from the ```ComfyUI-Custom-Scripts``` repository to display the answers visually in the ComfyUI interface.

## How to Run the Workflow

1. Launch ComfyUI by running:
```bash
python main.py
```

2. Create a new workflow or open an existing one.
   * Add image loader node and connect it to the ```BlipProcessorNode```.
   * Add ```ListToTextNode``` connect with ```BlipProcessorNode``` and ```ShowText``` with ```ListToTextNode``` nodes to view the results.
  
3. Configure your questions in the ```BlipProcessorNode```.

4. Run the workflow and view the outputs.