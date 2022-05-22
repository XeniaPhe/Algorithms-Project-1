FetchVariables;
fid = fopen('quicksortWorst.txt');
format = '%d    (%f, %d)';
size = [3 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

len = length(data);
min = data(1,1);
min2 = data(1,2);
min3 = data(1,3);
max = data(len,1);
n2Values = [max:-(max-min)/len:min+1].^2;
n2Values = flip(n2Values,2);
min4 = n2Values(1);

plot(data(:,1),data(:,2)/min2,'r',data(:,1),1.5*n2Values/min4,'g');
title('Quick Sort Worst Case');
xlabel(inpSize);
legend("x"+num2str(min2) + " seconds","1.5"+n2);
xlim([min Inf]);
axis square;