% Author: Chuanqiang Zhang
% Date: 04/02/2020



clear all
clc
SessionPath=  '\\sv-07-056\CZ\Data_Local\CZ009\Recording\BHV\CZ009_20200109\165629' ;

% Load mat data
load([SessionPath ,'\BehavResults.mat']);
load([SessionPath ,'\lickbin.mat']);

Perf= BehavResults.data(:,10);
Audhitcount=0;
Whhitcount=0;
for i= 1:size(BehavResults.data)
       
    TrialPerf= BehavResults.data(i,10);
    if TrialPerf==5
        Audhitcount=Audhitcount+1;
        Audreaction(Audhitcount).hit= BehavResults.data(i,11);        
    end
    
    if TrialPerf==3
        Whhitcount=Whhitcount+1;
        Whreaction(Whhitcount).hit= BehavResults.data(i,11);        
    end
    
end

% https://ch.mathworks.com/matlabcentral/answers/478420-going-from-structure-to-matrix
scatter([1:Audhitcount],struct2array(Audreaction));
figure()
scatter([1:Whhitcount],struct2array(Whreaction));

  

    
    
    
