%本程序对edge_acquire中获得的边缘进行两次降噪，并利用三次样条插值补全降噪后噪点处的数据
%本程序产生记录模板圆的圆心部分轨迹和椭圆形部分中心轨迹的csv文件
%为SplinedRound.csv与SplinedEllipse.csv。

%FlteringFunc(I)函数找出梯度较大的点（偏离轨迹较远）并去除
%Image_ellipse1.csv、Image_ellipse2.csv、Image_round1.csv、
%Image_round1.csv分别存储每一条边界线上点的位置

I = csvread('Image_ellipse2.csv');
ImageUp = FlteringFunc(I);

I = csvread('Image_ellipse1.csv');
ImageDown = FlteringFunc(I);

I = ImageUp + ImageDown;

%上下边际线靠的太近时需要删除，第二次降噪
for i = 1:180
    if sum(I(:,i)) == 2
      x=find(I(:,i)==1); 
      if x(2)-x(1) <= 10
        I(:,i)=zeros();
      end
    end
end
%合成图像若某一列仅有一个点，无法获得圆心（或椭圆中心轨迹），需要删除
for i=1:180
    if sum(I(:,i)) ~= 2
        I(:,i)=zeros();
    end
end

ImageAve = zeros(512,180);
for i=1:180
    if sum(I(:,i)) == 2
        x=find(I(:,i)==1)
        ave = round(0.5*(x(1)+x(2))); %四舍五入
        ImageAve(ave,i) = 1;
    end
end

clear x
clear y
y =[];
x =[];
for i=1:180
    if sum(ImageAve(:,i)) ==1 
        y = [y;find(ImageAve(:,i)==1)];
        x = [x;i];
    end
end
%三次样条插值，yy记录每一列的圆心（或椭圆中心）的纵坐标
yy = spline(x,y,[1:180]);
yy = round(yy)

ImageSplined = zeros(512,180);

for i=1:180
ImageSplined(yy(i),i)=1;
end

figure;
imshow(ImageSplined);
csvwrite('SplinedEllipse.csv',ImageSplined);
%圆心轨迹时写入文件
%csvwrite('SplinedRound.csv',ImageSplined);

