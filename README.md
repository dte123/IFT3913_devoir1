# IFT3913_devoir1

## Name
Yu Deng 20151659

## Explanation
The whole is written in python, and the right side shows that java occupies 99% because the jfreechart file is too large

## Requirements
This project requires Python 3.10 installed on your system

## Git Repo
https://github.com/dte123/IFT3913_devoir1.git

## Running The Code
> On Linux /MacOS 
1. Open this code directory in terminal(Linux/MacOS)
2. Run `python3 main.py`
3.  Follow the prompts to accomplish any tasks

> On Windows
1. Open this code directory on Command Prompt
2. Run `py main.py`
3. Follow the prompts to accomplish any tasks



## File Structure
> `main.py` - This file contains functions to run all the other files

>`jls/main.py` -  This contains the functionality of Part 0 of the assignment. When called the function expects folder path as input argument and returns `list` of `dict`s which contains the required `file_path`, `filename`, and `class name`

>`nvloc/main.py` -  This contains the functionality of Part 1 of the assignment. When called the function expects file path as input argument and returns `nvloc` of the supplied file

>`lcsec/main.py` -  This contains the functionality of Part 2 of the assignment. When called the function expects folder path as input argument and returns `list` of `dict`s which contains the required `file_path`, `filename`, `class name` and corresponsing `csec` value

>`egon/main.py` -  This contains the functionality of Part 3 of the assignment. When called the function expects folder path as input argument and returns `list` of `dict`s which contains the required `file_path`, `filename`, `class name` and corresponsing `csec` and `nvloc` values


## Testing and Running
### 1. Part 0 - JLS Program
Function to test the running of the Program
![JLS Test](./screenshots/jls_test.png)
The snapshot of the output below proves it produced an accurate output
![JLS Output](./screenshots/jls_output.png)


---

### 2. Part 1 - NVLOC Program
Function to test the running of the Program
<img src="./screenshots/nvloc_input.png" width="200%">
The snapshot of the output below proves it produced an accurate output
<img src="./screenshots/nvloc_output.png" width="200%">
<hr />

### 3. Part 2 - LCSEC Program
Function to test the running of the Program
<img src="./screenshots/lcsec_test.png" width="200%">
The snapshot of the output below proves it produced an accurate output
<img src="./screenshots/lcsec_output.png" width="200%">
<hr />
