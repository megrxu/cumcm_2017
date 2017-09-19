%本程序找出数据点连线的极值点（几何意义为偏离趋势线的点）进行第一次降噪
function FlteredI = FlteringFunc(I)

store = zeros(180,1);
for i=1:180
    store(i) = find(I(:,i)==1);
end

[pks,locs] = findpeaks(store);
locs1 = locs;

[pks,locs] = findpeaks(-1*store);
locs2 = locs;

locs = [locs1;locs2];

I(:,locs) = zeros();
FlteredI = I;
end
