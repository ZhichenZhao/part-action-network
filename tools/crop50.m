function [ out ] = crop50(I,bndbox)
%CROP50 Summary of this function goes here
%   Detailed explanation goes here
centerx=(bndbox(1)+bndbox(3))/2;
centery=(bndbox(2)+bndbox(4))/2;
width=bndbox(3)-bndbox(1);
height=bndbox(4)-bndbox(2);
width50=round(width*1.5);
height50=round(height*1.5);
x_leftup=centerx-round(width50/2);
y_leftup=centery-round(height50/2);
out=imcrop(I,[x_leftup y_leftup width50 height50]);
end

