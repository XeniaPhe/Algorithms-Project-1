FetchVariables;
fid = fopen('quickselectconstantsize.txt');
format = '%d     %f';
size = [2 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

n=100000;
len = length(data);
nValues = ones(1,len).*n.*log10(n);

plot(data(:,1),data(:,2)*10^7,'m',data(:,1),nValues,'g');
title('Quick Select Constant Size');
xlabel("Element Index");
legend(execTime7s,nlogn + " (n="+n+")");
xlim([0 Inf]);
axis square;