M = csvread('outputs/sheet_02.csv');

M = [zeros(128, 180); M ;zeros(128, 180)];

phase = 29.4056213110678;
angle = 0.9996;
im_I = iradon(M, [phase:angle:angle*179 + phase], 'cubic', 'Hamming');
imwrite(im_I, 'outputs/im_I.png')

im_B = im2bw(im_I,0.2);

% Get the ratio_de
ratio_de = sum(im_B) / sum(im_I);

% Get the index
cols = sum(im_B');
flag = 0;
for i = 1:length(cols)
    if flag == 0 && (cols(i)>0)
        index_x = i;
        index_1 = i;
        flag = 1;
    else if flag == 1 && (cols(i) == 0)
            index_x = (index_x + i - 1) / 2;
            index_2 = i;
            break;
        end
    end
end

rows = sum(im_B);
flag = 0;
for i = 1:length(rows)
    if flag == 0 && (rows(i)>0)
        index_y = i;
        flag = 1;
    else if flag == 1 && (rows(i) == 0)
            index_y = (index_y + i - 1) / 2;
            break;
        end
    end
end

ratio_len = (index_2 - index_1) / 80;
x = int16(index_x - 50 * ratio_len):int16(index_x + 50 * ratio_len);
y = int16(index_y - 50 * ratio_len):int16(index_y + 50 * ratio_len);

