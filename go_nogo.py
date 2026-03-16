##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

### INSTRUCTION ROUTINE ###
task_instruct_txt = """ 
In this task, you will see a series of images presented on the screen.
A cue will appear above each image telling you whether you should respond or not.
If you see a Go cue:
    Press the SPACEBAR as quickly as possible.
If you see a No go cue:
    Do NOT press any key and wait for the next trial.
Please try to respond as quickly and accurately as possible.
Press ENTER to begin the experiment.
 """

# Show instructions and wait until response (return)
task_instruct_txt = TextStim(win, task_instruct_txt, alignText='left', height=0.085)
task_instruct_txt.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        break  # break out of the loop!


# Initialize a (global) clock
clock = Clock()
f_list = f"/Users/shuhuiyang/Desktop/Lecture 7/HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1)
kb=Keyboard()

go = "Go"
nogo = "No go"

for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = "/Users/shuhuiyang/Desktop/Lecture 7/stimuli/" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"
        stim_txt1 = TextStim(win, nogo, pos=(0.0, 0.5))
    else: 
        correct = "go"
        stim_txt1 = TextStim(win, go, pos=(0.0, 0.5))
    im=ImageStim(win, path)    
    
    t_clock=Clock()
    response = "nogo"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
        stim_txt1.draw()
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    trial_foods['response']=response
    trial_foods['rt']= rt
    trial_foods['correct_response'] = correct

trial_foods.save(f"{p_name}_gonogo.csv")

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    
