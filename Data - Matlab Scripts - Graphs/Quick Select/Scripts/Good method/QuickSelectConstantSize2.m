FetchVariables;
fid = fopen('quickselectconstantsize.txt');
format = '%d     %f';
size = [2 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

n=100000;
len = length(data);
min = data(1,2);
nValues = ones(1,len);

plot(data(:,1),data(:,2)/min,'m',data(:,1),nValues,'g');
title('Quick Select Constant Size');
xlabel("Element Index");
legend("x "+num2str(min) + " seconds","x "+nlogn + " (n="+n + ")");
xlim([min Inf]);
axis square;