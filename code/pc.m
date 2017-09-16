M = csvread('outputs/sheet_02.csv');
im_M = (M / max(max(M)));

M = [zeros(64, 180); M ;zeros(64, 180)];

size(M)
phase = 29.4;
im_I = iradon(M, [phase:1.002:1.002*179 + phase], 'cubic', 'Hamming');

figure;
imshow(im_M);

figure
imshow(im_I);
size(im_I)
imwrite(im_I, 'outputs/im_I.png')