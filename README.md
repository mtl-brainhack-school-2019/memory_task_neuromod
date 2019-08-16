# memory_task_neuromod
![alt text][logo_neuromod]

[logo_neuromod]: https://raw.githubusercontent.com/mtl-brainhack-school-2019/memory_task_neuromod/master/logo_neuromod.jpg "Logo on web page"
![logo_neuromod.jpg] (logo_neuromod.jpg "Project Logo")
### The aim is to replicate the CIMA-Q memory task with open tools
#### Protocol: 15 images are randomly shown to subject in 1/4 of screen. 1 target image is shown twice. Subject must press a key when the                  repeated target image is displayed and indicate in wich quadrant it previously appeared.
##### {https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/projectAbstract.md "projectAbstract"}
## Prerequisites
### Download, extract (if compressed) and install Psychopy toolbox
#### N.B: You need to have a dedicated graphic card (in most cases) to display the experimental monitor created by the script.
{https://www.psychopy.org/download.html}
```python
s = pip install psychopy
```
### Download and extract the following folders from our drive.
{https://drive.google.com/drive/folders/1FbHI3wNBzHRyp8FSZ6wLiyWRXulq-mV9?usp=sharing}
#### From this Drive directory, download the clothing, food and furniture folders
#### Make sure these folders are in your current working directory alongside the python file
##### You can use the shutil module to easily navigate through directories (similar to how the Unix Shell commands work)
```python
s = import shutil
s = shutil.move(files,destination) #works just like the Unix Shell mv command
```
## Image stimuli preprocessing
### To make sure all images in a given directory (i.e. a semantic category) are formatted appropriately, execute the following function on the previously downloaded folders after extraction. I use the Spyder IDE to edit and run python files.

{https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/square_resize.py "Link to function script"}
```python
s = conda install -c anaconda spyder 
s = spyder square_resize.py
s = square_resize('categoryNameHere')
```
## Next objectives
- [] Create iterable trial logbook class (containing stimuli, position, key and time pressed
- [] Save the trial logbook in a convinient format
- [] Initiate a stimuli selection function to ensure proper randomization without replacement - except for trials target images
###### Determine if whether or not to define a special object class for target images
- [] Continue compiling creative commons complex images
 
