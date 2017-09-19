%本程序求出圆心轨迹与椭圆中心轨迹的振幅，在此基础上求解旋转中心的位置
clear all
I1 = csvread('SplinedEllipse.csv');
I2 = csvread('SplinedRound.csv');

y1 =[];
x1 =[];
y2 =[];
x2 =[];

for i=1:180
        y1 = [y1;find(I1(:,i)==1)];
        x1 = [x1;i];
end

for i=1:180
        y2 = [y2;find(I2(:,i)==1)];
        x2 = [x2;i];
end

k1  = find(y1==min(y1));
k2  = find(y2==min(y2));

c1 = max((y1(1)+y1(180))/2-y1(k1));
c2 = max((y2(1)+y2(180))/2-y2(k2));

Ratio = 1.01085271318*(((288/80) + (107/30))/2);
radius1 = c1/Ratio;
radius2 = c2/Ratio;
%解方程
syms x y
S1=x^2+y^2-radius1^2;
S2=(x-45)^2+y^2-radius2^2;
[x,y]=solve(S1,S2);

%以现实中的距离表示
vpa(x)
vpa(y)
%以像素表示
round(Ratio*vpa(x))
round(Ratio*vpa(y))




