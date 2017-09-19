%FindProperPeaks函数筛选出边界点位置并返回它们
function location = FindProperPeaks(pks,locs)
    a = [-pks';locs'];
    a =a';
    aa = sortrows(a,1);
    location(1) = aa(1,2);
    location(2) = aa(2,2);
end