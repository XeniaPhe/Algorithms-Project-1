FetchVariables;
fid = fopen('select50th.txt');
format = 'size is:  %d  time and comp count is:  (%f, %d)\n';
size = [3 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

len = length(data);
min = data(1,1);
min2 = data(1,2);
min3 = data(1,3);
max = data(len,1);
nValues = [max:-(max-min)/len:min+1];
nValues = flip(nValues,2);

for i = 1:1:len
    nValues(i) = nValues(i)*data(i,1);
end

min4 = nValues(1);

plot(data(:,1),data(:,2)/min2,'r',data(:,1),data(:,3)/min3,'b',data(:,1),1.10*nValues/min4,'g');
title('Partial Selection Sort 50th Percentile');
xlabel(inpSize);
legend("x"+num2str(min2) + " seconds","x"+num2str(min3)+" operations","1.10k"+n);
xlim([min Inf]);
axis square;