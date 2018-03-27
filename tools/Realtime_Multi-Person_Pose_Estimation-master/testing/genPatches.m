

close all;
clc;
addpath('src'); 
addpath('util');
addpath('util/ojwoodford-export_fig-5735e6d/');

% For MPI, mode = 2. For COCO, mode = 1.
mode = 1;
param = config(mode);
model = param.model(param.modelID);
net = caffe.Net(model.deployFile, model.caffemodel, 'test');

%%
id=0;
close all;
savePath = '/space3/water/datasets/Stanford40/PartImages/';

pics = dir(['/space3/water/datasets/Stanford40/BboxImages']);
pics = pics(3:end);
    
for m = 1:length(pics)
    im_name = pics(m).name;
    oriImg = imread(['/space3/water/datasets/Stanford40/BboxImages/' im_name]);
    disp(im_name);
    if(size(oriImg,2)/2>size(oriImg,1))
         scale0 = 368/max(size(oriImg, 2));
    else
        scale0 = 368/max(size(oriImg, 1));
    end
    twoLevel = 1;
    [final_score, ~] = applyModel(oriImg, param, net, scale0, 1, 1, 0, twoLevel);
    vis = 0;
    if mode == 1
        [candidates, subset] = connect56LineVec(oriImg, final_score, param, vis);
    elseif mode == 2
        [candidates, subset] = connect43LineVec(oriImg, final_score, param, vis);
    end
    boxes = genBbox(oriImg, candidates,subset,hsv(7),vis);
    parts={'head', 'torso', 'legs', 'larm', 'rarm', 'lhand', 'rhand'};
    for j=1:length(parts)
        if(isfield(boxes,parts{j}))
            bbox=getfield(boxes,parts{j});
            patch=oriImg(bbox(2):bbox(4),bbox(1):bbox(3),:);
            imwrite(patch, [savePath im_name(1:end-4) '_' parts{j} '.jpg'], 'jpg');
            id=id+1;
        end
    end
    
end






