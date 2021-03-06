run getParas.m

M = csvread('outputs/sheet_05.csv');
M = [zeros(128, 180); M ;zeros(128, 180)];

phase = 29.4056213110678;
im_I = iradon(M, [phase:0.9996:0.9996*179 + phase], 'cubic', 'Hamming');
im_Res = im_I(x, y) * ratio_de;
im_Res = im_Res .* (im_Res>0.05);
im_Res = imresize(im_Res, [256 256]);
%csvwrite('outputs/result_5.csv', im_Res)
imshow(im_Res/max(max(im_Res)))