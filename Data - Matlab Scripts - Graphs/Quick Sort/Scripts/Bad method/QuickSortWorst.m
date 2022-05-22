FetchVariables;
fid = fopen('quicksortWorst.txt');
format = '%d    (%f, %d)';
size = [3 Inf];

data = fscanf(fid,format,size)';
data = data(:,1:2);
fclose(fid);

len = length(data);
min = data(1,1);
max = data(len,1);
n2Values = [max:-(max-min)/len:min+1].^2;
n2Values = flip(n2Values,2);

plot(data(:,1),data(:,2)*10^7,'r',data(:,1),0.5*n2Values,'g');
title('Quick Sort Worst Case');
xlabel(inpSize);
legend(execTime7s,"0.5"+n2);
xlim([min Inf]);
axis square;