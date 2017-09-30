clear all;
close all;
clc;
class={
'applauding',
'blowing_bubbles',
'brushing_teeth',
'cleaning_the_floor',
'climbing',
'cooking',
'cutting_trees',
'cutting_vegetables',
'drinking',
'feeding_a_horse',
'fishing',
'fixing_a_bike',
'fixing_a_car',
'gardening',
'holding_an_umbrella',
'jumping',
'looking_through_a_microscope',	
'looking_through_a_telescope',
'playing_guitar',
'playing_violin',
'pouring_liquid',
'pushing_a_cart',
'reading',
'phoning',
'riding_a_bike',
'riding_a_horse',
'rowing_a_boat',
'running',
'shooting_an_arrow',
'smoking',
'taking_photos',
'texting_message',
'throwing_frisby',
'using_a_computer',
'walking_the_dog',
'washing_dishes',
'watching_TV',
'waving_hands',
'writing_on_a_board',
'writing_on_a_book'};
%% read the data
for k=1:40
fid=fopen(['/w/datasets/stanford40/stanford40/ImageSplits/', class{k}, '_test.txt']);
num=1;
while(~feof(fid))
nn=fscanf(fid,'%s',1); 
name{num}=nn(1:end-4);
if(isequal(name{num},[]))
    name(num)=[];
    break;
end
%[order(num)]=fscanf(fid,'%d',1);
%[label(num)]=fscanf(fid,'%d',1);
num=num+1;
end
fclose(fid);
num=num-1;
boundingbox=zeros(num,4);
%% extract bndbox from xml files
imgdir= '/w/datasets/stanford40/stanford40/JPEGImages';
annodir='/w/datasets/stanford40/stanford40/XMLAnnotations';
num=num-1;
for m=1:num
x=xmlread(fullfile(annodir,[name{m},'.xml']));
obListItems = x.getElementsByTagName('bndbox');
bnd=zeros(1,4);
for i = 0 : obListItems.getLength-1 
thisItem = obListItems.item(i); 
childNode = thisItem.getFirstChild; 
%childNode = childNode.getNextSibling;
while ~isempty(childNode)   
  if childNode.getNodeType == childNode.ELEMENT_NODE ;  
     childNodeNm = char(childNode.getTagName);   
     childNodeData = char(childNode.getFirstChild.getData);
     
     if(strcmp(childNodeNm,'xmin'))
         bnd(i+1,1)=str2num(childNodeData);
     end
     if(strcmp(childNodeNm,'ymin'))
         bnd(i+1,2)=str2num(childNodeData);
     end
     if(strcmp(childNodeNm,'xmax'))
         bnd(i+1,3)=str2num(childNodeData);
     end
     if(strcmp(childNodeNm,'ymax'))
         bnd(i+1,4)=str2num(childNodeData);
     end
  end
  childNode = childNode.getNextSibling;
end
end
boundingbox(m,:)=bnd(1,:);
end

%% resize and store new image
storepat='/u/water/research/stanford40_boundingbox/';
ff=fopen([storepat class{k} '_test']);
if(ff==-1)
    mkdir([storepat class{k} '_test']);
end
for m=1:num
    %if(label(m)==0)
    I=imread(fullfile(imgdir,[name{m},'.jpg']));
    I=crop50(I,boundingbox(m,:));
    %[im_h,im_w,im_d]=size(I);
    %I = imresize(I, 300/max(im_h, im_w), 'bicubic');
   
    imwrite(I,fullfile([storepat class{k} '_test'],[name{m},'_','.jpg']));
   
    %end
end

end














        
        
        
        
        
        
