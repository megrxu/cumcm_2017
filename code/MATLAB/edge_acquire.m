%本程序判断并获得附录2图像的边界点，store中1、2、3、4列分别存储4条边界线上点的坐标。
clear all;
%读取附录2中的图像
I = xlsread('A2.xlsx');
%获取图像的梯度信息
[FX,FY] = gradient(I);

store = zeros(180,4);

%获取边界信息
for i=1:180    
store(i,:) = GetPeaks(FY,i);
end

Image = zeros(512,180);
%获取圆边界
for i=1:180
    Image(store(i,1),i) = 0;
    Image(store(i,2),i) = 1;
    Image(store(i,3),i) = 0;
    Image(store(i,4),i) = 1;
end

%获取椭圆边界
%for i=1:180
    %Image(store(i,1),i) = 1;
    %Image(store(i,2),i) = 0;
    %Image(store(i,3),i) = 1;
    %Image(store(i,4),i) = 0;
%end

%显示获得的图形
figure;
imshow(Image);


%导出圆心、椭圆中心轨迹坐标
csvwrite('Image_round.csv',Image);  
%csvwrite('Image_ellipse.csv',Image);  



