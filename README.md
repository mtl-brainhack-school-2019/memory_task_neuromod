# memory_task_neuromod
### The aim is to replicate the CIMA-Q memory task with open tools
#### Protocol: 15 images are randomly shown to subject in 1/4 of screen. 1 target image is shown twice. Subject must press a key when the                  repeated target image is displayed and indicate in wich quadrant it previously appeared.
## Prerequisites
### Download, extract (if compressed) and install Psychopy toolbox
{https://www.psychopy.org/download.html}
```python
s = pip install psychopy
```
### Download and extract the following folders from our drive.
## PLEASE, do not remove, add, or alter these folders in any way. These images represent a lot of work and are precious for the project.
{https://drive.google.com/drive/folders/1FbHI3wNBzHRyp8FSZ6wLiyWRXulq-mV9?usp=sharing}
#### From this Drive directory, download the clothing, food and furniture folders
#### Make sure these folders are in your current working directory alongside the python file
##### You can use the shutil module to easily navigate through directories (similar to how the Unix Shell commands work)
```python
s = import shutil
s = shutil.move(files,destination) #works just like the Unix Shell mv command
```
## Image stimuli preprocessing
### To make sure all images in a given directory (i.e. a semantic category) are formatted appropriately, execute the following function on the previously downloaded folders after extraction.
{https://github.com/mtl-brainhack-school-2019/memory_task_neuromod/blob/master/square_resize.py "Link to function script"}
```python
s = square_resize('categoryNameHere')
```

 
