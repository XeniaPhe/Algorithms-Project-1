FetchVariables;
fid = fopen('select30th.txt');
format = 'size is:  %d  time and comp count is:  (%f, %d)\n';
size = [3 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

len = length(data);
min = data(1,1);
max = data(len,1);
nValues = [max:-(max-min)/len:min+1];
nValues = flip(nValues,2);

for i = 1:1:len
    nValues(i) = nValues(i)*data(i,1);
end

plot(data(:,1),data(:,2)*10^7,'r',data(:,1),data(:,3),'b',data(:,1),4.5*nValues,'g');
title('Partial Selection Sort 30th Percentile');
xlabel(inpSize);
legend(execTime7s,basicOp,"4.5k"+n);
xlim([min Inf]);
axis square;