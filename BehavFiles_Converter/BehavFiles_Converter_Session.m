% Use example:      BehavFiles_Converter('CZ004','xxx')
% First edition by George
% Modified by C.Zhang
% Date: 20191218
% Note: 
% 1) Input path subDate folder should not contain any files,otherweise error will occur.
% 2) Always double check the outcome

function BehavFiles_Converter_Session(SessionPath)
%%% Mouse example 'CZ004'
%%% Date example '20191119'
%%% 
% to edit input path
%inputmainPath = 'K:\';
%subMouse = 'CZ004';
%subDate = '20191119';
%dir([inputmainPath Mouse]);;
pathouts=regexp(SessionPath,'\','split');
% https://ch.mathworks.com/matlabcentral/answers/83033-separate-path-string-into-drive-and-folders
% https://ch.mathworks.com/matlabcentral/answers/174253-how-to-convert-a-1x1-cell-to-a-string

Mouse = char(pathouts(6));
Date = char(pathouts(9));


% to edit output path
%outputmainPath = 'K:\';
% outputpath = SessionPath ;
% mkdir(outputpath);
% Do not edit following parts

% BehavFiles = dir(SessionPath);
% BehavFiles(1:2) = [];   % Just in order to remove the . and .. folder

ResultsFinal = {};
ResultsFinal.data = [];
TrialsToExlude = [];

  
ResultsTemp = importdata([SessionPath  ,'\Results.txt']);
disp(size(ResultsTemp.data))
EarlyLicksTemp = importdata([SessionPath, '\EarlyLicks.txt']);
disp(size(EarlyLicksTemp.data))
if isa(EarlyLicksTemp,'cell')
  disp("No earlylicks detected, no need to translate.")
  return;
end
TrialNumberResults = ResultsTemp.data(:,1);
TrialNumberEarlyLicks = EarlyLicksTemp.data(:,1);
WhStD = ResultsTemp.data(:,2);
QW = ResultsTemp.data(:,3);
ITI = ResultsTemp.data(:,4);
StNoStim = ResultsTemp.data(:,6);
WhNoWh = ResultsTemp.data(:,7);
AuNoAu = ResultsTemp.data(:,8);
Lick  = ResultsTemp.data(:,9);
Perf = ResultsTemp.data(:,10);
RT = ResultsTemp.data(:,11);
TrialTime = ResultsTemp.data(:,13);
RwNoRw = ResultsTemp.data(:,14);
AudRw = ResultsTemp.data(:,15);
WhRw = ResultsTemp.data(:,16);
AudD = ResultsTemp.data(:,17);
AudA = ResultsTemp.data(:,18);
AudF = ResultsTemp.data(:,19);

TrialNumberTemp = [];
PerfTemp = [];
WhStDTemp = [];
QWTemp = [];
ITITemp = [];
StNoStimTemp = [];
WhNoWhTemp = [];
AuNoAuTemp = [];
LickTemp = [];
RTTemp = [];
TrialTimeTemp = [];
RwNoRwTemp = [];
AudRwTemp = [];
WhRwTemp = [];
AudDTemp =  [];
AudATemp = [];
AudFTemp = [];



for j = 1:size(TrialNumberResults,1)
    N = sum((TrialNumberEarlyLicks == TrialNumberResults(j)));  
    TrialNumberTemp = [TrialNumberTemp; TrialNumberResults(j); TrialNumberResults(j)*ones(N,1)];  
    PerfTemp = [PerfTemp ; 6*ones(N,1); Perf(j)];  
    WhStDTemp = [WhStDTemp ; NaN*ones(N,1) ; WhStD(j)];
    QWTemp = [QWTemp ; NaN*ones(N,1) ; QW(j)];
    ITITemp = [ITITemp ; NaN*ones(N,1) ; ITI(j)];
    StNoStimTemp = [StNoStimTemp ; NaN*ones(N,1) ; StNoStim(j)];
    WhNoWhTemp = [WhNoWhTemp ; NaN*ones(N,1) ; WhNoWh(j)];
    AuNoAuTemp = [AuNoAuTemp ; NaN*ones(N,1) ; AuNoAu(j)];
    LickTemp  = [LickTemp ; NaN*ones(N,1) ; Lick(j)];
    RTTemp  = [RTTemp ; NaN*ones(N,1) ; RT(j)];
    TrialTimeTemp  = [TrialTimeTemp ; NaN*ones(N,1) ; TrialTime(j)];
    RwNoRwTemp  = [RwNoRwTemp ; NaN*ones(N,1) ; RwNoRw(j)];
    AudRwTemp  = [AudRwTemp ; NaN*ones(N,1) ; AudRw(j)];
    WhRwTemp  = [WhRwTemp ; NaN*ones(N,1) ; WhRw(j)];
    AudDTemp  = [AudDTemp ; NaN*ones(N,1) ; AudD(j)];
    AudATemp  = [AudATemp ; NaN*ones(N,1) ; AudA(j)];
    AudFTemp  = [AudFTemp ; NaN*ones(N,1) ; AudF(j)];   
end

ResultsFinalTemp = [TrialNumberTemp WhStDTemp QWTemp ITITemp StNoStimTemp  WhNoWhTemp AuNoAuTemp LickTemp PerfTemp RTTemp TrialTimeTemp ...
   RwNoRwTemp AudRwTemp WhRwTemp AudDTemp AudATemp AudFTemp];

ResultsFinal.data = [ResultsFinal.data ; ResultsFinalTemp];


TrialNumber = (1:size(ResultsFinal.data,1))';
ResultsFinal.data = [TrialNumber ResultsFinal.data];


for k = 1:size(ResultsFinal.data,1)    
    if ismember(ResultsFinal.data(k,1),TrialsToExlude)      
        ResultsFinal.data(k,10) = NaN;
    end    
end

ResultsFinal.header = [{'TrialNumber'},{'TrialNumberOriginal'},{'WhiskerStimDur'},{'QuietWindow'},{'ITI'},{'Stim/NoStim'},{'Wh/NoWh'},{'Aud/NoAud'},{'Lick'} ...
    {'Performance'},{'ReactionTime'},{'TrialTime'},{'Rew/NoRew'},{'AudRw'},{'WhRw'},{'AudDur'},{'AudAmp'},{'AudFreq'}]; 
BehavResults = ResultsFinal;

% save([outputpath,[subPathprefix,'BehavResults.mat']],'BehavResults');      % (For testing purpose only.)
save([SessionPath,'\','BehavResults.mat'],'BehavResults');



disp(size(BehavResults.data))
clear all 
disp("finished...")


end
