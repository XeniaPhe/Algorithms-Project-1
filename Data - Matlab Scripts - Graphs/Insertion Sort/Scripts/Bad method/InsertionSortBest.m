FetchVariables;
fid = fopen('insertionBest.txt');
format = '%d    (%f, %d)';
size = [3 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

len = length(data);
min = data(1,1);
max = data(len,1);
nValues = [max:-(max-min)/len:min+1];
nValues = flip(nValues,2);

plot(data(:,1),data(:,2)*10^7,'r',data(:,1),data(:,3),'b',data(:,1),2*nValues,'g');
title('Insertion Sort Best Case');
xlabel(inpSize);
legend(execTime7s,basicOp,"2"+n);
xlim([min Inf]);
axis square;