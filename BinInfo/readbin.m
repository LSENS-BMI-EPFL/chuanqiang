% Author: Chuanqiang Zhang
% Date: 04/02/2020

clear all
clc

binpath='\\sv-07-056\CZ\Data_Local\CZ009\Recording\BHV\CZ009_20200120\124132' ;
[Files nID]=folderinfo(binpath);
[tmp ind]=natsortfiles({Files.name});
SortedFiles=Files(ind); 
SortedFilesLickBin = loadbin(SortedFiles);
save([binpath '\' 'lickbin.mat'],'SortedFilesLickBin')
disp('finished')