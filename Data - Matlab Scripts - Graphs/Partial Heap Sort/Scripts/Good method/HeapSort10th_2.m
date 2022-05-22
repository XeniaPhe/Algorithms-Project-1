FetchVariables;
fid = fopen('heap10th.txt');
format = 'size is :   %d  time is :  %f   %d\n';
size = [3 Inf];

data = fscanf(fid,format,size)';
data = data(:,1:2);
fclose(fid);

len = length(data);
min = data(1,1);
min2 = data(1,2);
max = data(len,1);
nValues = [max:-(max-min)/len:min+1];
nValues = flip(nValues,2);
nlogkValues = log10(data(:,1)*0.1);

for i = 1:1:len
    nlogkValues(i) = nValues(i)*nlogkValues(i);
end
min3 = nlogkValues(1);

plot(data(:,1),data(:,2)/min2,'r',data(:,1),4*nlogkValues/min3,'g');
title('Heap Sort 10th Percentile');
xlabel(inpSize);
legend("x"+num2str(min2) + " seconds","4"+nlogk);
xlim([min Inf]);
axis square;