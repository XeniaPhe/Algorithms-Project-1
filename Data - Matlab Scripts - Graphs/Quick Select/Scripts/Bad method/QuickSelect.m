FetchVariables;
fid = fopen('quickselect.txt');
format = '%d    (%f, %d)';
size = [3 Inf];

data = fscanf(fid,format,size)';
fclose(fid);

len = length(data);
min = data(1,1);
max = data(len,1);
nValues = [max:-(max-min)/len:min+1];
nValues = flip(nValues,2);
lognValues = log10(nValues);
nlognValues = nValues.*lognValues;

plot(data(:,1),data(:,2)*10^7,'r',data(:,1),data(:,3),'b',data(:,1),nlognValues,'g');
title('Quick Select');
xlabel(inpSize);
legend(execTime7s,basicOp,nlogn);
xlim([min Inf]);
axis square;