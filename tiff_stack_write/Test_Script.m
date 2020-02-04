% Author: Chuanqiang Zhang
% Date: 04/02/2020

% Test Script

folder= 'Z:\Data_Local\CZ002\Training\20191213\140328'

folderxinfo=dir('Z:\Data_Local\CZ002\Training\20191213\140328');

X=folderxinfo(contains({folderxinfo.name}, 'trial_'));

[tmp_X ind_X]=natsortfiles({X.name});  
X_task=X(ind_X);  


for i=1:length(X_task)

    tiff_stack_write([folder '\' X_task(i).name], [folder '\' 'test' '\' X_task(i).name '.tif'])
    
end

disp(finished)