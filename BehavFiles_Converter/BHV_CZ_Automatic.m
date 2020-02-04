% Author: Chuanqiang Zhang
% Date: 04/02/2020

%% copy *.txt from server

%server_path   = '\\sv1files.epfl.ch\Petersen-Lab\data\CZ\CZ_BHV\'            % Server LSENS
%local_server = '\\sv-07-056\cz\Data_Local\BHV_Data'
%default_path = '\\files7\data\czhang\input\'                                 % CZhang Default 
%output_path = '\\files7\data\czhang\output\'                                 % CZhang Default   (Remember always use ' ' for path, instead of " " )

%*** https://stackoverflow.com/questions/472692/how-to-copy-a-directory-structure-but-only-include-certain-files-using-windows/8074994
%*** https://ss64.com/nt/robocopy-exit.html
% dos("ROBOCOPY \\sv1files.epfl.ch\Petersen-Lab\data\CZ\CZ_BHV\ C:\Destination\ EarlyLicks.txt Results.txt /E /LEV:4")

%dos("ROBOCOPY " + local_server +" " + default_path + " " + "EarlyLicks.txt Results.txt /E /LEV:4");



% https://stackoverflow.com/questions/31142046/system-dir-call-to-network-drive-prunes-file-path

%% Translate two *.txt files into a single *.mat   (example)

BehavFiles_Converter('CZ004','20191112', default_path, output_path)
 
%% Listing folder, extract Mouse name and date

% https://stackoverflow.com/questions/27337514/matlab-dir-without-and
% https://ch.mathworks.com/matlabcentral/answers/7155-elegant-way-to-extract-part-of-a-structure-as-an-array
clc
Mouse=dir(default_path);

% https://ch.mathworks.com/matlabcentral/answers/335071-how-can-i-filter-struct-according-to-strings-in-field
% https://ch.mathworks.com/help/matlab/ref/contains.html
% https://ch.mathworks.com/help/matlab/ref/strcmp.html

Mousename = Mouse(contains({Mouse.name}, 'CZ'))


% Mouse name forloop  (old version)
% mouse_id = struct([])
% for i=1:length(Mouse)
%     mousename = Mouse(i).name;
%     if strcmp(mousename,'.')  % do nothing        
%         continue;
%     end
%     if strcmp(mousename,'..') % do nothing          
%         continue;
%     end
%     mouse_id(i).name= mousename;
% end

%% Date forloop
clc
Mousedate = dir([default_path , 'CZ001'])
Mousedatefolder = Mousedate(contains({Mousedate.name}, '20'))  % 20 was only chosen because 2019 2020 all include 20. It will work for 80 years :)

% Mousedate forloop  (old version)
% Mousedate=dir([default_path , 'CZ001'])
% for i=1:length(Mousedate)
%     mousedate = Mousedate(i).name;
%     if strcmp(mousedate,'.')  % do nothing
%             continue;
%     end
%     if strcmp(mousedate,'..') % do nothing
%             continue;
%     end
%     disp(mousedate)
% end


%%
clc
for i= 1:length(Mousename)
    Mousedate = dir([default_path , Mousename(i).name]);
    Mousedatefolder = Mousedate(contains({Mousedate.name}, '20'));
    for j= 1:length(Mousedatefolder)
        disp([Mousename(i).name,'  ',Mousedatefolder(j).name] )
        if length(dir([default_path , Mousename(i).name,'\', Mousedatefolder(j).name]))>3
            disp("Multipul sessions within one day!!!")
            continue;
        end
        % disp([num2str(i),'  ' ,num2str(j)])  (for testing purpose, if you want to display two number variables.)
        BehavFiles_Converter( Mousename(i).name, Mousedatefolder(j).name , default_path, output_path )
    end
end


