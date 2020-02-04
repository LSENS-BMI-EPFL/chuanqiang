% Author: Chuanqiang Zhang
% Date: 04/02/2020

function Files = loadbin(Files)
% Plot Logging Bin data.
% How to use
% input    output from folderinfo funcktion, and file ID 
% output   plot of selected file. Detailed information see code.
% Version: 4
% Date: 20191228
close();
trialcount = size(Files);
trialcount = trialcount(1) ;

for k = 1:trialcount
    % https://ch.mathworks.com/matlabcentral/answers/19790-indent-a-block-of-code
    fid3=fopen([Files(k).folder '\' Files(k).name],'r');
    if isequal(Files(k).name , 'BHV_Logging.bin')
        data = fread(fid3,[4,Inf],'double');   % if k represented file is 'BHV_Logging.bin'
        % in data array
        % 1  Time
        % 2  Lick
        % 3  Trail
        % 4  Valve
        timestamp = data(1,:);
        ch_lick = data(2,:);
        %subplot(3, 1, 1);
        %plot(timestamp,ch_lick,'r');
        %ylim([-0.01 0.1]);
        %title('Lick');
        ch_trail = data(3,:);
        %subplot(3, 1, 2);
        %plot(timestamp,ch_trail,'g');
        %ylim([-1 10]);
        %title('Trial');
        ch_valve = data(4,:);
        %subplot(3, 1, 3);
        %plot(timestamp,ch_valve,'b');
        %ylim([-1 10]);
        %title('Valve');
        disp([Files(k).folder '\' Files(k).name])
    else
        data = fread(fid3,[2,Inf],'double');   % if k represented file is not 'BHV_Logging.bin'    
        % in data array
        % 1  Time
        % 2  Lick 
        timestamp = data(1,:);
        ch_lick = data(2,:);
        %subplot(1, 1, 1);
        %plot(timestamp,ch_lick,'r');
        %ylim([-0.01 0.1]);
        %title('Lick');
        disp([Files(k).folder '\' Files(k).name]);
        fclose(fid3);
        Files(k).lick = ch_lick;
        %disp("Plotting finished.")
    end
end


end
