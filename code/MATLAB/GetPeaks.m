%GetPeaks可以获取每一列中的较大的四个极值点位置，返回store储存这些位置
%这些位置即为图像的边界信息
function store = GetPeaks(fy,i)

fy_negative = -1*fy;

[pks,locs] = findpeaks(fy(:,i));
location = FindProperPeaks(pks,locs);
store(1)=location(1);
store(2)=location(2);

[pks,locs] = findpeaks(fy_negative(:,i));
location = FindProperPeaks(pks,locs);
store(3)=location(1);
store(4)=location(2);

end
