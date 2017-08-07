# part-action-network

This project descibes the Part Action Network proposed in our paper in ICCV2017: Single Image Action Recognition using Semantic Part Actions, Zhichen Zhao, Huimin Ma and Shaodi You.

In general, the main purpose of this paper is to capture "part action" cues to improve the body action recognition. We view a body action as a combination of several part actions.


## Part actions
we define 5 kinds of parts: head, torso, lower body, two arms and two hands. For each of them, we define some actions, such as "head: lokking up", "hand: half holding" etc.

|index|part|action|
|:--------:|:--------:|:--------:|
|1|head|breathing|
|2|head|drinking|
|3|head|laughing|
|4|head|looking down|
|5|head|looking through|
|6|head|looking up|
|7|head|normal|
|8|head|speaking|
|9|head|brushing teeth|
|-|-|-|

The part action set we have collected is not perfect now, if you find annotation errors or you have good ideas on how to design the set, please feel free to contact me.

## Annotations
The annotations are provided as "txt" files, in each of them, we label part actions in order of head-torso-lower_body-left_arm-right_arm-left_hand-right_hand. Since in any case you need to locate part locations in the test phase by algprithms, we do not provide part locations in the training set, which keeps consistency for the part localization.

Use the following scripts to get annotations:

```
  ./get_annotations.sh
```
## Testing

### Models
coming soon
## Training
### Our modified Caffe
coming soon

