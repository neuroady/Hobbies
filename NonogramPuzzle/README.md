
# NonogramMaker
### NOTE: forked from [@LyndonFan](https://github.com/LyndonFan)'s [NonogramMaker](https://github.com/LyndonFan/NonogramMaker). I only made a few minor changes.  
Run `CreateNono.sh` to create nonograms of images present in `./images/` folder. Nonograms will be generated with default settings (see below). To change Nonogram encoding properties use [@LyndonFan](https://github.com/LyndonFan)'s guide below. You can choose colored or black and white Nonograms. You can also limit the size and number of colors in the Nonograms. Output folder is `./images/outputs/` and solutions are exported in `./images/solutions/`. 

**Warning**: Images with no background will color the Nonogram space (this issue will be resolved in future commits).

-----

This application turns a picture into a nonogram: black and white or coloured.

(link to introductory video: <a href="https://youtu.be/kH7u9wnF9EY">https://youtu.be/kH7u9wnF9EY</a>)

# Usage

`GenNonogram.py [-h] [-d MAXDIM] [-b] [-n [NUMCOLOR]] [-r [GETRESULT]] image`

- positional arguments:
  - `image`: path to image to be processed

- optional arguments:

  - `-h, --help`:
    show this help message and exit
  - `-d MAXDIM, --maxDim MAXDIM`:
    maximum no. of squares in any dimension in the nonogram (default = 80)
  - `--minDim MINDIM`:
    minimum no. of squares in any dimension in the nonogram (default = 20).
    
    Note if MAXDIM and MINDIM are in conflict (e.g. picture has dimensions 10x50, default max and min dims), then MINDIM will take priority (e.g. in this case the result will be 20x100).
  - `-b, --blackAndWhite`:
    indicate the image should be converted to black and white
  - `-n [NUMCOLOR], --numColor [NUMCOLOR], --numColour [NUMCOLOR]`:
    positive integer to denote the number of colors that should appear in your nonogram IN ADDITION to your background color. A 0 or negative integer means the algorithm will choose this number for you. (default = 0)
  - `-r [GETRESULT], --getResult [GETRESULT]`
    boolean to indicate whether you want a separate file containing the finished picture (default = True)
