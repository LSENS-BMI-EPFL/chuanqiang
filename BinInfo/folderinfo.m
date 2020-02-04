% Author: Chuanqiang Zhang
% Date: 04/02/2020

function [Files nID]=folderinfo(folder_name)
% Used to display Bin Files
% How to use
% input    folder path
% output   file information and total count

%folder_name = 'C:\CZ_BHV';   % '' or "" maters
%folder_name = 'C:\CZ_BHV\CZ003\20191031\141209\';   % '' or "" maters

Files=dir([folder_name,'\','LickTrace*.bin']);
nID=length(Files);
for k=1:length(Files)
   FileNames=Files(k).name;
end
end
